import requests
import json

print('Enter your bearer token')
token = input()

print('Enter the pass code you want to update')
pass_code = input()

print('Enter the email this pass is connected to')
email = input()

print('Enter the brand the pass belongs to')
brand_id = input()

print('Enter the date this pass should expire, enter `no-date` if shouldnt expire')
expiration_date = input()


print('Enter the status of the pass, enum values[active, expired, blocked, demo, redeemed]')
status = input()

url = 'https://api.walnutloyalty.com/passes'
payload = {
    "email": email,
    "brand_id": brand_id,
    "pass_code": pass_code,
    "expiration_date": expiration_date,
    "status": status
}
headers = {
  'Authorization': 'Bearer ' + token,
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request('PUT', url, headers=headers, json=payload)
print(response.json())