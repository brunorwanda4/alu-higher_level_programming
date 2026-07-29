#!/bin/bash
# sends a POST request with email and subject params, displays body
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
