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
	text = text + "Talkshow  \n"
	text = text + "["+data[2]["title"]+"]("+data[2]["url"]+")  \n"
	text = text + "Reddit  \n"
	for item in data[3]:
		text = text + "["+item["title"]+"]("+item["url"]+")  \n"
	return text
	
	
	
	
st.title("Daily Information")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Get Data', on_click=click_button)

if st.session_state.clicked:
	load_state = st.text("Loading...")
	result = createdata()
	md = createmd(result)
	load_state.text("Loading...Done!")
	st.markdown(md)