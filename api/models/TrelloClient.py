#!/usr/bin/env python3

import logging

import requests
import dateutil.parser

logger = logging.getLogger(__name__)


class TrelloClient:
    """A Trello client wrapper taking care of authentication and stuff
    """

    def __init__(self, token, api_key, board):
        self.trello_token = token
        self.api_key = api_key
        self.board = board

    def getCards(self):
        resp = requests.get(f'https://api.trello.com/1/boards/{self.board}/cards?filter=visible&key={self.api_key}&token={self.trello_token}')
        assert resp.status_code == 200

        cards = resp.json()
        interestingCards = list()
        for card in cards:
            if card['due'] is not None and card['dueComplete'] is False:
                interestingCards.append(card)

        return interestingCards

    def getCardsDueUntil(self, timeLimit):
        cards = self.getCards()

        filteredCards = list()
        for card in cards:
            dueDate = card['due']

            if dateutil.parser.parse(dueDate).date() <= timeLimit.date():
                smallCard = {
                    'Task': card['name'],
                    'dueDate': card['due']
                }
                filteredCards.append(smallCard)

        return filteredCards
