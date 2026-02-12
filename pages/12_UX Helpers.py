import streamlit as st
import time

from utils import set_page_config, add_navigation, attach_custom_css

set_page_config(page_title="Performance & UX Helpers in Streamlit | Danish Javed")

st.sidebar.title("UX Helpers")
st.sidebar.markdown("""
- [Spinner](#spinner)
- [Progress](#progress)
- [Toaster](#toaster)
- [Status](#status)
""")
st.title("UX Helpers")
st.caption("""
Widgets to help us improve the user experience.
""")

st.divider()
st.header("Spinner")
st.write("""
Displays a spinner while the task is running. Simple params
- `text`: text to display while code is executed
- `show_time`: show the time taken to execute the code
- `width`: "content"|"streach" width of the spinner  

Check out the example below :material/keyboard_double_arrow_down:
""")

st.code("""
if st.button("Run a heavy task"):
    with st.spinner(text="Processing...", show_time=True, width="stretch"):
        placeholder = st.warning("in progress")
        time.sleep(3)
    placeholder.success("Done")
""")

st.write("> **Works like this :material/keyboard_double_arrow_down:**")

if st.button("Run a heavy task"):
    with st.spinner(text="Processing...", show_time=True, width="stretch"):
        placeholder = st.warning("in progress")
        time.sleep(3)
    placeholder.success("Done")

st.divider()

st.header("Progress")
st.write("""
We can use this when we want to show progress updates of some task. Like we see in download bar etc.

Check out the example below :material/keyboard_double_arrow_down:
""")

st.code("""
# kept it inside button to not slow down the page load
if st.button("See progress bar"):
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(1 if percent_complete % 30 == 0 else 0.05)
        my_bar.progress(percent_complete + 1, text=progress_text+ " : " + str(percent_complete) + "% done")
    time.sleep(1)
    my_bar.success("Done!")
""")

st.write("> **Works like this :material/keyboard_double_arrow_down:**")

progress_text = "Operation in progress. Please wait."
if st.button("See progress bar"):
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(1 if percent_complete % 30 == 0 else 0.05)
        my_bar.progress(percent_complete + 1, text=progress_text+ " : " + str(percent_complete) + "% done")
    time.sleep(1)
    my_bar.success("Done!")

st.divider()
st.header("Toaster")
st.write("""
Displays a toast message at the upper right corner of the screen. Simple params
- `body`: markdown message to display
- `icon`: icon to display along with the message
- `duration`: "short", "long", "infinite", or int sec time to display the message

""")
st.code("""
if st.button("Show toast"):
    st.toast("This is a toast message", icon=":material/info:", duration=3)
""")
if st.button("Show toast"):
    st.toast("This is a toast message", icon=":material/info:", duration=3)

st.divider()
st.header("Status")
st.write("""
Spinner showed just that something is happening.
Progress bar showed the amount of progress made in the task.
Status provides very clear details about the state of the task.

Rule of thumb 
- Spinner: when we don't know how long the task will take
- Progress bar: when we know the exact time taken to complete the task
- Status: when we know the exact step by step state of the task

Again, simple params
- `label`: text to display
- `expanded`: True|False : if true, the status bar will be expanded to show more details
- `state`: "running"|"complete"|"error" : state of the status bar

&nbsp;  
We can use it two different ways. Check the examples below :material/keyboard_double_arrow_down:
""")

st.code("""
        with st.status(label="Installing packages...", state="running") as status:
            time.sleep(2)
            status.update(label="Downloading dependencies...")
            time.sleep(2)
            status.update(label="Extracting files!")
            time.sleep(2)
            status.update(label="Installing...")
            time.sleep(2)
            status.update(label="Done!", state="complete")
            
        with st.status("Installing packages...", expanded=True, state="running") as status:
            time.sleep(2)
            st.write("Downloading dependencies...")
            time.sleep(2)
            st.write("Extracting files!")
            time.sleep(2)
            st.write("Done !!")
            status.update(label="Installation complete", state="complete")
""")
example_1_col, example_2_col = st.columns(2)

with example_1_col:
    if st.button("Check example 1"):
        with st.status(label="Installing packages...", state="running") as status:
            time.sleep(2)
            status.update(label="Downloading dependencies...")
            time.sleep(2)
            status.update(label="Extracting files!")
            time.sleep(2)
            status.update(label="Installing...")
            time.sleep(2)
            status.update(label="Done!", state="complete")

with example_2_col:
    if st.button("Check example 2"):
        with st.status("Installing packages...", expanded=True, state="running") as status:
            time.sleep(2)
            st.write("Downloading dependencies...")
            time.sleep(2)
            st.write("Extracting files!")
            time.sleep(2)
            st.write("Done !!")
            status.update(label="Installation complete", state="complete")


attach_custom_css()
add_navigation(previous_page="pages/11_Performace Helpers.py", previous_page_title="Performance & UX Helpers")