#!/usr/bin/python3
"""DOCUMENTED."""

import requests
response = requests.get('https://intranet.hbtn.io/status')

print(f"Body response:")
print(f"\t - type: {type(response.text)}")
print(f"\t - content:{response.text}")
