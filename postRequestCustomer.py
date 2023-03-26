import requests
import json

# customerId = 'your customerId here'
apiKey = 'ac21b41fd2a4c1cf2e3b8e1dace9ad57'

url = 'http://api.nessieisreal.com/customers?key={}'.format(apiKey)
payload = {
  "first_name": "Achudan",
  "last_name": "T Sadhasivam",
  "address": {
    "street_number": "501",
    "street_name": "Thomas Jefferson Rd",
    "city": "Herndon",
    "state": "VA",
    "zip": "20171"
  }
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
    print('customer failed')