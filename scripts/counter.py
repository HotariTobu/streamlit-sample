import streamlit as st

from lib import StateFactory

state = StateFactory()

count, set_count = state(0)

if st.button(f"Count: {count}"):
    set_count(count + 1)
