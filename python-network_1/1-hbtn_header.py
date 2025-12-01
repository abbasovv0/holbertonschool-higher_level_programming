#!/usr/bin/python3
"""Fetches a URL and displays the X-Request-Id header value."""

import sys
import urllib.request


def main():
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get("X-Request-Id")
        if x_request_id:
            print(x_request_id)


if __name__ == "__main__":
    main()

