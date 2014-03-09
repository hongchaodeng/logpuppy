#!/usr/bin/env python

import curses
import sys
import time

from logmonitor.logreader     import LogReader
from logmonitor.logpublisher  import LogPublisher
from logmonitor.logsubscriber import LogSubscriber
from logmonitor.loganalyzer   import LogAnalyzer
from logmonitor.logdisplay    import LogDisplay

# Note (03/09/14):
# Here I choose 1 second interval between publish activities. And therefore it is also
# the minimal time unit for subscriber.
# The reason I chose this and tradeoff I made
# 1. The traffic counting of past 2 minutes uses a sliding window which requires minimal
#    granularity. If the interval is too small, the computational load will be very high;
#    if the interval is too large, the precision will be very low. 1 second is one of the
#    reasonable choices.
# 2. publisher will do publish every interval. This includes reading logs and notifying
#    every subscriber (subscriber will decide whether to callback by another count).
#    Publish interval has the similar tradeoff as above.
def logmonitor(stdscr, *args, **kwargs):
    # init
    reader    = LogReader(sys.argv[1])
    publisher = LogPublisher(reader)
    analyzer  = LogAnalyzer(sys.argv[2])
    display   = LogDisplay(stdscr, analyzer)

    publisher.add_subscriber(
            LogSubscriber(10, display.refresh_most_hits)
            )
    publisher.add_subscriber(
            LogSubscriber(1, display.refresh_alert)
            )

    # publish event every one second
    while True:
        time.sleep(1)
        publisher.publish()

    # deinit
    reader.close()

def main():
    curses.wrapper(logmonitor)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usgae: ./main.py <logfile> <threshold>"
        exit(-1)
    main()
