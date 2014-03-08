# LogSubscriber
# - interval: In this program the time unit is one second.
# - - This is the interval between two callbacks. We use a temp counting.
# - callback: callback will be called with the logs stored during interval.
class LogSubscriber(object):

    def __init__(self, interval, callback):
        self.interval = interval
        self.count = interval
        self.callback = callback
        self.logs = []

    def mail(self, logs):
        self.logs.append(logs)
        self.count -= 1
        if self.count == 0:
            self.callback(self.logs)
            self.logs = []
            self.count = self.interval

