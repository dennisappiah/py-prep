import json

import requests

url = "https://jsonplaceholder.typicode.com/comments"
query_strings = {"postId": 1}
headers = {"Authorization": "Bearer " + "xxxxx"}

response = requests.get(url=url, params=query_strings, headers=headers)
response_text = response.text

# converting to python object (list of dictionary object) - unMarshalling
comment_dictionary_list = json.loads(response_text)

for comment in comment_dictionary_list:
    print(str(comment["postId"]) + " " + comment["name"])

# POST Request
new_post = {
    "postId": 30,
    "it": 7,
    "name": "repels the consequences of present or lesser pleasures",
    "email": "Dallas@ole.me",
    "body": "blahblah",
}

# converting dict object into json
payload = json.dumps(new_post)

res = requests.post(url=url, data=payload, headers=headers)

if res.status_code == requests.codes.created:
    print(f"{res.status_code} - resource creation is successful")
    print(res.text)
