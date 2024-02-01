import streamlit as st

import tagesschau
import ardaudio
import mediathek
import parsereddit

def createdata():
	tab = []
	tab.append(tagesschau.headlines())
	tab.append(ardaudio.table())
	tab.append(mediathek.get())
	tab.append(parsereddit.table())
	return tab
	
st.title("Daily Information")

if st.button("Get Data"):
	load_state = st.text("Loading...")
	result = createdata()
	load_state.text("Loading...Done!")
	st.write(result)