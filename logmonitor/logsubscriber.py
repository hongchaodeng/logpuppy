# LogSubscriber
# - interval:
# - count:
# - callback:
# - logs:
class LogSubscriber(object):

    def __init__(self, interval, callback):
        self.interval = interval
        self.count = interval
        self.callback = callback
        self.logs = []

