import requests
import xml.etree.ElementTree as ET
from datetime import date

def get_rss(endpoint):
	url= endpoint
	headers = {"Content-Type": "application/atom+xml", "User-Agent": "Mozilla/5.0"}
	payload = {}
	result = requests.get(url, headers=headers, json=payload)
	print(result.status_code)
	# print(result.text)
	return ET.fromstring(result.text)

def get_data(endpoint):
	for child in get_rss(endpoint):
		if "entry" in child.tag:
			# 8, 5, publish:7
			# print(str(date.today()))
			if "published" in child[6].tag:
				if "2024-01-30" == child[6].text.split(":")[0].split("T")[0]:
					
					return {"title": child[7].text, "url":child[4].attrib["href"]}
			else:
				if "2024-01-30" == child[7].text.split(":")[0].split("T")[0]:
					
					return {"title": child[8].text, "url":child[5].attrib["href"]}

def table():
	tab = []
	tab.append(get_data("https://www.reddit.com/r/YouShouldKnow/.rss"))
	tab.append(get_data("https://www.reddit.com/r/todayilearned/.rss"))
	tab.append(get_data("https://www.reddit.com/r/LifeProTips/.rss"))
	return tab

