import streamlit as st

from utils import set_page_config

set_page_config(page_title="Streamlit Notes | Danish Javed")

pages = [
    st.Page("app_pages/Home Page.py", title="Introduction", icon=":material/home:"),
    st.Page("app_pages/Headings.py", title="Headings", icon=":material/title:"),
    st.Page("app_pages/Text And Messaging.py", title="Text & Messaging", icon=":material/chat:"),
    st.Page("app_pages/Structure and Layout.py", title="Structure & Layout", icon=":material/view_quilt:"),
    st.Page("app_pages/Input Widgets.py", title="Input Widgets", icon=":material/tune:"),
    st.Page("app_pages/Forms.py", title="Forms", icon=":material/edit_note:"),
    st.Page("app_pages/Data Display.py", title="Data Display", icon=":material/table_chart:"),
    st.Page("app_pages/Charts.py", title="Charts", icon=":material/show_chart:"),
    st.Page("app_pages/Media.py", title="Media", icon=":material/image:"),
    st.Page("app_pages/Upload and Download.py", title="Upload & Download", icon=":material/cloud_upload:"),
    st.Page("app_pages/State & control flow.py", title="State & Control Flow", icon=":material/bolt:"),
    st.Page("app_pages/Performace Helpers.py", title="Performance Helpers", icon=":material/speed:"),
    st.Page("app_pages/UX Helpers.py", title="UX Helpers", icon=":material/emoji_objects:"),
    st.Page("app_pages/Multi-page Routing.py", title="Multi-page Routing", icon=":material/route:"),
    st.Page("app_pages/Deployment.py", title="Deployment", icon=":material/rocket_launch:"),
]

navigation = st.navigation(pages)
navigation.run()

