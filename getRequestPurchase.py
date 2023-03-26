import requests
import json

customerId = '641f5f1978f6910a15f0e098'
apiKey = 'ac21b41fd2a4c1cf2e3b8e1dace9ad57'

url = 'http://api.nessieisreal.com/accounts/{}/purchases?key={}'.format(customerId,apiKey)

# Create a Savings Account
response = requests.get(url)
response_json = response.json()

merchant_list =[{"merchant-name":"Walmart","merchant-id":"641f612878f6910a15f0e0a5","merchant-category":"grocery"},
                {"merchant-name":"UPS","merchant-id":"641f612878f6910a15f0e0a4","merchant-category":"other"},
                {"merchant-name":"Dunkin Donuts","merchant-id":"641f630678f6910a15f0e0a6","merchant-category":"food/restaurants"},
                {"merchant-name":"Chik-Fil-A","merchant-id":"641f612878f6910a15f0e0a3","merchant-category":"food/restaurants"},
                {"merchant-name":"Chipotle","merchant-id":"641f612878f6910a15f0e0a0","merchant-category":"food/restaurants"},
                {"merchant-name":"Capital-One","merchant-id":"641f612878f6910a15f0e09f","merchant-category":"finance"},
                {"merchant-name":"Apple","merchant-id":"641f612878f6910a15f0e09e","merchant-category":"other"},
                {"merchant-name":"Geico","merchant-id":"641f612878f6910a15f0e09c","merchant-category":"healthcare"},
                {"merchant-name":"McDonalds","merchant-id":"641f612878f6910a15f0e09a","merchant-category":"food/restaurants"},
                {"merchant-name":"Target","merchant-id":"5c37f22bb8e2a665da3eb28d","merchant-category":"grocery"},
                {"merchant-name":"Bed Bath & Beyond","merchant-id":"5c37f228b8e2a665da3eb221","merchant-category":"lifestyle"},
                {"merchant-name":"Adidas","merchant-id":"5c37f225b8e2a665da3eb1b7","merchant-category":"lifestyle"},
                {"merchant-name":"Nike","merchant-id":"5c37f223b8e2a665da3eb15b","merchant-category":"lifestyle"},
                {"merchant-name":"Clys","merchant-id":"5c37f20eb8e2a665da3eaea2","merchant-category":"other"},
                {"merchant-name":"Cavalier Courts","merchant-id":"641f93a578f6910a15f0e3c2","merchant-category":"utilities"},
                {"merchant-name":"Loudoun Water","merchant-id":"641f938578f6910a15f0e3c1","merchant-category":"utilities"},
                {"merchant-name":"American Electric","merchant-id":"641f936b78f6910a15f0e3c0","merchant-category":"utilities"}
                ]


for r in response_json:
      if r['description'] == "string":
            for merchant in merchant_list:
                  if merchant['merchant-id'] == r['merchant_id']:
                        r['description']=merchant['merchant-name']

for r in response_json:
      for merchant in merchant_list:
            if r['merchant_id'] == merchant['merchant-id']:
                  r['category'] = merchant['merchant-category']
                  break

json_object = json.dumps(response_json, indent=4)
with open("/Users/harivigneshgomathi/Documents/HooHacks/response_get.json", "w") as outfile:
    outfile.write(json_object)

