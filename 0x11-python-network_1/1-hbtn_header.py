#!/usr/bin/python3
"""A script that:
- takes in tha URL,
- sends tha request to tha URL and displays tha value
- of tha X-Request-Id variable found in tha header of tha response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
