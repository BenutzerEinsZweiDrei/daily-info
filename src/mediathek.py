# curl mediathekwebview
# momentan nicht eingebunden

import requests

def get_ard(query):
	url= "https://mediathekviewweb.de/api/query"
	headers = {"Content-Type": "text/plain"}
	payload = {
    "queries": [ # multiple queries
      {
        "fields": ['title', 'topic'], # fields channel
        "query": query
      }
    ],
    "sortBy": 'timestamp',
    "sortOrder": 'desc',
    "future": False,
    "offset": 0,
    "size": 10,
    "duration_min": 20,
    "duration_max": 100
  }
	result = requests.post(url, headers=headers, json=payload)
	# 
	print(result.status_code)
	return result.json()

print(get_ard("Tagesschau")["result"]["results"][0]) #url website und title