import requests
import json

url = 'https://api.github.com'
user='MikeGer92'

git_req = requests.get(f'{url}/users/{user}/repos')

with open('data.json', 'w') as repo_list:
    json.dump(git_req.json(), repo_list)

    for i in git_req.json():
        print(i['name'])