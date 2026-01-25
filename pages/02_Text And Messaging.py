import time

import streamlit as st
from utils import get_custom_css, add_navigation
import pandas as pd

st.set_page_config(page_title='Text and Messaging in Streamlit | Danish Javed', page_icon="👨🏻‍💻", layout='wide')


st.sidebar.title("Text and Messaging")
st.sidebar.markdown("""
- [Write](#write)
- [Markdown](#markdown) 
    - [_Hack_](#hack)
- [Code Block](#code-block)
- [Text](#text)
- [Callouts](#callouts)
- [Empty](#empty)
- [Dialogue](#dialogue)
""")

st.title("Texts and messaging")

st.divider()

st.subheader('Write')
st.text("Most commonly used, and most versetile. "
        "We can throw any type of data and it'll render it perfectly. "
        "It auto-detects the input type and renders accordingly while accepting n number of arguments.")
st.write("""
- String → text / markdown
- Number → text
- List / dict → pretty print
- DataFrame → table
- Matplotlib / Plotly fig → chart
- Multiple args → spaced output
""")
st.text("Code for this 👆🏻 is here 👇🏻")
st.code(body="""
    st.write(\"""
    - String → text / markdown
    - Number → text
    - List / dict → pretty print
    - DataFrame → table
    - Matplotlib / Plotly fig → chart
    - Multiple args → spaced output
    ""\")
    """)
with st.expander("_**Checkout examples**_"):
    st.text("Some examples")
    text_col, markdown_col, number_col = st.columns(3)
    with text_col:
        st.markdown("**Text Example**")
        st.code("""st.write("Hello Text")""")
        st.write("Hello Text")
        pass
    with markdown_col:
        st.markdown("**Markdown Example**")
        st.code("""st.write("_**Hello markdown**_")""")
        st.write("_**Hello markdown**_")
        pass
    with number_col:
        st.markdown("**Number Example**")
        st.code("""st.write(525, 324)""")
        st.write(525, 324)
        pass
    with st.container():
        st.markdown("**List/Dict Example**")
        st.code("""
        st.write(["Hello", "**World**", 123], {"name":"Sahiba Bali", "occpation":"Actor/Influencer"})
        """)
        st.write(["Hello", 123], {"name": "Sahiba Bali", "occpation": "Actor/Influencer"})
        pass

    with st.container():
        st.markdown("#### Dataframes Examples")
        st.caption("For now they would seem a little too advance, that is why I have placed them here.")
        st.text("These are actually the most real world use cases and what we'll actually be doing in production. ")
        table_df = pd.DataFrame({
            "User": ["Aman", "Riya", "Karan", "Neha", "Ishaan"],
            "Plan": ["Pro", "Free", "Enterprise", "Pro", "Free"],
            "Amount (₹)": [2400, 0, 12000, 2400, 0],
            "Status": ["Success", "Pending", "Success", "Success", "Failed"]
        })
        st.write(table_df)

st.divider()
st.subheader("Markdown")
st.text(
    "Streamlit also provides the option to use markdown. We can render any markdown in out UI and it would work fine.")
st.text("I have been using this through out the page. Bullet points are the simple examples.")
st.code(language="python", body="""
 st.markdown(\"""##### Subheaders  

        - Translated to h3 tags
        - Mark subheadings of the section""\")""")
st.caption("Not just these but we can use all the markdown tags")

st.markdown("##### ⚠️Hack")
st.caption("It's not recommended at all, as it breaks the UI consistency and defates the purpose of simplicity")
st.markdown(
    "We can also render html in streamlit, which we shouldn't unless its a must. we need to pass `unsafe_allow_html=True`. Here is an example")
st.code("""
st.markdown("We can also render html in streamlit, which we shouldn't unless its a must. Here is an example"
            "<span style=\"color:red\">This is html<span>", unsafe_allow_html=True)
""")
st.text("Renders 👇🏻")
st.markdown("<span style=\"color:red\">This is html<span>", unsafe_allow_html=True)

st.divider()

st.subheader("Code block")
st.markdown("This is `<code>` with streamlit styling and feature.")
st.markdown("We have three important and very useful parameters here.  ")
st.markdown("""
- body : the code
- width : the width of the block -> "content" | "streach"
- language : the language of the code
""")
st.text("The code in block below is rendered like this")
st.code(body="""st.code(body="st.code('<code>')", language="python", width="content")""",
        language="python", width="content")

st.divider()

st.subheader("Text")
st.write("""
Usually, used for logs and data that are raw. **It doesn't allow markdown**.
""")

st.code('st.text("Hello World!!")', language="python", width="content")
st.text("Hello World!!")

st.divider()

st.subheader("Callouts")
st.write("""
These are elements used to provide status or key findings, like toast messages or notes blocks. We have 4 options available here.

- info
- error
- warning
- exception
""")

info_col, error_col = st.columns(2)
with info_col:
    st.write("""
    ##### Info
    """)
    st.code("""st.info("Password has to be alpha numeric.", icon="ℹ️")""",
            language="python", width="content")
    st.info("Dashboard API is online now", icon="ℹ️")

with error_col:
    st.write("""
    ##### Error
    """)
    st.code("""st.error("API Key expired", icon="🚨")""", language="python", width="content")
    st.error("Invalid API key", icon="🚨")

st.divider()

warning_col, exception_col = st.columns(2)
with warning_col:
    st.write("""##### Warning""")
    st.code("""st.warning("Password is to expire in 3 days.", icon="⚠️")""", language="python", width="content")
    st.warning("Password is to expire in 3 days.", icon="⚠️")
with exception_col:
    st.write("""##### Exception""")
    st.code("""st.exception(RuntimeError("This is a dummy exception"))""", language="python", width="content")
    st.exception(RuntimeError("This is a dummy exception"))

st.divider()
st.header("Empty")
st.write("""As weird as it might sound, it is actually one of the coolest stuff. 
It allows only one line as output at once. Next line clears the previous one. Checkout the cool example below: """)

st.code("""
if st.button("Start timer 🕒"):
    with st.empty():
        for i in range(1, 11):
            st.write(f"{'⌛' if i%2==0 else '⏳'} {i} seconds completed")
            time.sleep(1)
        else:
            st.write("🕛 5 seconds completed")
""")

if st.button("Start timer 🕒"):
    with st.empty():
        for i in range(1, 6):
            st.write(f"{'⌛' if i%2==0 else '⏳'} {i} seconds completed")
            time.sleep(1)
        else:
            st.write("🕛 5 seconds completed")

st.divider()

st.header("Dialogue")
st.caption("Simple html modal")

st.write("""
Important parameters : 
- title : Modal title
- width : Modal width
- dismiss : If modal can be dismissed (use case of false would be to block user journey, like session time out)
- on_dismiss : Function to be called when modal is closed
""")

st.code("""
def dismiss_handler():
    st.write("Modal closed")

@st.dialog(title="Test Modal", width="medium", dismissible=True, on_dismiss=dismiss_handler)
def open_dialogue():
    st.divider()
    st.write("Yeah here is the modal")
""")

st.write("> **Renders this 👇🏻, click the button below to open the modal**")

def dismiss_handler():
    st.write("Modal closed")

@st.dialog(title="Test Modal", width="medium", dismissible=True, on_dismiss=dismiss_handler)
def open_dialogue():
    st.divider()
    st.write("Yeah here is the modal")


if st.button("Open dialogue"):
    open_dialogue()

get_custom_css()

add_navigation(previous_page="01_Headings.py",
               previous_page_title="Headings",
               next_page_title="Structure and Layout",
               next_page="03_Structure and Layout.py"
               )