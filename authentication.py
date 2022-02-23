import requests
import json

print('Enter your dashboard email address')
email = input()

print ('Enter dashboard password')
password = input()
url = 'https://api.walnutloyalty.com/oauth/token'

payload = {
    "email": email,
    "password": password,
    "permissions": [
        "device.get", "device.store", "location.get", "passes.get", "passes.remove", "passes.update", "passes.store", "location.store", "search.pass", "product.get", "product.store", "brand.get", "brand.import", "scan.url"
    ]
}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request('POST', url, headers=headers, json=payload)
print(response.json())