import streamlit as st
from utils import add_navigation, attach_custom_css, sidebar_expander

sidebar_expander("Deployment", """
- [Overview](#deployment)
""")

st.title("Deployment")
st.caption("We can deploy our streamlit apps to streamlit community cloud")

st.write("""
This is pretty simple. 
- Signup with GitHub account at https://share.streamlit.io/
- On the top right corner you'll see "Create App"
- Choose deploy a "Deploy a public app from GitHub"
- Fill the simple form
- Choose a subdomain 
- Deploy and done.
""")

st.image("assets/deployment.png", caption="Deployment in Streamlit")
st.write("""
Congrats if you have made it this far. You're now able to develop and deploy your streamlit apps to the cloud.

###### Cheers to us 🥂. See you again in my next article. Untill then, happy coding.
""")
attach_custom_css()
add_navigation(previous_page="Multi-page Routing.py", previous_page_title="Multi-page Routing")

