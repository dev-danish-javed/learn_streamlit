import streamlit as st

from utils import add_navigation, attach_custom_css, sidebar_expander

sidebar_expander("Media", """
- [Images](#images)
- [Video](#video)
- [Audio](#audio)
""")

st.title("Media")
st.caption('This is fun simple section')

st.write("""
In the media part streamlit provides three types of media
- Image
- Video
- Audio

> ⚠️ These are very simple widgets, don't expect the events and control as html and js
""")

st.divider()

st.header("Images")
st.write("""
This is very simple widget, just pass the image path and caption. The parameters are pretty straight forward.
- `image` : path/url to the image
- `caption` : caption for better context
- `width` : to control the size
- `use_container_width` : to make the image fill the width of the container
""")

st.code("""
st.image(image="assets/linkedin_cover.png", caption="My LinkedIn Cover Photo")

img_1_col, img_2_col = st.columns(2)

with img_1_col:
    version_1_col, version_2_col = st.columns(2)
    with version_1_col:
        st.image("assets/sample_image_1.png", width=200, caption="How I imagine myself")
    with version_2_col:
        st.image(image="https://images.stockcake.com/public/0/4/f/04f6eb18-f4c8-4f11-a4e1-5aaf59c86c7a/coding-anime-hero-stockcake.jpg", caption="How I imagine myself")
with img_2_col:
    st.image("assets/sample_image_2.png", use_container_width=True, caption="How I see my hello world  apps")
""")

st.write("> **Renders this :material/keyboard_double_arrow_down:**")

st.image(image="assets/linkedin_cover.png", caption="My LinkedIn Cover Photo")

img_1_col, img_2_col = st.columns(2)

with img_1_col:
    version_1_col, version_2_col = st.columns(2)
    with version_1_col:
        st.image("assets/sample_image_1.png", width=200, caption="How I imagine myself")
    with version_2_col:
        st.image(image="https://images.stockcake.com/public/0/4/f/04f6eb18-f4c8-4f11-a4e1-5aaf59c86c7a/coding-anime-hero-stockcake.jpg", caption="How I imagine myself")
with img_2_col:
    st.image("assets/sample_image_2.png", use_container_width=True, caption="How I see my hello world  apps")

st.divider()

st.header("Video")
st.write("Pretty simple and straight forwards, checkout the code below")
st.code("""
local_video_col, link_video_col = st.columns(2)
with local_video_col:
    st.video(data="assets/Rida_Street_Food.mp4", width=350)
with link_video_col:
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", width="stretch")
""")

local_video_col, link_video_col = st.columns(2)
with local_video_col:
    st.video(data="assets/Rida_Street_Food.mp4", width=350)
with link_video_col:
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", width="stretch")

st.divider()
st.header("Audio")
st.write("Pretty simple and straight forwards, checkout the code below")

st.code("""
# this loops first 20 seconds of the audio but user can explicity skip to any part of the audio
st.audio("assets/alexgrohl-burn-the-track.mp3", end_time="20s", loop=True)
""")

st.audio("assets/alexgrohl-burn-the-track.mp3", end_time="20s", loop=True)

attach_custom_css()
add_navigation(previous_page="Charts.py", previous_page_title="Charts", next_page="Upload and Download.py", next_page_title="Upload and Download")

