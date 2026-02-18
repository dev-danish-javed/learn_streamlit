import numpy as np
import streamlit as st
import pandas as pd

from utils import attach_custom_css, add_navigation, sidebar_expander

sidebar_expander("Charts", """
- [Line Chart](#line-chart)
- [Bar Chart](#bar-chart)
- [Area Chart](#area-chart)
""")


st.title("Charts")
st.write("""Streamlit provides only three charts types natively
- Line Chart
- Bar Chart
- Area Chart

&nbsp;  
&nbsp;
There are some common parameters that can be used to customize these chart.
- `use_container_width` : True|False, default True, when use entire available width
- `width` : 600 or whatever you want
- `height` : 300 or whatever you want
- `x` : The property to be used as x-axis,
- `y` : The property to be used as y-axis,
- `x_label` : Label for x-axis,
- `y_label` : Label for y-axis,
- `color` : Array of hex colors for the graph

""")

st.divider()
st.header("Line Chart")
st.write("""
Show how a value changes over an ordered dimension for continious data.
Good for cases were we only want to show the trend.
It helps plot points and show their relations. Ex: If the stock stable, is it going up or down, 
number of visitors, sales trend, performance in load testing etc.  

Below we have dummy data to show the user base growth over time in mobile and web apps.
This data can simply show the user trends for both.

- date : pd.date_range("2025-08-31", periods=7, freq="W") - generates a weekly time series of 7 weeks
- app_users : [40, 60, 220, 240, 332, 360, 372] - dummy data for mobile app users
- web_users : [160, 250, 180, 140, 165, 160, 172] - dummy data for web users
- set_index("date") - sets the date as index i.e the x-axis
""")

st.code("""
default_line_chart, pareameterized_line_chart = st.columns(2)
with default_line_chart:
    st.write("> **Renders as below :material/keyboard_double_arrow_down:**")

    # relativly simple line chart
    df_2 = pd.DataFrame({
        "Date": pd.date_range("2025-08-31", periods=7, freq="W"),
        "App Users": [40, 60, 220, 240, 332, 360, 372],
        "Web Users": [160, 250, 180, 140, 165, 160, 172]
    }).set_index("Date")
    st.line_chart(df_2)

with pareameterized_line_chart:
    st.write("> **The version with more parameters :material/keyboard_double_arrow_down:**")

    df = pd.DataFrame({
        "Date": pd.date_range("2025-08-31", periods=7, freq="W"),
        "App Users": [40, 60, 220, 240, 332, 360, 372],
        "Web Users": [160, 250, 180, 140, 165, 160, 172]
    })
    # polished
    st.line_chart(df,
                  x="Date",
                  y=["App Users", "Web Users"],
                  x_label="Date",
                  y_label="Users",
                  color=["#00f7c6", "#8400f7"],
                  use_container_width=True,
                  height=300,)
""")
default_line_chart, pareameterized_line_chart = st.columns(2)
with default_line_chart:
    st.write("> **Renders as below :material/keyboard_double_arrow_down:**")

    # relativly simple line chart
    df_2 = pd.DataFrame({
        "Date": pd.date_range("2025-08-31", periods=7, freq="W"),
        "App Users": [40, 60, 220, 240, 332, 360, 372],
        "Web Users": [160, 250, 180, 140, 165, 160, 172]
    }).set_index("Date")
    st.line_chart(df_2)

with pareameterized_line_chart:
    st.write("> **The version with more parameters :material/keyboard_double_arrow_down:**")

    df = pd.DataFrame({
        "Date": pd.date_range("2025-08-31", periods=7, freq="W"),
        "App Users": [40, 60, 220, 240, 332, 360, 372],
        "Web Users": [160, 250, 180, 140, 165, 160, 172]
    })
    # polished
    st.line_chart(df,
                  x="Date",
                  y=["App Users", "Web Users"],
                  x_label="Date",
                  y_label="Users",
                  color=["#00f7c6", "#8400f7"],
                  use_container_width=True,
                  height=300,)

st.divider()

st.header("Bar Chart")
st.write("""
Show how discrete buckets compare in magnitude.
- X axis : categories
- Y axis : values

Ex. the number of users in different regions of the world, number of sales in different categories etc.
""")

st.code("""
default_bar_chart, paramerterized_bar_chart = st.columns(2)

with default_bar_chart:
    st.write("> **Default Bar Chart**")
    df_2 = pd.DataFrame({
        "Payment Method": ["UPI", "Debit Card", "NetBanking", "Wallet", "Credit Card", "Venmo", "ACH", "Cash"],
        "Amount Paid": [520, 340, 180, 90, 803, 280, 410, 605],
        "Amount Due": [120, 200, 0, 600, 166, 56, 70, 125],
    })
    st.bar_chart(df_2, x="Payment Method", y=["Amount Due","Amount Paid"])

with paramerterized_bar_chart:
    st.write("> **The version with more parameters :material/keyboard_double_arrow_down:**")

    df = pd.DataFrame({
        "Payment Method": ["UPI", "Debit Card", "NetBanking", "Wallet", "Credit Card", "Venmo", "ACH", "Cash"],
        "Amount Paid": [520, 340, 180, 90, 803, 280, 410, 605],
        "Amount Due": [120, 200, 0, 600, 166, 56, 70, 125],
    }).set_index("Payment Method")

    st.bar_chart(df,
                 use_container_width=False,
                 width=600, height=300,
                 x_label="Payment Method", y_label="Amount",
                 color=["#95ff00", "#ff8c00"],  stack=False, sort=False)
""")

default_bar_chart, paramerterized_bar_chart = st.columns(2)

with default_bar_chart:
    st.write("> **Default Bar Chart**")
    df_2 = pd.DataFrame({
        "Payment Method": ["UPI", "Debit Card", "NetBanking", "Wallet", "Credit Card", "Venmo", "ACH", "Cash"],
        "Amount Paid": [520, 340, 180, 90, 803, 280, 410, 605],
        "Amount Due": [120, 200, 0, 600, 166, 56, 70, 125],
    })
    st.bar_chart(df_2, x="Payment Method", y=["Amount Due","Amount Paid"])

with paramerterized_bar_chart:
    st.write("> **The version with more parameters :material/keyboard_double_arrow_down:**")

    df = pd.DataFrame({
        "Payment Method": ["UPI", "Debit Card", "NetBanking", "Wallet", "Credit Card", "Venmo", "ACH", "Cash"],
        "Amount Paid": [520, 340, 180, 90, 803, 280, 410, 605],
        "Amount Due": [120, 200, 0, 600, 166, 56, 70, 125],
    }).set_index("Payment Method")

    st.bar_chart(df,
                 use_container_width=False,
                 width=600, height=300,
                 x_label="Payment Method", y_label="Amount",
                 color=["#95ff00", "#ff8c00"],  stack=False, sort=False)

st.divider()

st.header("Area Chart")
st.write("""
Similar to line chart, but with area under the curve, which emphasizes the magnitude and volume.
""")

st.code("""
df = pd.DataFrame({
    "Date": pd.date_range("2024-01-01", periods=7, freq="D"),
    "Free Users": [120, 135, 450, 665, 280, 195, 210],
    "Premium Users": [30, 185, 40, 250, 160, 270, 85],
}).set_index("Date")

plain_area_chart, polished_are_chart = st.columns(2)
with plain_area_chart:
    st.write("> **Default Area Chart**")
    st.area_chart(df)

with polished_are_chart:
    st.write("> **Area Chart with more parameters**")
    st.area_chart(df,
                 use_container_width=False,
                 width=600, height=300,
                 x_label="Date", y_label="Users",
                 color=["#4f819c", "#939c4f"])
""")


df = pd.DataFrame({
    "Date": pd.date_range("2024-01-01", periods=7, freq="D"),
    "Free Users": [120, 135, 450, 665, 280, 195, 210],
    "Premium Users": [30, 185, 40, 250, 160, 270, 85],
}).set_index("Date")

plain_area_chart, polished_are_chart = st.columns(2)
with plain_area_chart:
    st.write("> **Default Area Chart**")
    st.area_chart(df)

with polished_are_chart:
    st.write("> **Area Chart with more parameters**")
    st.area_chart(df,
                 use_container_width=False,
                 width=600, height=300,
                 x_label="Date", y_label="Users",
                 color=["#4f819c", "#939c4f"])

attach_custom_css()
add_navigation(previous_page_title="Data Display", previous_page="Data Display.py", next_page_title="Media", next_page="Media.py")

