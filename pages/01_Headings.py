import streamlit as st

from utils import get_custom_css, add_navigation

st.set_page_config(page_title='Headings in Streamlit | Danish Javed', page_icon="👨🏻‍💻", layout='wide')

st.title("Title and headings")
st.divider()
st.header("Page title")
st.caption("Typically used once per page")
st.text(
    "Consider this as the page intro. Like headline of news or the title of our article. Below is what I have used for this page")
st.code(body="""st.title("Title and headings")""", language="python")

st.divider()

st.header("Headings")
st.text("In streamlit we have 2 heading options as header and subheader. Its intentional to keep it simple.")

st.subheader("Headers")
st.markdown("""
- Translated to h2 tags
- Mark heading of the section""")
st.text("Like I have used for this section")
st.code('st.header("Headings")')

st.subheader("Subheaders")
st.markdown("""
    - Translated to h3 tags
    - Mark subheadings of the section""")
st.text("Like I have used for this")
st.code('st.subheader("Subheaders")')

st.divider()

st.header("Divider")
st.markdown("This is simple `<hr>`. Provides a horizontal ruling across the screen.")
st.code(body="st.divider()", language="python")

st.divider()

st.subheader("Captions")
st.text("These are best to provide context for something. For ex, adds timeframe below a matrics etc")
st.text("Like I have used right below the page title")
st.code(body='st.context("A sample streamlit page to demo commonly used elements")')

## We will discuss this in later sections
st.sidebar.title("Headings")
# st.sidebar.page_link("Headings#page-title", label="Page Title")
st.sidebar.markdown("""
- [Page Title](#page-title)
- [Headings](#headings)
    - [Headers](#headers) 
    - [Subheaders](#subheaders)
- [Divider](#divider)
- [Captions](#captions)
""")
get_custom_css()

add_navigation(previous_page="Introduction.py",
               previous_page_title="Introduction",
               next_page_title="Text and Messaging",
               next_page="02_Text And Messaging.py"
               )
