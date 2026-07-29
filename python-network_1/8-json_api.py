#!/usr/bin/python3
"""Searches users via the search_user API and displays [id] name"""
import requests
import sys

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": letter})
    try:
        result = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not result:
            print("No result")
        else:
            for item in result:
                print("[{}] {}".format(item.get("id"), item.get("name")))
