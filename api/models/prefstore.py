#!/usr/bin/env python3

import logging
import os

import requests

logger = logging.getLogger(__name__)


CENTRAL_NODE_BASE_URL = os.environ.setdefault('CENTRAL_NODE_BASE_URL', 'http://localhost:8080/api/v1')

class PrefStoreClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_user_prefs(self, user):
        r = requests.get("{}/preferences/user/{}".format(self.base_url, user), timeout=10)
        assert r.status_code == 200
        return r.json()

    def get_global_prefs(self):
        r = requests.get("{}/preferences/global".format(self.base_url), timeout=10)
        assert r.status_code == 200
        return r.json()

PREFSTORE_CLIENT = PrefStoreClient(CENTRAL_NODE_BASE_URL)


def getTrelloData(userName):
    userPrefs = PREFSTORE_CLIENT.get_user_prefs(userName)
    globalPrefs = PREFSTORE_CLIENT.get_global_prefs()

    return globalPrefs['trello_token'], globalPrefs['trello_key'], userPrefs['trello_board']
