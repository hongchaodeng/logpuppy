Log-Puppy: A Console Program for HTTP Log Monitor
======

What Is It
------
This is a console program that monitors an actively written to HTTP log (e.g. apache log). Think of it a **htop** for apache log.

Currently, it provides two kinds of information:

* Every 10s, displays the most visited section
* If traffic in past 2 minutes went high or recovered, shows and keeps messages in a rotating manner.

Note that and traffic and threshold here means **hits per second**.

### Screenshots

![enter image description here][1]

![enter image description here][2]

How to Use It
------
Enter into the 'logpuppy/' directory, type
        
        $ ./main <logfile> <threshold>
        
Where first argument is the log file to be monitored, second argument is the threshold that judges if traffic is high.

Use *Ctrl + C* to quit the program.

Architecture
------
![enter image description here][3]


Testing for Alerting Logic
------

The alert has 4 cases:

* **Not alerting** receives **Low** traffic. Nothing happens.
* **Not alerting** receives **High** traffic. Become alerting and add alert message.
* **Alerting** receives **High** traffic. Nothing happens.
* **Alerting** receives **Low** traffic. Become not alerting and add a recovery message.

Future Improvement
------
There are many kinds of improvement that could be done on this project. Here I am listing some of them:

* Write all alerts and recover messages to disk. These things are logs themselves.
* Handle exceptions for parsing external logs in a proper manner.
* Add keystroke handler to receive user input.
* The publish for loop has overhead that makes it not exactly 1s interval. This can be nicely solved in Go by using channels and goroutine.


  [1]: pictures/Selection_001.png
  [2]: pictures/Selection_002.png
  [3]: pictures/arch.png
