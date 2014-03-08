# LogPublisher:
# - subscriber_queue:
# - reader:
class LogPublisher(object):

    def __init__(self, reader):
        self.subscriber_queue = []
        self.reader = reader

    def add_subscriber(self, subscriber):
        self.subscriber_queue.append(subscriber)

    def publish(self):
        logs = self.reader.readlines()
        for subscriber in subscriber_queue:
            subscriber.mail(logs)
