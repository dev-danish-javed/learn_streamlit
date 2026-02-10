import streamlit as st

from utils import set_page_config, add_navigation, attach_custom_css

set_page_config(page_title="Upload and download in Streamlit | Danish Javed")

st.title("State and control flow")
st.caption("Now we are hitting the real stuff. Pay attention or else, we'll get 2am calls from the project manager")
st.write("""
We have three important concepts here.
- `st.session_state`
- `st.stop()`
- `st.rerun()`

Let's get over them one by one
""")
st.divider()

st.header("Session State")
st.header(f"{st.session_state.user_name if 'user_name' in st.session_state else 'Anonymous'}")
st.write("""
This is straightforward. 
- One dict
- Per user session
- Survives reruns, **not page refreshes**
- Explicit, not reactive
    - changes made do not reflecte in the UI automatically
    - we are responsible for that

Think server-side sessionStorage, that's it.
We have a map that we can use to store data, and it would remain across reruns for the entire user session.
But mind it, not shared across users. The map's scope is only for the current user session.
""")

st.divider()
st.write("##### Test secret section")
try:
    test_secret = st.secrets["TEST_SECRET"]
    st.write(f"Found the secret: {test_secret}")
except KeyError:
    st.write("> **Missing value bro**")

attach_custom_css()
add_navigation(previous_page="pages/09_Upload and Download.py", previous_page_title="Upload and Download")
