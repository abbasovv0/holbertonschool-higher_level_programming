#!/usr/bin/python3
"""DOCUMENTED."""

import sys
import urllib.parse
import urllib.request


def main():
    url = sys.argv[1]
    email = sys.argv[2]

    # POST datasını hazırlamaq
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # POST request göndərmək
    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == "__main__":
    main()
