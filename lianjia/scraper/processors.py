# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from builtins import str
import re


def decode(info):
    return info.decode('utf-8')


# address | numOfRooms | size
def get_address(text):
    if not isinstance(text, str):
        text = str(text)
    return text.split()[1]


def get_size(text):
    if not isinstance(text, str):
        text = str(text)
    pattern = r'[1-9]\d*'
    return re.findall(pattern, text.split()[2])[0]


def get_n_livingroom(text):
    if not isinstance(text, str):
        text = str(text)
    pattern = r'[0-9]\d*'
    return re.findall(pattern, text.split()[1])[1]


def get_n_bedroom(text):
    if not isinstance(text, str):
        text = str(text)
    pattern = r'[0-9]\d*'
    return re.findall(pattern, text.split()[1])[0]



