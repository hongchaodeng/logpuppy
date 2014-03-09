import re

class Traffic:

    def __init__(self, time_interval):
        self.queue = [0 for _ in xrange(time_interval)]
        self.cap = time_interval
        self.count = 0
        self.pos = 0
        self.avg = 0.0

    def add(self, value):
        pos = (self.pos + 1) % self.cap
        old_value = self.queue[pos]
        self.queue[pos] = value
        self.pos = pos

        self.avg = self.avg * self.count
        if self.count < self.cap:
            self.count += 1
        else:
            self.avg -= old_value
        self.avg = (self.avg + value) / self.count

    def average(self):
        return self.avg


# LogAnalyzer
# # For most hits
# - section_hits: map of key 'section' and value 'hits'
# - most_hits: tuple of the (maximum hits section, hits)
# # for alerts
# - threshold:
# - traffic:
class LogAnalyzer(object):

    def __init__(self, threshold_s):
        # for most hits
        self.section_hits = {}
        self.most_hits = ("", 0)

        self.pattern_url = re.compile(r'^\S+ \S+ \S+ \[.+\] "\S+ (\S+) \S+"')
        self.pattern_section = re.compile(r'/(.+?)/')

        # for alerts
        self.threshold = int(threshold_s)
        self.traffic = Traffic(2 * 60)
        self.pattern_time = re.compile(r'^\S+ \S+ \S+ \[(.+)\]')
        self.alerting = False


    def analyze_most_hits(self, logs):
        # when parsing the string, the program needs to continue running even though
        # the parsing went wrong. This is reasonable because we can't control
        # external input.
        for line in logs:
            try:
                m_url = self.pattern_url.match(line)
                url = m_url.group(1)

                m_section = self.pattern_section.match(url)
                if not m_section:
                    continue
                section = m_section.group(1)

                # update
                if section not in self.section_hits:
                    self.section_hits[section] = 1
                else:
                    self.section_hits[section] += 1

                if self.section_hits[section] > self.most_hits[1]:
                    self.most_hits = (section, self.section_hits[section])

            except:
                # TODO: logging and handling different errors
                pass


    def analyze_alert(self, logs):
        self.traffic.add( len(logs) )

        try:
            m_time = self.pattern_time.match(logs[-1])
            atTime = m_time.group(1)

            if not self.alerting and self.traffic.average() >= self.threshold:
                msg = "High traffic alert - hits = {:.2f}, trigger at {}".format(
                        self.traffic.average(), atTime)
                self.alerting = True
            elif self.alerting and self.traffic.average() < self.threshold:
                msg = "Traffic recovered below {} at {}".format(
                        self.threshold, atTime)
                self.alerting = False
            else:
                msg = ""

            return msg
        except:
            return ""
