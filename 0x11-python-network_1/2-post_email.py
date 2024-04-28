#!/usr/bin/python3
"""A script that:
- takes in tha URL
- sends a POST request to tha passed URL
- takes email as tha parameter
- displays tha body of tha response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
