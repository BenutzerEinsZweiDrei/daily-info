import requests
import xml.etree.ElementTree as ET
from datetime import date, timedelta

def get_rss(endpoint):
	url= endpoint
	headers = {"Content-Type": "application/atom+xml", "User-Agent": "Mozilla/5.0"}
	payload = {}
	result = requests.get(url, headers=headers, json=payload)
	print(result.status_code)
	# print(result.text)
	return ET.fromstring(result.text)

def get_data(endpoint):
	
	yesterday = date.today() - timedelta(days=1)
	
	for child in get_rss(endpoint):
		if "entry" in child.tag:
			if (child[6] is not None) and (child[7] is not None):
				
				if "published" in child[6].tag:
					if str(date.today()) == child[6].text.split(":")[0].split("T")[0] or str(yesterday) == child[6].text.split(":")[0].split("T")[0]:
						return {"title": child[7].text, "url":child[4].attrib["href"]}
						
				elif "published" in child[7].tag:
						if str(date.today()) == child[7].text.split(":")[0].split("T")[0] or str(yesterday) == child[7].text.split(":")[0].split("T")[0]:
							return {"title": child[8].text, "url":child[5].attrib["href"]}
					
def check(endpoint):
	result = get_data(endpoint)
	if result:
		return result
	else:
		return {"title": "no", "url": "no"}

def table():
	tab = []
	tab.append(check("https://www.reddit.com/r/YouShouldKnow/.rss"))
	tab.append(check("https://www.reddit.com/r/todayilearned/.rss"))
	tab.append(check("https://www.reddit.com/r/LifeProTips/.rss"))
	return tab
	