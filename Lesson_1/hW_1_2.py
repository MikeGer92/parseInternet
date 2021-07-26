import json

import requests

# ID: c4b945fc6d014437920376b820ea295a
# Пароль: 4f6f3f43e2cc42248779cc43bb59c537

url_token = 'https://oauth.yandex.com/client_id=c4b945fc6d014437920376b820ea295a'
url_auth = 'https://oauth.yandex.ru/authorize?response_type=token&client_id=c4b945fc6d014437920376b820ea295a'


url = 'https://cloud-api.yandex.net/v1/'
token = 'AQAAAAABHrRvAAdFlnYfES43uUDxozqo3SLQV1U'


headers = {
    'Content-Type': 'application/json', 'Authorization': token
}
disk_info = 'disk'
folder_info = 'disk/resources'
disk = requests.get(f'{url}{disk_info}')
disk.json()
disk = requests.get(f'{url}{disk_info}', headers = headers)
disk.json()
print(disk.json())

disk = requests.get(f'{url}{folder_info}?path=app:/', headers = headers)

for i in disk.json()['resource_id']:
    print(i)
with open('disk.json', 'w') as f:
    json.dump(disk.json(), f)