import streamlit as st

from utils import set_page_config, add_navigation, attach_custom_css

set_page_config(page_title="Performance Helpers in Streamlit | Danish Javed")
st.title("Performance Helpers")
st.caption("Section under progress, please check back soon 🖖🏻")

attach_custom_css()
add_navigation(previous_page="pages/10_State & control flow.py", previous_page_title="State & Control Flow",
               next_page="pages/12_UX Helpers.py", next_page_title="UX Helpers")
