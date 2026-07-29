#!/bin/bash
# displays the size in bytes of the body of the response
curl -s -o /dev/null -w "%{size_download}\n" "$1"
