# LogDisplay
# - stdscr
# - analyzer
# - alerts
class LogDisplay(object):

    def __init__(self, stdscr, analyzer):
        self.height, self.width = stdscr.getmaxyx()
        self.analyzer = self.analyzer
        self.alerts = []

    def refresh_most_hits(self, logs):
        self.analyzer.analyze_most_hits(logs)
        section, hits = self.analyzer.most_hits
        self.draw_most_hits(section, hits)

    def draw_most_hits(self, section, hits):
        pass

    def refresh_alert(self, logs):
        self.analyzer.analyze_alert(logs)

        value, time = self.analyzer.high_traffic_record()
        if not value:
            return

        self.alerts.append((value, time))
        self.draw_alerts()

    def draw_alerts(self):
        pass
