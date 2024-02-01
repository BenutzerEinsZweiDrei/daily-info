# use https://github.com/NicoWeio/blinkist

# import blinkist as library
from blinkist.blinkist import (get_free_daily, get_latest_books,
                               get_latest_collections, get_trending_books,
                               search_books)

def get_f():
	return get_free_daily("de")

def f_sort(free):
			# title subtitle url
			return { "title" : free["title"], "subtitle" : free["subtitle"], "url" : free["url"] }
			
def free():
	result = get_f()
	return f_sort(result["book"])
