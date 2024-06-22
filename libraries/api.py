import requests
import json
import os
from requests import RequestException


def create_gist():
    url = "https://api.github.com/gists"
    headers = {
        "Accept": "application/json",
        "Authorization": f"token {os.getenv('TOKEN')}",
    }

    gist = {
        "files": {"main.go": {"content": "test"}},
        "description": "this is a test",
        "public": False,
    }

    gist_json = json.dumps(gist)

    try:
        response = requests.post(url, headers=headers, data=gist_json, timeout=1)
        response.raise_for_status()  # raise an exception for HTTP errors
    except RequestException as err:
        print(f"Error making request: {err}")
        return

    try:
        body = response.json()
    except Exception as err:
        print(f"Error reading response body: {err}")
        return

    print(f"Body: {json.dumps(body, indent=2)}")
    print(f"Response status: {response.status_code}")


def get_comments():
    url = "https://jsonplaceholder.typicode.com/comments"
    query_strings = {"postId": 1}
    headers = {
        "Authorization": f"bearer {os.getenv('TOKEN')}",
    }

    response = requests.get(url=url, params=query_strings, headers=headers)

    # converting to python object (list of dictionary object) - unMarshalling
    comment_dictionary_list = json.loads(response.text)

    for comment in comment_dictionary_list:
        print(str(comment["postId"]) + " " + comment["name"])


if __name__ == "__main__":
    create_gist()
    get_comments()
