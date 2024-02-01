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
	return {ts,ard,mt,red}
	
st.title("Daily Information")

if st.button("Get Data"):
	load_state = st.text("Loading...")
	result = createdata()
	load_state.text("Loading...Done!")
	st.write(result)