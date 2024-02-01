# curl mediathekwebview

import requests

def get_ard(query):
	url= "https://mediathekviewweb.de/api/query"
	headers = {"Content-Type": "text/plain"}
	payload = {
    "queries": [ # multiple queries
      {
        "fields": ["topic"], # fields channel, title, topic
        "query": query
      }
    ],
    "sortBy": 'timestamp',
    "sortOrder": 'desc',
    "future": False,
    "offset": 0
    # "size": 10
    # "duration_min": 20,
    # "duration_max": 100
  }
	for item in query.split("#"):
		payload["queries"].append({ "fields": ["topic"], "query": item})
	result = requests.post(url, headers=headers, json=payload)
	# 
	print(result.status_code)
	# print(result.text)
	return result.json()

def get():
	result = get_ard("#miosga #hart,aber,fair #maischberger #phoenix,runde #unter,den,linden #presse,club #markus,lanz")["result"]["results"][0] #url website und title
	return { "title": result["title"], "url" : result["url_website"]} 