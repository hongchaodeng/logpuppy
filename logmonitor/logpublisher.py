# LogPublisher:
# - subscriber_queue:
# - reader:
class LogPublisher(object):

    def __init__(self, reader):
        self.subscriber_queue = []
        self.reader = reader

    def addSubscriber(self, subscriber):
        self.subscriber_queue.append(subscriber)

    def publish(self):
        pass
