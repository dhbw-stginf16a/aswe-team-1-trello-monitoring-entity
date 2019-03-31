#!/usr/bin/env python3

import json

from random import randint
from datetime import datetime, timedelta

with open('test/trello_sample.json', 'r') as file:
    data = json.load(file)

def randomizeDueDate(card):
    card['due'] = datetime.now() + timedelta(days=randint(0,31))
    card['due'] = card['due'].isoformat()
    return card

def getDueDatedCards():
    return [randomizeDueDate(card) for card in data]
