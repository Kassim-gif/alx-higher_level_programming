#!/bin/bash
# Sends  tha JSON POST request to tha given URL with a given JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
