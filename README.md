ulak
====

ulak periodically sends you a summary of NewRelic reports to your inbox.

trivia: ulak is Turkish and means courier or messenger.

installation
------------

    $ virtualenv ulak
    $ cd ulak
    $ source bin/activate
    $ git clone https://github.com/halk/ulak.git
    $ cd ulak
    $ pip install -r requirements.txt
    $ cp config-dist.py config.py
    $ python ulak.py -h

crons (example)
---------------

    SHELL=/bin/bash
    # will sent a report every 3 hours starting from 11am to 11pm
    0 11,14,17,20,23 * * * yourUser cd /yourDir/ulak/ulak/ && source ../bin/activate && /yourDir/ulak/bin/python ulak.py --hours=3 yourProject > ulak.log
    # will sent a report of 12 hours on 8am - covering the night
    0 8 * * * yourUser cd /yourDir/ulak/ulak/ && source ../bin/activate && /yourDir/ulak/bin/python ulak.py --hours=12 yourProject > ulak.log

troubleshooting
---------------

- you need libxml2 and libxslt to be able to install lxml