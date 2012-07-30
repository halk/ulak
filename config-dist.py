# -*- coding: utf-8 -*-

class Config(object):

    PROJECTS = {
        'myProject': {                                          # project shortname e.g. ulak
            'NR_ACCOUNT_ID': '',                                # NewRelic account id
            'NR_LOGIN_EMAIL': 'info@example.com',               # NewRelic email address
            'NR_LOGIN_PASSWORD': 'pass',                        # NewRelic password
            'NR_ERROR_REPORT_FOR_APPS': {                       # Selection of NewRelic apps to get error reports
                'www.example.com': '123456',
                'be.example.com':  '123457'
            },

            'EMAIL_TO':   ['admin@example.com'],                # Recipients of report
            'EMAIL_FROM': 'no-reply@example.com',               # Sender of report

            'PROJECT_LOGO': 'http://example.com/logo.png'       # Project logo
        }
    }