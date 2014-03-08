import re

class Traffic:

    def __init__(self, time_interval):
        self.queue = [0 for _ in xrange(time_interval)]
        self.cap = time_interval
        self.count = 0
        self.pos = 0
        self.avg = 0.0

        self.pattern_url = re.compile(r'\S+ \S+ \S+ \[.+\] "\S+ (\S+) \S+"')
        self.pattern_section = re.compile(r'/(.*?)/')
        self.pattern_section_single = re.compile(r'/(.*?)')

    def add(self, item):
        pos = (self.pos + 1) % self.cap
        old_value = self.queue[pos]
        self.queue[pos] = item
        self.pos = pos

        self.avg = self.avg * self.count
        if self.count < self.cap:
            self.count += 1
        else:
            self.avg -= old_value
        self.avg = (self.avg * + item) / self.count

    def average(self):
        return self.avg


# LogAnalyzer
# # For most hits
# - section_hits: map of key 'section' and value 'hits'
# - most_hits: tuple of the (maximum hits section, hits)
# # for alerts
# - threshold:
# - traffic
class LogAnalyzer(object):

    def __init__(self, threshold_s):
        # for most hits
        self.section_hits = {}
        self.most_hits = ("", 0)
        # for alerts
        self.threshold = int(threshold_s)
        self.traffic = Traffic(2 * 60)

    def analyze_most_hits(self, logs):
        for line in logs:
            try:
                m_url = self.pattern_url.match(line)
                url = m.group(1)
                m_section = self.pattern_section.match(url)
                if m_section == None:
                    m_section = self.pattern_section_single.match(url)
                section = m_section.group(1)

                # update
                if section not in self.section_hits:
                    self.section_hits[section] = 1
                else:
                    self.section_hits[section] += 1

                if self.section_hits[section] > self.most_hits[1]:
                    self.most_hits[0] = section
                    self.most_hits[1] = self.section_hits[section]

            except:
                # TODO: logging errors
                pass


    def analyze_alert(self, logs):
        pass

