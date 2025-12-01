#!/usr/bin/python3
"""DOC."""

import sys
import requests


def main():
    url = sys.argv[1]   # Terminaldan URL alınır
    email = sys.argv[2]  # Terminaldan email alınır

    # POST datası
    data = {'email': email}

    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    main()
