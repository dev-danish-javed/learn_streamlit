import streamlit as st

from utils import set_page_config, add_navigation, attach_custom_css

set_page_config(page_title="Upload and download in Streamlit | Danish Javed")

attach_custom_css()


st.sidebar.title("State and control flow")
st.sidebar.markdown("""
- [Rerun](#st-rerun)
- [Stop](#st-stop)
- [Session State](#session-state)
""")

st.title("State and control flow")
st.caption("Now we are hitting the real stuff. Pay attention or else, we'll get 2am calls from the project manager")
st.write("""
We have three important concepts here.
- `st.rerun()`
- `st.stop()`
- `st.session_state`

Let's get over them one by one
""")

st.divider()
st.header("`st.rerun()`")
st.write("""
Immediately aborts the current execution and starts the script again from the top. Triggered after any widget interaction implicitly. Helpful to load session state updates and restore UI. 

> **We'll see this in action in the sections below.**

""")
st.divider()

st.header("`st.stop()`")
st.write("""
Stops the execution of the current script. Helpful when prerequisites are not met. Like user is not logged in.
Or paywall is set. Or the file not uploaded to anlayse.

Consider this; we know that any widget interaction reruns the script. So if we click a button, the script will rerun.
Let's do this, we'll stop the script when the user clicks the button to effectively stop rendering the content below that part.
""")

st.code("""
if st.button("Rerun the script to restore the page"):
    st.rerun()
if st.button("Stop the script"):
    st.stop()
st.write("Hit the stop button to stop anything being rendered from this point")
""")

if st.button("Rerun the script to restore the page"):
    st.rerun()
if st.button("Stop the script"):
    st.stop()
st.write("Hit the stop button to stop anything being rendered from this point")

st.divider()

st.header("Session State")
st.write("""
This is an important concept. Read very carefully. 
- One dict
- Per user session
- Survives reruns, **not page refreshes**
- Explicit, not reactive
    - changes made do not reflecte in the UI automatically
    - we are responsible for that

Think server-side sessionStorage, that's it. So **it won't survive page refreshes**.
We have a map that we can use to store data, and it would remain across reruns for the entire user session.
But mind it, not shared across users. The map's scope is only for the current user session.

The change in session state doesn't reflect in the UI automatically. We have to explicitly update the UI by rerunning it.

&nbsp;  
> Now check the code below :material/keyboard_double_arrow_down:
""")
st.code("""
st.write(f"Hello {st.session_state.get("session_demo_user_name", "Reader")}")
st.session_state["session_demo_user_name"] = "Danish"
st.write(f"Hello {st.session_state.get("session_demo_user_name", "Reader")}")
if st.button("Rerun"):
    st.rerun()
""")

st.write("""Before looking at this in action, let's understand what's happening here.
- `st.write(f"Hello {st.session_state.get("session_demo_user_name", "Reader")}")`
    - We are printing the value of the key `session_demo_user_name` from the session state. 
    - If it doesn't exist, we are printing the default value `Reader`.
    - When you first landed on the page, it would say, "Hello Reader"
- `st.session_state["session_demo_user_name"] = "Danish"`
    - We are setting the value of the key `session_demo_user_name` to "Danish" in the session state.
- Now, here is the important bit. Even when we set the value in session, first line still says "Hello Reader"
- `st.write(f"Hello {st.session_state.get("session_demo_user_name", "Reader")}")`
    - This time, it prints the value of the key `session_demo_user_name` from the session state. 
    - Since we have set the value, it prints "Hello Danish"
    - But first line still says "Hello Reader"
- Now, why is that? Because we have not rerun the code yet. Sessions sate is not reactive and changing the value won't do anything unless we do
- With the `Rerun` button, we have provided a way to rerun the code.
- Once you rerun the page, you'll see both of them saying "Hello Danish"
- Now even if we run it `n` times, both will always say "Hello Danish", becaues it can survive reruns.
- Even if we go to another page, come back and come back, it'll still say "Hello Danish", because its the same session.
- Even if we use `st.session_state.get("session_demo_user_name")` in another page hereafter, we'll always get "Danish"
- What happens when we refresh the page? 
    - Session is reset and so is the sesstion_state
    - We'll again see "Hello Reader" and "Hello Danish

&nbsp;

> Checkout the ouptut below :material/keyboard_double_arrow_down:
""")

st.write(f"Hello {st.session_state.get("session_demo_user_name", "Reader")}")
st.session_state["session_demo_user_name"] = "Danish"
st.write(f"Hello {st.session_state.get("session_demo_user_name", "Reader")}")
if st.button("Rerun"):
    st.rerun()

add_navigation(previous_page="pages/09_Upload and Download.py", previous_page_title="Upload and Download",
               next_page="pages/11_Performace Helpers.py", next_page_title="Performance Helpers")