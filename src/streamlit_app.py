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
	text = "Tagesschau<br>"
	for item in data.ts:
		text = text + "["+item["hl"]+"]("+item["url"]+")<br>"
	text = text + "Podcast<br>"
	for item in data.ard:
		text = text + "["+item["title"]+"]("+item["url"]+")<br>"
	text = text + "Talkshow<br>"
	text = text + "["+data.mt["title"]+"]("+data.mt["url"]+")<br>"
	text = text + "Reddit<br>"
	for item in data.red:
		text = text + "["+item["title"]+"]("+item["url"]+")<br>"
	return text
	
	
	
	
st.title("Daily Information")

if st.button("Get Data"):
	load_state = st.text("Loading...")
	result = createdata()
	md = createmd(result)
	load_state.text("Loading...Done!")
	st.markdown(md)