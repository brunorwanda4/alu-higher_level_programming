#!/bin/bash
# sends a GET request with header X-HolbertonSchool-User-Id: 98, displays body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
