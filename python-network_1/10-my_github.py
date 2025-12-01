#!/usr/bin/python3
"""DOC."""

import sys
import requests


def main():
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        json_data = response.json()
        print(json_data.get("id"))
    else:
        print("Error: Invalid credentials")


if __name__ == "__main__":
    main()
