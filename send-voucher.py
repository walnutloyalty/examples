import requests
import json

print('Enter You bearer token')
token = input()

print('Enter the email that should receive the coupon')
email = input()

print('Enter the coupon_id of the coupon you want to send')
coupon_id = input()

print('Enter the brand id of the brand the coupon should be attached to')
brand_id = input()

print('when should the coupon expire')
expiration_date = input()

print('Added a status to the coupon, enum values[active, expired, blocked, demo, redeemed]')
status = input()


url = 'https://api.walnutloyalty.com/passes'
payload = {
    "email": email,
    "brand_id": brand_id,
    "coupon_id": coupon_id,
    "expiration_date": expiration_date,
    "status": status
}
headers = {
  'Authorization': 'Bearer ' + token,
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request('POST', url, headers=headers, json=payload)
print(response.json())