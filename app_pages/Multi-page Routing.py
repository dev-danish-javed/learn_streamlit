import streamlit as st
from utils import add_navigation, attach_custom_css, sidebar_expander

sidebar_expander("Multi-page Routing", """
- [Pages-based Routing](#pages-based-routing)
- [Dynamic Routing](#dynamic-routing)
""")

st.title("Multi-page Routing")
st.caption("Design user navigation for multiple pages")
st.write("""We have two options for multi-page routing:
- Pages based routing
- Dynamice routing

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
    - Home Page.py
    - pages/
        - page1.py
        - page2.py
```
The sidebar navigation will be generated automatically based on the directory structure.   
To manage the order of pages we attach numeric prefixes to the page filenames.  

&nbsp;   
Here is what this app's structure looks like when using programmatic routing:
```
- learn-stramlit
- Home Page.py
- app_pages/
    - Home Page.py
    - Headings.py
    - Text And Messaging.py
    ...
```
""")
st.divider()
st.header("Dynamic routing")

attach_custom_css()
add_navigation(previous_page="UX Helpers.py", previous_page_title="UX Helpers",
               next_page="Deployment.py", next_page_title="Deployment")

