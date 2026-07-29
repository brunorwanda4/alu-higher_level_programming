#!/bin/bash
# displays the body of the response, only for a 200 status code
response=$(curl -s -w "HTTPSTATUS:%{http_code}" "$1")
status=$(echo "$response" | tr -d '\n' | sed -e 's/.*HTTPSTATUS://')
body=$(echo "$response" | sed -e 's/HTTPSTATUS\:.*//')
if [ "$status" -eq 200 ]; then
    echo "$body"
fi
