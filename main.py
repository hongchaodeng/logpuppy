#!/usr/bin/env python

import curses
import sys
import time

from logmonitor.logreader     import LogReader
from logmonitor.logpublisher  import LogPublisher
from logmonitor.logsubscriber import LogSubscriber
from logmonitor.loganalyzer   import LogAnalyzer
from logmonitor.logdisplay    import LogDisplay


def logmonitor(stdscr, *args, **kwargs):
    # init
    reader = LogReader(sys.argv[1])
    publisher = LogPublisher(reader)
    analyzer = LogAnalyzer(sys.argv[2])
    display = LogDisplay(stdscr, analyzer)

    publisher.addSubscriber(
            LogSubscriber(10, display.refresh_most_hits)
            )
    publisher.addSubscriber(
            LogSubscriber(1, display.refresh_alert)
            )

    # main loop
    while 1:
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
