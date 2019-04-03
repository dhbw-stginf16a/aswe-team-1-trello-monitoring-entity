#!/usr/bin/env python3

import os

import pytest
import requests

from app import app


class TestConnexion:
    """The base test providing auth and flask clients to other tests
    """
    cache: dict = {}
    CENTRAL_NODE_BASE_URL = os.environ.setdefault('CENTRAL_NODE_BASE_URL', 'http://localhost:8080/api/v1')

    @pytest.fixture(scope='function')
    def client(self, requests_mock):
        preferences = {
            'trello_token': '12345',
            'trello_key': 'abc12345',
        }

        requests_mock.get(f'{self.CENTRAL_NODE_BASE_URL}/preferences/global', status_code=200, json=preferences)
        requests_mock.post(f'{self.CENTRAL_NODE_BASE_URL}/monitoring', text='', status_code=204)
        with app.app.test_client() as c:
            yield c
            app.registerThread.stop()
