ulak
====

ulak periodically sends you a summary of NewRelic reports to your inbox.

trivia: ulak is Turkish and means courier or messenger.

installation
------------

    $ virtualenv ulak
    $ cd ulak
    $ source bin/activate
    $ git clone git@github.com:halk/ulak.git
    $ cd ulak
    $ pip install -r requirements.txt
    $ cp config-dist.py config.py
    $ python ulak.py -h

crons (example)
---------------

    SHELL=/bin/bash
    # will sent a report every 3 hours starting from 11am to 11pm
    0 11,14,17,20,23 * * * cd /yourDir/ulak/ulak/; source ../bin/activate; python ulak.py --hours=3 yourProject
    # will sent a report of 12 hours on 8am - covering the night
    0 8 * * * cd /yourDir/ulak/ulak/; source ../bin/activate; python ulak.py --hours=12 yourProject

troubleshooting
---------------

- you need libxml2 and libxslt to be able to install lxml