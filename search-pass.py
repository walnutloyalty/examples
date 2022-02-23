import requests
import json

print('Enter your bearer token')
token = input()

print('Enter the pass code you want to search')
pass_code = input()

url = 'https://api.walnutloyalty.com/search/pass'
params = {
  'pass_code': pass_code,
}
headers = {
  'Authorization': 'Bearer ' + token,
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request('GET', url, headers=headers, params=params)
print(response.json())