#!/usr/bin/python3
import sys
import urllib.request

url = sys.argv[https://intranet.hbtn.io]

with urllib.request.urlopen(url) as response:
    print(response.headers.get("X-Request-Id"))
