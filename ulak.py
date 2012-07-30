# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
from newrelic import NewRelic
from config import Config
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
from inlinestyler.utils import inline_css
import sys
import argparse
import logging
import cssutils
import pprint

if __name__ == '__main__':

    cssutils.log.setLevel(logging.FATAL)

    parser = argparse.ArgumentParser()
    parser.add_argument('projects', metavar='PROJECT', nargs='+', help='The projects to be included in the report (comma-separated)')
    parser.add_argument('--hours', type=int, default=3, help='Report time period in hours (default: 3)')
    parser.add_argument('-p', action='store_const', default=False, const=True, help='Print report out instead of sending email')
    args = parser.parse_args()

    # check projects
    for project_key in args.projects:
        if not project_key in Config.PROJECTS.keys():
            print 'project %s not in configuration' % project_key

    env = Environment(loader=FileSystemLoader('templates'))

    for name, config in Config.PROJECTS.iteritems():
        if not name in args.projects:
            continue

        # init newrelic
        newrelic = NewRelic(config['NR_ACCOUNT_ID'])
        newrelic.login(config['NR_LOGIN_EMAIL'], config['NR_LOGIN_PASSWORD'])

        # load data
        serverssum = newrelic.get_servers_overview()
        appssum = newrelic.get_apps_overview()
        errors = newrelic.get_errors(config['NR_ERROR_REPORT_FOR_APPS'], args.hours)

        # render email
        template = env.get_template('index.html')
        html = template.render(name=name, config=config, hours=args.hours, appssum=appssum, serverssum=serverssum, errors=errors)
        html = inline_css(html.encode('utf-8'))

        # send email
        msg = MIMEText(html, 'html', 'utf-8')
        msg['Subject'] = '%s NewRelic Summary Report' % name.capitalize()
        msg['From'] = config['EMAIL_FROM']
        msg['To'] = ', '.join(config['EMAIL_TO'])

        if args.p:
            print html
        else:
            p = Popen(['/usr/sbin/sendmail', '-t'], stdin=PIPE)
            p.communicate(msg.as_string())
