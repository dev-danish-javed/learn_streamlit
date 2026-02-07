import streamlit as st

from utils import build_navigation_pages

navigation = st.navigation(build_navigation_pages())
navigation.run()
