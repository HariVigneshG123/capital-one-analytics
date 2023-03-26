import requests
import json

customerId = '641f4ce278f6910a15f0e07d'
apiKey = 'ac21b41fd2a4c1cf2e3b8e1dace9ad57'

url = 'http://api.nessieisreal.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
payload = {
  "type": "Credit Card",
  "nickname": "HVG CC",
  "rewards": 10000,
  "balance": 10000,	
}
# Create a Savings Account
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('account created')
else:
    print('account failed')