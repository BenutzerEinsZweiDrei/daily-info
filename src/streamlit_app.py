import streamlit as st

import tagesschau
import ardaudio
import mediathek
import parsereddit

def createdata():
	ts = tagesschau.headlines()
	ard = ardaudio.table()
	mt = mediathek.get()
	red = parsereddit.table()
	return [ts,ard,mt,red]

def createmd(data):
	text = "Tagesschau  \n"
	for item in data[0]:
		text = text + "["+item["hl"]+"]("+item["url"]+")  \n"
	text = text + "Podcast<br>"
	for item in data[1]:
		text = text + "["+item["title"]+"]("+item["url"]+")  \n"
	text = text + "Talkshow<br>"
	text = text + "["+data[2]["title"]+"]("+data[2]["url"]+")  \n"
	text = text + "Reddit  \n"
	for item in data[3]:
		text = text + "["+item["title"]+"]("+item["url"]+")  \n"
	return text
	
	
	
	
st.title("Daily Information")

if st.button("Get Data"):
	load_state = st.text("Loading...")
	result = createdata()
	md = createmd(result)
	load_state.text("Loading...Done!")
	st.markdown(md)