 # use https://github.com/NicoWeio/blinkist

# import blinkist as library
import sys
sys.path.insert(1,"<path to blinkist python>")
import main

def f_sort(free):
			# title subtitle url
			return { "title" : free["title"], "subtitle" : free["subtitle"], "url" : free["url"] }
			
def free():
	result = main.get_f()
	return f_sort(result["book"])
