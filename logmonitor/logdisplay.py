import curses

# LogDisplay
# - stdscr
# - analyzer
# - alerts
# - alerting
class LogDisplay(object):

    def __init__(self, stdscr, analyzer):
        self.stdscr = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.analyzer = analyzer
        self.alerts = []
        self.alerting = False

        self.draw_most_hits("", 0)

    def refresh_most_hits(self, logs):
        self.analyzer.analyze_most_hits(logs)
        section, hits = self.analyzer.most_hits
        self.draw_most_hits(section, hits)

    def draw_most_hits(self, section, hits):
        output = "Section '%s' has most hits: %d" % (section, hits)
        self.stdscr.addstr(0, 0, output[:self.width], curses.A_REVERSE)
        self.stdscr.refresh()

    def refresh_alert(self, logs):
        self.analyzer.analyze_alert(logs)
        #value, time = self.analyzer.high_traffic_record()
        #self.alerts.append((value, time))
        #self.draw_alerts()

    def draw_alerts(self):
        pass
