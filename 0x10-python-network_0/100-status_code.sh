#!/bin/bash
# Sends tha GET request to a given URL and display tha response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
