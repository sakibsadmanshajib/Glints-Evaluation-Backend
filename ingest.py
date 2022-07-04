import json
import urllib.request
import requests

BACKEND_URL = 'http://localhost:8000/api/v1/'

def data_upload(URI, dict_data):
    headers = {'Content-type': 'application/json'}
    return requests.post(URI, json=dict_data, headers=headers)

def data_download(URI):
    with urllib.request.urlopen(URI) as url:
        return json.loads(url.read().decode())

print('Downloading restaurant data...')         
res = data_upload(f'{BACKEND_URL}add-restaurants/', data_download("https://gist.githubusercontent.com/seahyc/b9ebbe264f8633a1bf167cc6a90d4b57/raw/021d2e0d2c56217bad524119d1c31419b2938505/restaurant_with_menu.json"))
if res.status_code == 200:
    print('Restaurant data added successfully')
else:
    print(f'{res.status_code} Restaurant data addition failed')

print('Downloading customer data...')
res = data_upload(f'{BACKEND_URL}add-customers/', data_download("https://gist.githubusercontent.com/seahyc/de33162db680c3d595e955752178d57d/raw/785007bc91c543f847b87d705499e86e16961379/users_with_purchase_history.json"))
if res.status_code == 200:
    print('Customer data added successfully')
else:
    print(f'{res.status_code} Customer data addition failed')