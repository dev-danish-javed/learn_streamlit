import json

import streamlit as st
import pandas as pd

from utils import set_page_config, add_navigation, attach_custom_css

set_page_config(page_title="Upload and download in Streamlit | Danish Javed")

st.sidebar.title("Upload and Download")
st.sidebar.markdown("""
- [Upload](#upload)
- [Download Button](#download-button)
""")

st.title("Upload and download")
st.caption("This is where we'll see how to upload and download files")
st.divider()
st.header("Upload")
st.write("""
Not the usual way of uploading files.
- Returns a file-like object
- Lives in memory, not persisted anywhere
- session bound
- gone at page refresh
- if users closes the file manager window, we get None

The important parameters are:
- label: text to display
- type: list of allowed file extensions
- on_change: callback function
- accept_multiple_files: True|False|"directory" : directory allows users to select a directory and all files will be uploaded
- help: Tooltip text with icon
- key: unique identifier, consider it like id
- disabled: True|False or int 0 for disabled anything else enabled
- max_upload_size : **Introduced in 1.53** 
""")

st.write("""
&nbsp;  
Consider this example below. Here we allow to upload only images or csv file. And then we render it accordingly.
&nbsp; 
""")

st.code("""
uploaded_file = st.file_uploader(label="Drop an image or csv",
                                 type=["jpg", "png", "jpeg", "csv"],
                                 help="Upload an image or csv",
                                 key="file_uploader")

if uploaded_file is not None:
    st.write(f\""" ###### :material/check: File uploaded successfully.
    - File name - {uploaded_file.name}
    - File type - {uploaded_file.type}
    - Size - {(uploaded_file.size/1024):.2f} kB
    \""")
    if uploaded_file.type.startswith("image/"):
        st.image(uploaded_file, caption="Uploaded Image.", width=300)
    else:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df, hide_index=True)
else:
    st.write("> ##### :material/data_alert: No file uploaded.")
""")

uploaded_file = st.file_uploader(label="Drop an image or csv",
                                 type=["jpg", "png", "jpeg", "csv"],
                                 help="Upload an image or csv",
                                 key="file_uploader")

if uploaded_file is not None:
    st.write(f""" ###### :material/check: File uploaded successfully.
    - File name - {uploaded_file.name}
    - File type - {uploaded_file.type}
    - Size - {(uploaded_file.size/1024):.2f} kB
    """)
    if uploaded_file.type.startswith("image/"):
        st.image(uploaded_file, caption="Uploaded Image.", width=300)
    else:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df, hide_index=True)
else:
    st.write("> ##### :material/data_alert: No file uploaded.")

st.write("##### Upload multiple files")

st.code("""
uploaded_files = st.file_uploader(label="Select folder with image and CSVs only", type=["jpg", "png", "jpeg", "csv"], accept_multiple_files="directory")
if uploaded_files is None:
    st.write("> ##### :material/data_alert: No files uploaded.")
else :
    for uploaded_file in uploaded_files:
        st.write(f\""" ###### :material/check: File loaded successfully.
            - File name - {uploaded_file.name}
            - File type - {uploaded_file.type}
            - Size - {(uploaded_file.size / 1024):.2f} kB
            \""")
        if uploaded_file.type.startswith("image/"):
            st.image(uploaded_file, caption="Uploaded Image.", width=300)
        else:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df, hide_index=True)
""")

uploaded_files = st.file_uploader(label="Select folder with image and CSVs only", type=["jpg", "png", "jpeg", "csv"], accept_multiple_files="directory")
if uploaded_files is None:
    st.write("> ##### :material/data_alert: No files uploaded.")
else :
    for uploaded_file in uploaded_files:
        st.write(f""" ###### :material/check: File loaded successfully.
            - File name - {uploaded_file.name}
            - File type - {uploaded_file.type}
            - Size - {(uploaded_file.size / 1024):.2f} kB
            """)
        if uploaded_file.type.startswith("image/"):
            st.image(uploaded_file, caption="Uploaded Image.", width=300)
        else:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df, hide_index=True)

st.divider()
st.header("Download Button")
st.write("""
This allows users to download a file.
- label: text to display on button
- data: data to download
- file_name: name of the file to be downloaded

We need not to care about the mime type, streamlit takes care of it.

> ##### ⚠️ Binary files always go in as byte array

Checkout the code below:
""")

st.code("""
json_data = {"name": "Danish Javed", "profile": "full stack developer",
             "linkedin": "https://www.linkedin.com/in/devdanish/",
             "portfolio": "https://www.devdanish.in",
             "email": "dev.danish.javed@gmail.com",
             "blogs": "https://technotes.devdanish.in"}

st.download_button(label="Download JSON", data=json.dumps(json_data, indent=2), file_name="danish-profile.json")

with open("assets/Rida In Garden.png", "rb") as file:
    st.download_button(
        label="Download AI Image",
        data=file,
        file_name="Rida_In_Garden.png",
        mime="image/png"
    )
""")

json_data = {"name": "Danish Javed", "profile": "full stack developer",
             "linkedin": "https://www.linkedin.com/in/devdanish/",
             "portfolio": "https://www.devdanish.in",
             "email": "dev.danish.javed@gmail.com",
             "blogs": "https://technotes.devdanish.in"}

st.download_button(label="Download JSON", data=json.dumps(json_data, indent=2), file_name="danish-profile.json")

with open("assets/Rida In Garden.png", "rb") as file:
    st.download_button(
        label="Download AI Image",
        data=file,
        file_name="Rida_In_Garden.png",
        mime="image/png"
    )

attach_custom_css()
add_navigation(previous_page="pages/08_Media.py", previous_page_title="Charts")
