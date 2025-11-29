#!/usr/bin/python3
"""DOCUMENTED"""
import json


def save_to_json_file(my_obj, filename):
    """DOCSTRING"""
    with open(filename, "w", encoding="utf-8") as json_file:
        return json.dump(my_obj, json_file)
