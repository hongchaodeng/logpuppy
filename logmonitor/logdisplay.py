from collections import deque

class Alerts(object):
    def __init__(self, capacity):
        self.queue = deque()
        self.cap = capacity

    def add(self, msg):
        self.queue.appendleft(msg)
        if len(self.queue) > self.capacity:
            self.queue.pop

    def get_recent(n):
        return self.queue[:n]


# LogDisplay
# - stdscr
# - analyzer
# - alerts
class LogDisplay(object):

    def __init__(self, stdscr, analyzer):
        self.stdscr = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.analyzer = analyzer
        self.alerts = Alerts(self.height)

        self.draw_most_hits("", 0)

    def refresh_most_hits(self, logs):
        self.analyzer.analyze_most_hits(logs)
        section, hits = self.analyzer.most_hits
        self.draw_most_hits(section, hits)

    def draw_most_hits(self, section, hits):
        output = "Section '%s' has most hits: %d" % (section, hits)
        if self.width - len(output) > 0:
            sweeping = " " * (self.width - len(output))
        else:
            sweeping = ""
        self.stdscr.addstr(0, 0, output[:self.width] + sweeping)
        self.stdscr.refresh()

    def refresh_alert(self, logs):
        msg = self.analyzer.analyze_alert(logs)
        if msg:
            self.alerts.add(msg)
            self.draw_alerts()

    def draw_alerts(self):
        msgs = self.alerts.get_recent(self.height - 2)
        for i in xrange(2, self.height):
            msg = msgs[i-2]
            if self.width - len(msg) > 0:
                sweeping = " " * (self.width - len(msg))
            else:
                sweeping = ""
            self.stdscr.addstr(i, 0, msg[:self.width] + sweeping)
        self.stdscr.refresh()

