import streamlit as st
import pandas as pd

from utils import get_custom_css

# Page config, page_title -> tab title, page_icon -> favicon, layout -> wide=container fulid, center=container (bootstrap)
st.set_page_config(page_title='Streamlit Intro | Danish Javed', page_icon="👨🏻‍💻", layout='wide')

# h1 tag. Page title. Should be used only once
st.title("Streamlit Notes")
# Wrties muted text, great for providing containt
st.caption("A sample streamlit page to demo commonly used elements")
st.page_link(icon="🔗", page="https://www.devdanish.in", label="by Danish Javed", help="Learn more about the author")

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
    st.text(" Add \"streamlit\" in requirements.txt and run command below 👇🏻")
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


st.sidebar.title("Streamlit Introduction")
st.sidebar.markdown("""
- [Introduction](#introduction)
- [Installation](#installation) 
- [Page Setup](#page-setup)
""")
get_custom_css()

st.divider()

if st.button("Next : Headings \t->"):
    st.switch_page("pages/01_Headings.py")

