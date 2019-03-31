#!/usr/bin/env python3

import logging

from datetime import datetime

import dateutil.parser

from api.models.prefstore import getTrelloData
from api.models.TrelloClient import TrelloClient

logger = logging.getLogger(__name__)


def getCards(body):
    token, key, board = getTrelloData(body['payload']['user'])
    client = TrelloClient(token, key, board)
    if body['type'] == 'cards_due_day':
        day = dateutil.parser.parse(body['payload']['date'])
        cards = client.getCardsDueUntil(day)
    elif body['type'] == 'cards_due_until':
        until = dateutil.parser.parse(body['payload']['date'])
        cards = client.getCardsDueUntil(until)

    response = {
        'type': body['type'],
        'payload': {
            'cards': cards
        }
    }

    return [response], 200
