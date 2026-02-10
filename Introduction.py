import logging

import streamlit as st

from email_util import send_mail, send_welcome_mail
from utils import attach_custom_css, add_navigation, set_page_config

# Page config, page_title -> tab title, page_icon -> favicon, layout -> wide=container fulid, center=container (bootstrap)
set_page_config(page_title='Streamlit Intro | Danish Javed')

st.sidebar.title("Streamlit Introduction")
st.sidebar.markdown("""
- [Introduction](#introduction)
- [Installation](#installation) 
- [Page Setup](#page-setup)
""")

# ignore st.session_state for now, we'll discuss it in dedicated section
if "user_name" in st.session_state:
    st.title(f"Welcome {st.session_state.user_name} !! Let's get started")
else:
    # h1 tag. Page title. Should be used only once
    st.title("Streamlit Notes")
# Wrties muted text, great for providing containt
st.caption("A sample streamlit page to demo commonly used elements")
st.page_link(icon=":material/link:", page="https://www.devdanish.in", label="Danish Javed", help="Learn more about the author")

# hr tag
st.divider()

# Consider it as section heading
st.header("Introduction")
st.write("""
    Streamlit is UI tool native to python. The prime purpose for this is to act as data presentation layer.  
    The prime benfit
    - seamless integration in python codebase
    - no seperate front end backend request management
    - super fast and easy UI development 
    """)

st.divider()

st.header("Getting started")
st.text("Here I'm writing the details of my learnings. I'll be using streamlit to note down my streamlit notes 😂🔥")

st.divider()

st.subheader("Installation")
st.text("Let's get started with installation first.")
col1, col2 = st.columns(2)
with col1:
    st.text(" Add \"streamlit\" in requirements.txt and run command below :material/keyboard_double_arrow_down:")
    st.code("pip install -r requirements.txt")
with col2:
    st.write("Or simply do ")
    st.code("pip install streamlit")

st.divider()

st.subheader("Page Setup")
st.text("""Like we have head in html, this our place to setup our page.""")
st.code(body="""import streamlit as st
st.set_page_config(page_title='Danish Javed',page_icon="👨🏻‍💻", layout='wide')""", language="python")
st.markdown("""
 Some simple optoins that we have 
 - page_title -> tab title
 - page_icon -> favicon
 - layout _(bootstrap analogy)_
    - wide = container fulid
    - center = container
""")

@st.dialog(title="Welcome, Reader", width="medium", dismissible=True)
def collect_user_name():
    with st.form(key="user_form", enter_to_submit=False):
        user_name = st.text_input(label= "Your name", placeholder="Enter name for custom experience")
        user_email = st.text_input(label="Email", placeholder="Please provide your email, won't spam 🤞🏻")
        st.form_submit_button("Enter")
    if user_email:
        st.session_state.user_email = user_email
        pass
    if user_name:
        st.session_state.user_name = user_name
        st.rerun()


if "user_name" not in st.session_state:
    collect_user_name()
else:
    if "user_reported" not in st.session_state:
        try:
            send_mail(to=st.secrets["SMTP_USER_NAME"], subject=f"Add {st.session_state.user_name} on LinkedIn",
                  body=f"Hi, {st.session_state.user_name} viewed you streamlit notes, consider adding them on LinkedIn")
            st.session_state.user_reported = True
        except Exception as e:
            pass
if "user_email" in st.session_state:
    if "user_greeted" not in st.session_state:
        try:
            send_welcome_mail(user_email=st.session_state.user_email)
            st.session_state.user_greeted = True
        except Exception as e:
            pass

attach_custom_css()

add_navigation(next_page="01_Headings.py", next_page_title="Headings")
