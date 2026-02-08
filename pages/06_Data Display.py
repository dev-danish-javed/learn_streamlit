import streamlit as st
import pandas as pd

from utils import add_navigation, attach_custom_css, set_page_config

set_page_config(page_title="Data Display in Streamlit | Danish Javed")

st.title("Data Display")
st.caption("Now these are the actual stuff that we'll see more often")

st.divider()

st.header("Metrics")
st.write("""
Metrics displays the KPIs. We have some very useful options:
- `label` : what the data is about
- `value` : current value
- `delta` : the change from last value
- `delta_color` : "inverse" | "normal" | "off" -> By default, postive value is considered good and is green, we can change the nature with inverse or disable it with off
- `delta-arrow` : "up" | "down" |  "off" | "auto"

> **Checkout the sample code below :material/keyboard_double_arrow_down:**
""")

st.code("""

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        label="Revenue",
        value="₹12.4M",
        delta="+8%",
        chart_data=[4, 10, 6, 8]
    )
    pass
with col2:
    st.metric(
        label="Customer Exit",
        value="12",
        delta="2%",
        chart_data=[20,15,10,12],
        chart_type="bar",
        delta_color="inverse"
    )
    pass
with col3:
    st.metric(
        label="Weekly Sales",
        value="200k",
        delta="+12%",
        chart_data=[50, 70, 90, 30, 78, 200],
        chart_type="area"
    )
    pass
""")

st.write("> **Renders as below :material/keyboard_double_arrow_down:**")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        label="Revenue",
        value="₹12.4M",
        delta="+8%",
        chart_data=[4, 10, 6, 8]
    )
    pass
with col2:
    st.metric(
        label="Customer Exit",
        value="12",
        delta="2%",
        chart_data=[4,10,6,8,20,15,10,12,4,10,6,8,20,15,10,12],
        chart_type="bar",
        delta_color="inverse"
    )
    pass
with col3:
    st.metric(
        label="Weekly Sales",
        value="200k",
        delta="+12%",
        chart_data=[50, 70, 90, 30, 78, 200],
        chart_type="area"
    )
    pass

st.divider()

st.header("Table")
st.write("""Its a simple table, no additional features. We have 2 simple parameters
- data
- border : True|False|Horizontal
&nbsp;  
&nbsp;  
**Sample code :material/keyboard_double_arrow_down:**
""")

st.code("""
df = pd.DataFrame({
    "date": pd.date_range("2026-01-01", periods=7).date,
    "revenue": [120, 150, 100, 180, 160, 220, 200],
    "users": [80, 95, 70, 110, 105, 140, 130],
    "conversion_rate": [3.2, 3.5, 2.9, 4.1, 3.8, 4.5, 4.3]
})
st.table(data=df,border="horizontal")
""")
st.write("> **Renders the table below :material/keyboard_double_arrow_down:**")
df = pd.DataFrame({
    "date": pd.date_range("2026-01-01", periods=7).date,
    "revenue": [120, 150, 100, 180, 160, 220, 200],
    "users": [80, 95, 70, 110, 105, 140, 130],
    "conversion_rate": [3.2, 3.5, 2.9, 4.1, 3.8, 4.5, 4.3]
})
st.table(data=df,border="horizontal")

st.divider()

st.header("Dataframe")
st.write("""
Its an interactive table that is:
- sortable
- scrollable
- resizeable
- searchable
- downloadable

&nbsp;  
&nbsp;
We have some cool optoins here
- `height` : its better to provide a height to the table or else the large dataset will expand a lot
- `use_container_width` : True by default, it set to False, the table will take width as per content width
- `row_height` : Explicitly set height of each row
- `hide_index` : By default row index are displayed, we can hide them with this option

&nbsp;  

**Sample code :material/keyboard_double_arrow_down:**

""")

st.code("""
df = pd.DataFrame({
    "date": pd.date_range("2026-01-01", periods=7).date,
    "revenue": [120, 150, 100, 180, 160, 220, 200],
    "users": [80, 95, 70, 110, 105, 140, 130],
    "conversion_rate": [3.2, 3.5, 2.9, 4.1, 3.8, 4.5, 4.3]
})
st.dataframe(
    df,
    height=150,
    use_container_width=True,
    hide_index=True,
    row_height=40,
)
""")

st.write("> **Renders the table below :material/keyboard_double_arrow_down:**")

df = pd.DataFrame({
    "date": pd.date_range("2026-01-01", periods=7).date,
    "revenue": [120, 150, 100, 180, 160, 220, 200],
    "users": [80, 95, 70, 110, 105, 140, 130],
    "conversion_rate": [3.2, 3.5, 2.9, 4.1, 3.8, 4.5, 4.3]
})
st.dataframe(
    df,
    height=150,
    use_container_width=True,
    hide_index=True,
    row_height=40,
)

st.divider()

st.header('JSON viewer')
st.write("""Displays json in simple format. We have only 2 simple parameters
- body : The json data
- expanded : _default True_, if it has to remains expanded by default

The code below :material/keyboard_double_arrow_down:
""")
st.code("""
json_data = {
    "user": "danish",
    "active": True,
    "roles": ["admin", "editor"],
    "stats": {
        "logins": 42,
        "last_login": "2026-01-09"
    }
}

st.json(body=json_data, expanded=False)
""")

st.write("> **Renders the content as below :material/keyboard_double_arrow_down:**")
json_data = {
    "user": "danish",
    "active": True,
    "roles": ["admin", "editor"],
    "stats": {
        "logins": 42,
        "last_login": "2026-01-09"
    }
}

st.json(body=json_data, expanded=False)

st.write("> ##### But the way its most commonly used is with expanders like below :material/keyboard_double_arrow_down:")
st.code("""
with st.expander("See raw data"):
    st.json(body=json_data)
""")
with st.expander("See raw data"):
    st.json(body=json_data)




st.sidebar.title("Data Display")
st.sidebar.markdown("""
- [Metrics](#metrics)
- [Table](#table)
- [Dataframe](#dataframe)
- [JSON Viewer](#json-viewer)
""")

attach_custom_css()
add_navigation(previous_page="05_Forms.py", previous_page_title="Forms",
               next_page="07_Charts.py", next_page_title="Charts")