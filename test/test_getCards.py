import json
from datetime import datetime, timedelta

import pytest
import requests_mock
import requests

from .TestConnexion import TestConnexion
from .trello_sampleData import getDueDatedCards

@pytest.mark.usefixtures('client')
class TestRequest(TestConnexion):
    """A test to get events from the calendar api
    """
    nasaURL = 'http://www.nasa.gov/templateimages/redesign/calendar/iCal/nasa_calendar.ics'

    @pytest.fixture(scope='class')
    def trelloCards(self):
        """Due dated cards from a file
        """
        return getDueDatedCards()

    def test_getEventsDay(self, client, requests_mock, trelloCards):
        print(self.CENTRAL_NODE_BASE_URL)
        request = {
            'type': 'cards_due_day',
            'payload': {
                'user': 'AntonHynkel',
                'date': datetime.today().isoformat()
            }
        }

        preferences = {
            'trello_board': 'abc'
        }
        requests_mock.get(f'{self.CENTRAL_NODE_BASE_URL}/preferences/user/AntonHynkel', status_code=200, json=preferences)
        requests_mock.get(f'https://api.trello.com/1/boards/{preferences["trello_board"]}/cards', text=json.dumps(trelloCards))
        response = client.post('/api/v1/request', json=request)

        assert response.status_code == 200

    def test_getEventsTimerange(self, client, requests_mock, trelloCards):
        endDate = datetime.now() + timedelta(days=7)
        request = {
            'type': 'cards_due_until',
            'payload': {
                'user': 'AntonHynkel',
                'date': endDate.isoformat()
            }
        }

        preferences = {
            'trello_token': '12345',
            'trello_key': 'abc12345',
            'trello_board': 'abc'
        }
        requests_mock.get(f'{self.CENTRAL_NODE_BASE_URL}/preferences/user/AntonHynkel', status_code=200, json=preferences)
        requests_mock.get(f'https://api.trello.com/1/boards/{preferences["trello_board"]}/cards', text=json.dumps(trelloCards))
        response = client.post('/api/v1/request', json=request)

        assert response.status_code == 200
