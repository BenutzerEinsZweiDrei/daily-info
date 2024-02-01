# curl ard audiothek

import requests
import json
from datetime import date

def get_ids(thing):
	url= "https://api.ardaudiothek.de/graphql"
	headers = {"accept": "application/json", "Content-Type": "application/json", "Origin": "https://api.ardaudiothek.de", "DNT" : "1"}
	payload = """
	query { search(query: """+'"'+thing+'"'+""") {items  {nodes  {title, url, publishDate}}}}"""
	result = requests.post(url, headers=headers, json={"query":  payload})
	print(result.status_code)
	return result.json()

def get_item(endpoint):
	url = endpoint
	headers = {"accept": "application/json", "Content-Type": "application/json", "Origin": "https://api.ardaudiothek.de", "DNT" : "1"}
	payload = {}
	result = requests.get(url, headers=headers, json=payload)
	print(result.status_code)
	return result.json()["data"]["item"]
	
	
def search(qu):
	for item in get_ids(qu)["data"]["search"]["items"]["nodes"]:
		if str(date.today()) == item["publishDate"].split(":")[0].split("T")[0]:
			se_result = get_item(item["url"])
			# title, sharingUrl
			return {"title": se_result["title"], "url": se_result["sharingUrl"]}
		# print(date.today())
		# if we didnt get result
	return {"title": "no","url":"no"}

def table():
	tab = []
	tab.append(search("Ende der Welt Glosse"))
	tab.append(search("Quarks Daily Wissenspodcast"))
	return tab
	# Quarks kommt um 15 Uhr