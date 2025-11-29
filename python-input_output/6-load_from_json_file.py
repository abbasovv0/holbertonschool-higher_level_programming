#!/usr/bin/python3
"""DOCUMENTED"""
import json


def load_from_json_file(filename):
    """DOCSTRING"""
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.load(json_file)
