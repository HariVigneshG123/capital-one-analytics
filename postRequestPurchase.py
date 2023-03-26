import random
import requests
import json
import time

def str_time_prop(start, end, time_format, prop):

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)

merchant_list =[{"merchant-name":"Walmart","merchant-id":"641f612878f6910a15f0e0a5"},
                {"merchant-name":"UPS","merchant-id":"641f612878f6910a15f0e0a4"},
                {"merchant-name":"Dunkin Donuts","merchant-id":"641f630678f6910a15f0e0a6"},
                {"merchant-name":"Chik-Fil-A","merchant-id":"641f612878f6910a15f0e0a3"},
                {"merchant-name":"Chipotle","merchant-id":"641f612878f6910a15f0e0a0"},
                {"merchant-name":"Capital-One","merchant-id":"641f612878f6910a15f0e09f"},
                {"merchant-name":"Apple","merchant-id":"641f612878f6910a15f0e09e"},
                {"merchant-name":"Geico","merchant-id":"641f612878f6910a15f0e09c"},
                {"merchant-name":"McDonalds","merchant-id":"641f612878f6910a15f0e09a"},
                {"merchant-name":"Target","merchant-id":"5c37f22bb8e2a665da3eb28d"},
                {"merchant-name":"Bed Bath & Beyond","merchant-id":"5c37f228b8e2a665da3eb221"},
                {"merchant-name":"Adidas","merchant-id":"5c37f225b8e2a665da3eb1b7"},
                {"merchant-name":"Nike","merchant-id":"5c37f223b8e2a665da3eb15b"},
                {"merchant-name":"Clys","merchant-id":"5c37f20eb8e2a665da3eaea2"},
                {"merchant-name":"Cavalier Courts","merchant-id":"641f93a578f6910a15f0e3c2"},
                {"merchant-name":"Loudoun Water","merchant-id":"641f938578f6910a15f0e3c1"},
                {"merchant-name":"American Electric","merchant-id":"641f936b78f6910a15f0e3c0"}
                ]

apiKey = 'ac21b41fd2a4c1cf2e3b8e1dace9ad57'
account_id = '641f5f1978f6910a15f0e098'
url = 'http://api.nessieisreal.com/accounts/{}/purchases?key={}'.format(account_id,apiKey)

for i in range(20):
    val = random.choice(merchant_list)
    payload = {
        "merchant_id": val['merchant-id'],
        "medium": "balance",
        "purchase_date": random_date("2022-11-01", "2023-03-01", random.random()),
        "amount": random.randint(1,500),
        "status": "pending",
        "description": val['merchant-name']
    }
    payload_json = json.dumps(payload)
    response = requests.post( 
        url, 
        data=payload_json,
        headers={'content-type':'application/json'},
	)
    print(payload_json)
    if response.status_code == 201:
        print('Purchase created')
    else:
        print('Purchase failed')