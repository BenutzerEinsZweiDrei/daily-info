# curl https://www.tagesschau.de/api2/news/

import requests

def get_ts():
	url= "https://www.tagesschau.de/api2/homepage/"
	headers = {"accept": "application/json"}
	payload = {}
	result = requests.get(url, headers=headers, json=payload)
	# print(result.status_code)
	return result.json()
	
def create_table(ts):
	table = []
	for item in ts["news"]:
		if "title" and "shareURL" in item:
			if not list(item["title"])[0] == '"':
				table.append({ "url" : item["shareURL"], "hl" : item["title"]})
	return table
			
def headlines():
	ts = get_ts()
	return create_table(ts)
