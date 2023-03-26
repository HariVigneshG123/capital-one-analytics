import requests
import json

# customerId = 'your customerId here'
apiKey = 'ac21b41fd2a4c1cf2e3b8e1dace9ad57'

url = 'http://api.nessieisreal.com/merchants?key={}'.format(apiKey)
payload = {
  "name": "Cavalier Courts",
  "category": 
        "utility",
  "address": {
    "street_number": "72",
    "street_name": "Food Road",
    "city": "New York City",
    "state": "NY",
    "zip": "22000"
  },
  "geocode": {
    "lat": 42.44261090000001,
    "lng": -76.5086618
  }
}
# Create a Savings Account
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('merchant created')
else:
    print('merchant failed')