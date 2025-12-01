#!/usr/bin/python3
"""DOCUMENTED."""

import sys
import requests


def main():
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")
    if x_request_id:
        print(x_request_id)


if __name__ == "__main__":
    main()
