# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pprint

class NewRelic(object):
    baseUrl = 'https://rpm.newrelic.com/'

    def __init__(self, accountId):
        self.accountId = accountId
        self.s = requests.session()

    def login(self, email, password):
        r = self.s.post(
            self.baseUrl + 'session',
            data={
                'login[email]':    email,
                'login[password]': password
            }
        )
        if r.status_code != requests.codes.ok:
            raise Exception('http request to login failed')

    def get(self, urlSuffix='', data={}):
        url = 'https://rpm.newrelic.com/' + urlSuffix
        r = self.s.get(url, data=data)
        if r.status_code != requests.codes.ok:
            raise Exception('http request failed. got status %s for url: %s' % (response.status, url))
        return r

    def get_servers_overview(self):
        r = self.get('accounts/%s/servers' % self.accountId)
        soup = BeautifulSoup(r.text)
        servertable = soup.find(id='hosts_dashboard_table')
        for row in servertable.findAll('tr'):
            if row.find('th'):
                row.find('th').extract()
            if row.find('td'):
                row.find('td').extract()
        servertable.find('h2', text='Servers').replaceWith('Servers')
        return servertable

    def get_errors(self, apps, hours):
        self.get('set_time_window?tw[dur]=last_%s_hours' % (hours))

        data = {}
        for name, id in apps.iteritems():
            data[name] = self._get_errors(id)
        return data.items()

    def _get_errors(self, app):
        r = self.get('accounts/%s/applications/%s/traced_errors' % (self.accountId, app))
        soup = BeautifulSoup(r.text)
        errortable = soup.find(id='errors')
        return errortable

    def get_apps_overview(self):
        r = self.get('accounts/%s/applications' % self.accountId)
        soup = BeautifulSoup(r.text)
        apptable = soup.find(id='apptable')
        # remove lights
        [light.extract() for light in apptable.findAll('td', {'class':'app_traffic_light'})]
        [actions.extract() for actions in apptable.findAll('td', {'class':'actions'})]
        # remove colspan=2 and header from <h2>Applications</h2>
        apptable.find('h2', text='Applications').parent['colspan'] = 1
        apptable.find('h2', text='Applications').replaceWith('Applications')
        return apptable