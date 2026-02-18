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
&nbsp;  
> ##### **Checkout sample code [here](https://github.com/dev-danish-javed/learn_streamlit/tree/page_based_routing)**
""")
st.divider()
st.header("Dynamic routing")
st.write("""
In this approach we use pages object and pass it to the navigation component.

&nbsp;  
Checkout the code below:
""")
st.code("""
pages = [
    st.Page("app_pages/Home Page.py", title="Introduction", icon=":material/home:"),
    st.Page("app_pages/Headings.py", title="Headings", icon=":material/title:"),
    st.Page("app_pages/Text And Messaging.py", title="Text & Messaging", icon=":material/chat:"),
    st.Page("app_pages/Structure and Layout.py", title="Structure & Layout", icon=":material/view_quilt:"),
    st.Page("app_pages/Input Widgets.py", title="Input Widgets", icon=":material/tune:"),
    st.Page("app_pages/Forms.py", title="Forms", icon=":material/edit_note:"),
    st.Page("app_pages/Data Display.py", title="Data Display", icon=":material/table_chart:"),
    st.Page("app_pages/Charts.py", title="Charts", icon=":material/show_chart:"),
    st.Page("app_pages/Media.py", title="Media", icon=":material/image:"),
    st.Page("app_pages/Upload and Download.py", title="Upload & Download", icon=":material/cloud_upload:"),
    st.Page("app_pages/State & control flow.py", title="State & Control Flow", icon=":material/bolt:"),
    st.Page("app_pages/Performace Helpers.py", title="Performance Helpers", icon=":material/speed:"),
    st.Page("app_pages/UX Helpers.py", title="UX Helpers", icon=":material/emoji_objects:"),
    st.Page("app_pages/Multi-page Routing.py", title="Multi-page Routing", icon=":material/route:"),
    st.Page("app_pages/Deployment.py", title="Deployment", icon=":material/rocket_launch:"),
]

navigation = st.navigation(pages)
navigation.run()
""")

attach_custom_css()
add_navigation(previous_page="UX Helpers.py", previous_page_title="UX Helpers",
               next_page="Deployment.py", next_page_title="Deployment")

