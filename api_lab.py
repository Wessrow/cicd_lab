#!/usr/bin/python3
"""
Labbing requests CI/CD issues
By Gustav Larsson
"""

import requests
import json

requests.urllib3.disable_warnings()

def main():

    base_url = "https://api.github.com/repositories?page=5&per_page=2"

    response = requests.get(base_url)

    return response

if __name__ == "__main__":
    print(json.dumps(main().json(), indent=2))