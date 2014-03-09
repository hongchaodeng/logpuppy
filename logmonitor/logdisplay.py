from collections import deque

class Alerts(object):
    def __init__(self, capacity):
        self.queue = deque()
        self.cap = capacity

    def add(self, msg):
        self.queue.appendleft(msg)
        if len(self.queue) > self.cap:
            self.queue.pop

    def get_recent(self):
        return self.queue


# LogDisplay
# - stdscr
# - analyzer
# - alerts
class LogDisplay(object):
    MOST_HITS_RESERVED = 1
    AVG_TRAF_RESERVED  = 1
    END_RESERVED       = 1

    def __init__(self, stdscr, analyzer):
        self.stdscr = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.analyzer = analyzer
        self.alerts = Alerts(self.height -
                self.MOST_HITS_RESERVED - self.AVG_TRAF_RESERVED - self.END_RESERVED)

        self.stdscr.addstr(0, 0, self.width_long("Wait 10+ seconds"))
        self.stdscr.refresh()

    # helper function to fit line into console window width
    def width_long(self, line):
        if self.width - len(line) > 0:
            sweeping = " " * (self.width - len(line))
        else:
            sweeping = ""
        return line[:self.width] + sweeping

    def refresh_most_hits(self, logs):
        self.analyzer.analyze_most_hits(logs)
        section, hits = self.analyzer.most_hits
        self.draw_most_hits(section, hits)

    def refresh_alert(self, logs):
        msg = self.analyzer.analyze_alert(logs)
        self.draw_average_traffic()
        if msg:
            self.alerts.add(msg)
            self.draw_alerts()

    def draw_most_hits(self, section, hits):
        output = "Section '%s' has most hits: %d" % (section, hits)
        self.stdscr.addstr(0, 0, self.width_long(output))
        self.stdscr.refresh()

    def draw_average_traffic(self):
        avg_update = self.width_long(
                "Average traffic: {:.2f}".format(self.analyzer.traffic.average()))
        self.stdscr.addstr(1, 0, avg_update)
        self.stdscr.refresh()

    def draw_alerts(self):
        row = self.MOST_HITS_RESERVED + self.AVG_TRAF_RESERVED
        for msg in self.alerts.get_recent():
            if self.width - len(msg) > 0:
                sweeping = " " * (self.width - len(msg))
            else:
                sweeping = ""
            self.stdscr.addstr(row, 0, self.width_long(msg))
            row += 1
            if row == self.height - self.END_RESERVED:
                break
        self.stdscr.refresh()

