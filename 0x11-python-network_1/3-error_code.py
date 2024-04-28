#!/usr/bin/python3
"""A script that:
- takes in tha URL,
- sends a request to tha URL
- displays tha body of tha response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
