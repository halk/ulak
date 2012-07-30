ulak
====

Ulak periodically sends you a summary of NewRelic reports to your inbox.

Trivia: ulak is Turkish and means courier or messenger.

installation
------------

    $ virtualenv --no-site-packages ulak
    $ cd ulak
    $ source bin/activate
    $ git clone git@github.com:halk/ulak.git
    $ cd ulak
    $ pip install -r requirements.txt
    $ cp config-dist.py config.py