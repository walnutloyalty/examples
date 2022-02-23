import requests
import json

print('Enter your bearer token')
token = input()

print('Enter the pass code you want to remove')
pass_code = input()

print('Enter the email that belongs to the coupon')
email = input()

print('Enter the brand id of the brand Id of the coupon')
brand_id = input()


url = 'https://api.walnutloyalty.com/passes'
payload = {
    "email": email,
    "brand_id": brand_id,
    "pass_code": pass_code,
}
headers = {
  'Authorization': 'Bearer ' + token,
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request('DELETE', url, headers=headers, json=payload)
print(response.json())