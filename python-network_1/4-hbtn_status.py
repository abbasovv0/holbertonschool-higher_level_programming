#!/usr/bin/python3
"""DOCUMENTED."""

import requests

url = 'https://intranet.hbtn.io/status'
response = requests.get(url)

print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")
