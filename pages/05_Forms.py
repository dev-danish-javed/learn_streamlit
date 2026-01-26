import time

import streamlit as st

from utils import add_navigation, get_custom_css

st.set_page_config(page_title="Forms in Streamlit | Danish Javed", layout="wide", page_icon="👨🏻‍💻")

st.sidebar.title("Forms")
st.sidebar.markdown("""
- [Sample Code](#sample-code)
- [Form Validation](#form-validation)
""")

st.title("Forms in Streamlit")

st.write("""Used when
 - Inputs need to be grouped together
 - Multiple feilds are related and are to be validated togeather
 - Submission is single event
 
 Ex: Apply filters/chanes or signup screens or any other form
 
 
 We have a few simple parameters.
 -  clear_on_submit : default false
 -  enter_to_submit : default true
 
 > **Forms should have a key and duplicate keys aren't allowed.**
 """)

st.divider()

st.header("Sample code")
st.caption("I have used non default options for demo")

st.code("""
with st.form(key="login_form", clear_on_submit=True, enter_to_submit=False):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

if not submitted:
    st.warning("Form not submitted yet")

if submitted:
    st.success("Form submitted")
    st.write("email: ", email, "password: ", password)

""")

with st.form(key="login_form", clear_on_submit=True, enter_to_submit=False):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

if not submitted:
    st.warning("Form not submitted yet")

if submitted:
    st.success("Form submitted")
    st.write("email: ", email, "password: ", password)

st.divider()

st.header("Form validation")
st.write("""
We can also perform form validation when the form is submitted.
""")

st.code("""

if "submitted" not in st.session_state:
    st.session_state.submitted = False

with st.form("login_form_validate"):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

if not submitted:
    st.warning("Form not submitted yet")

if submitted:
    with st.empty():
        st.info("Validating form inputs")
        time.sleep(1)
        if not email or not password:
            st.error("Email and password are required")
        elif "@" and "." not in email:
            st.error("Email is not valid")
        elif len(password) < 4:
            st.error("Password is too short")
        else :
            st.success("Form submitted successfully")
            time.sleep(3)
            st.write(f\"""
            - email : {email}
            - password : {password}
            \""")

""")

st.write("> **Renders this form below 👇🏻**")

if "submitted" not in st.session_state:
    st.session_state.submitted = False

with st.form("login_form_validate"):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

if not submitted:
    st.warning("Form not submitted yet")

if submitted:
    with st.empty():
        st.info("Validating form inputs")
        time.sleep(1)
        if not email or not password:
            st.error("Email and password are required")
        elif "@" and "." not in email:
            st.error("Email is not valid")
        elif len(password) < 4:
            st.error("Password is too short")
        else :
            st.success("Form submitted successfully")
            time.sleep(3)
            st.write(f"""
            - email : {email}
            - password : {password}
            """)



get_custom_css()
add_navigation(previous_page="04_Input Widgets.py",
               previous_page_title="Input Widgets",
               next_page="pages/06_Data Display.py",
               next_page_title="Data Display")
