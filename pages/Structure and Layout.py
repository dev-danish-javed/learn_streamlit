import streamlit as st

from utils import get_custom_css

st.set_page_config(page_title='Structure and Layout in Streamlit', page_icon="👨🏻‍💻", layout='wide')
st.header("""Structure the layout""")
st.caption("Allows to provide structure our pages")

st.divider()

st.subheader("Columns")
st.text("Same as html tables but with slightly different syntax. "
        "There is no row explicitly. "
        "We create n number of columns that are all a part of one row. "
        "When we need new row, we create new set of columns, which by default will be rendered in a new row.")

st.code(body="""
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### Column 1")
    st.text("Blah blah "* 15)
with col2:
    st.markdown("#### Column 2")
    st.text("Blah blah "* 15)
with col3:
    st.markdown("#### Column 3")
    st.text("Blah blah "* 15)
""", language="python")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### Column 1")
    st.text("Blah blah " * 15)
with col2:
    st.markdown("#### Column 2")
    st.text("Blah blah " * 15)
with col3:
    st.markdown("#### Column 3")
    st.text("Blah blah " * 15)

st.markdown("""
#### Custom Column Width
""")
st.text("By default, the columns generated used equal width. But we do get the option to make them use custom width. "
        "Same columns as above used with different width.")
st.text("Instead of pssing the count of columns we want, we pass an array with ratio units of the widths we want. "
        "The count of the array size decides the number of columns ")
st.code("col1, col2, col3 = st.columns([4,2,1])", language="python")
col1, col2, col3 = st.columns([4, 2, 1])
with col1:
    st.markdown("#### Column 1")
    st.text("Blah blah " * 15)
with col2:
    st.markdown("#### Column 2")
    st.text("Blah blah " * 15)
with col3:
    st.markdown("#### Column 3")
    st.text("Blah blah " * 15)

st.divider()

st.subheader("Container")
st.text("""
This is a logic group of ui elements. Conceptually, they are similar to what components are in react.
They don't add anything on the UI level other than structural grouping, nothing visible to the user.
""")
st.code(body="""
with st.container():
    st.text("This is inside a container")

""", language="python")
st.text("Rendered as 👇🏻, notice that nothing fancy is happening here")
with st.container():
    st.text("This is inside a container")

st.text("The prime benifit is when paried with functions, they act as resulable blocks, conceptually, a component")

st.code(body="""
def greet_person(name:str):
    with st.container():
        prefix = "" if name.startswith("Mr") else "Mr. "
        st.markdown(f"Hello _**{prefix}{name}**_")

greet_person("Elon")
greet_person("Mr Trump")
""")
st.text('Renders 👇🏻')


def greet_person(name: str):
    with st.container():
        prefix = "" if name.startswith("Mr") else "Mr. "
        st.markdown(f"Hello _**{prefix}{name}**_")


greet_person("Elon")
greet_person("Mr Trump")

st.divider()

st.subheader("Expanders")
st.markdown("""
Just like we have `details` tag html, we have expanders in streamlit. The `summary` part goes as string parameter. 
""")
st.code(body="""
with st.expander("Summary"):
    st.text("This is expander content")
    st.text("Blah blah " * 150)
""", language="python")

st.text("Renders this 👇🏻")

with st.expander("Summary"):
    st.text("This is expander content")
    st.text("Blah blah " * 150)

st.divider()

st.subheader("Sidebars")
st.text(
    "Consider these are the side panel that we often see in the documentation "
    "or the filters section that we get in ecom websites. "
)
st.markdown("""
These have the same set of options that we have in streamlit, just that we have to do `st.sidebar.<anything else>`.
""")

st.caption(
    "I have kept the code down here, for article purpose, but its better to keep it on early part of the page for readability")
st.text("Checkout the upper left corner of this page. Click the icon and that's where the content is rendered.")

st.code("""
st.sidebar.title("Structure the layout")
st.sidebar.markdown(""\"
- [Columns](#columns)
    - [Custom column width](#custom-column-width)
- [Container](#container) 
    - [Subheaders](#subheaders)
- [Divider](#divider)
- [Expanders](#expanders)
- [Sidebars](#sidebars)
""\")
""")

st.sidebar.title("Structure the layout")
st.sidebar.markdown("""
- [Columns](#columns)
    - [Custom column width](#custom-column-width)
- [Container](#container) 
    - [Subheaders](#subheaders)
- [Divider](#divider)
- [Expanders](#expanders)
- [Sidebars](#sidebars)
""")
get_custom_css()

st.divider()

previous_col, next_col = st.columns(2)

with previous_col:
    if st.button("<- Previous : Headings"):
        st.switch_page("pages/Headings.py")

with next_col:
    if st.button("Next : Text And Messaging ->"):
        st.switch_page("pages/Text And Messaging.py")