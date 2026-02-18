import streamlit as st
from utils import set_page_config, add_navigation, attach_custom_css

set_page_config(page_title="Multi-page Routing in Streamlit | Danish Javed")
st.sidebar.title("Multi-page Routing")

st.title("Multi-page Routing")
st.caption("Design user navigation for multiple pages")
st.write("""We have two options for multi-page routing:
- Pages based routing
- Dnynamice routing

Let's get over them one by one""")

st.divider()
st.header("Pages-based routing")
st.write("""
This is very straight forward. It works on a directory basis. We keep our home page in the root directory.
Thereafter we create a pages directory and keep all our pages inside it.
> **:material/emergency_home: Nested directories are not supported**

&nbsp;  
Here's an example:
```
- streamlit_app/
    - app.py
    - pages/
        - page1.py
        - page2.py
```
The sidebar navigation will be generated automatically based on the directory structure.   
To manage the order of pages we attach numeric prefixes to the page filenames.  

&nbsp;   
Here is what this apps structure looks like:
```
- learn-stramlit
- Introduction.py
- pages/
    - 01_Headings.py
    - 02_Text And Messaging.py
    ...
```
""")

attach_custom_css()