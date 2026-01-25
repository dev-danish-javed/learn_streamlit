import streamlit as st

from utils import add_navigation, get_custom_css

st.set_page_config(page_title="Forms in Streamlit | Danish Javed", layout="wide", page_icon="👨🏻‍💻")

st.title("Forms in Streamlit")
st.caption("⚠️ Work in progress")

get_custom_css()
add_navigation(previous_page="04_Input Widgets.py", previous_page_title="Input Widgets")
