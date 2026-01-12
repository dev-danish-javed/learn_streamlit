import streamlit as st
import pandas as pd

# Page config, page_title -> tab title, page_icon -> favicon, layout -> wide=container fulid, center=container (bootstrap)
st.set_page_config(page_title='Danish Javed', page_icon="👨🏻‍💻", layout='wide')

# h1 tag. Page title. Should be used only once
st.title("Streamlit Notes")
# Wrties muted text, great for providing containt
st.caption("A sample streamlit page to demo commonly used elements")
st.page_link(icon="🔗", page="https://www.devdanish.in", label="by Danish Javed", help="Learn more about the author")

# hr tag
st.divider()

# Consider it as section heading
st.header("Introduction")
st.write("""
    Streamlit is UI tool native to python. The prime purpose for this is to act as data presentation layer.  
    The prime benfit
    - seamless integration in python codebase
    - no seperate front end backend request cycles
    - super fast and easy UI development 
    """)

st.divider()

st.header("Getting started")
st.text("Here I'm writing the details of my learnings. I'll be using streamlit to note down my streamlit notes 😂🔥")

st.divider()

st.subheader("Installation")
st.text("Let's get started with installation first.")
col1, col2 = st.columns(2)
with col1:
    st.text(" Add \"streamlit\" in requirements.txt and run command below 👇🏻")
    st.code("pip install -r requirements.txt")
with col2:
    st.write("Or simply do ")
    st.code("pip install streamlit")

st.divider()

st.subheader("Page Setup")
st.text("""Like we have head in html, this our place to setup our page.""")
st.code(body="""import streamlit as st
st.set_page_config(page_title='Danish Javed',page_icon="👨🏻‍💻", layout='wide')""", language="python")
st.markdown("""
 Some simple optoins that we have 
 - page_title -> tab title
 - page_icon -> favicon
 - layout _(bootstrap analogy)_
    - wide = container fulid
    - center = container
""")

st.divider()

st.subheader("Page title")
st.caption("Typically used once per page")
st.text(
    "Consider this as the page intro. Like headline of news or the title of our article. Below is what I have used for this page")
st.code(body="st.title(\"Streamlit Notes\")", language="python")

st.divider()

st.subheader("Headings")
st.text("In streamlit we have 2 heading options as header and subheader. Its intentional to keep it simple.")
header_col, subheader_col = st.columns(2)
with header_col:
    st.markdown("""##### Headers  

    - Translated to h2 tags
    - Mark heading of the section""")
    st.text("Like I have used for this section")
    st.code('st.header("Getting started")')
    pass
with subheader_col:
    st.markdown("""##### Subheaders  

        - Translated to h3 tags
        - Mark subheadings of the section""")
    st.text("Like I have used for this")
    st.code('st.subheader("Headings")')

st.divider()

st.subheader("Captions")
st.text("These are best to provide context for something. For ex, adds timeframe below a matrics etc")
st.text("Like I have used right below the page title")
st.code(body='st.context("A sample streamlit page to demo commonly used elements")')

st.divider()

st.subheader("Divider")
st.markdown("This is simple `<hr>`. Provides a horizontal ruling across the screen.")
st.code(body="st.divider()", language="python")

st.divider()
st.subheader("Code block")
st.markdown("This is `<code>` with streamlit styling and feature.")
st.markdown("We have three important and very useful parameters here.  ")
st.markdown("""
- body : the code
- width : the width of the block -> "content" | "streach"
- language : the language of the code
""")
st.code(body="""st.code(body="st.code('<code>')", language="python", width="content")""",
        language="python", width="content")

st.divider()
st.header("""Structure the layout""")
st.caption("Allows to provide structure our pages")

st.subheader("Columns")
st.text("Same as html tables but with slightly different syntax. "
        "There is no row explicitly. "
        "We create n number of columns that are all a part of one row. "
        "When we need new row, we create new set of columns, which by default will be rendered in a new row.")

st.code(body="""
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### Column 1")
    st.text("Blah blah "* 15)
with col2:
    st.markdown("#### Column 2")
    st.text("Blah blah "* 15)
with col3:
    st.markdown("#### Column 3")
    st.text("Blah blah "* 15)
""", language="python")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### Column 1")
    st.text("Blah blah " * 15)
with col2:
    st.markdown("#### Column 2")
    st.text("Blah blah " * 15)
with col3:
    st.markdown("#### Column 3")
    st.text("Blah blah " * 15)

st.markdown("""
#### Column width
""")
st.text("By default, the columns generated used equal width. But we do get the option to make them use custom width. "
        "Same columns as above used with different width.")
st.text("Instead of pssing the count of columns we want, we pass an array with ratio units of the widths we want. "
        "The count of the array size decides the number of columns ")
st.code("col1, col2, col3 = st.columns([4,2,1])", language="python")
col1, col2, col3 = st.columns([4, 2, 1])
with col1:
    st.markdown("#### Column 1")
    st.text("Blah blah " * 15)
with col2:
    st.markdown("#### Column 2")
    st.text("Blah blah " * 15)
with col3:
    st.markdown("#### Column 3")
    st.text("Blah blah " * 15)

st.divider()

st.subheader("Container")
st.text("""
This is a logic group of ui elements. Conceptually, they are similar to what components are in react.
They don't add anything on the UI level other than structural grouping, nothing visible to the user.
""")
st.code(body="""
with st.container():
    st.text("This is inside a container")

""", language="python")
st.text("Rendered as 👇🏻, notice that nothing fancy is happening here")
with st.container():
    st.text("This is inside a container")

st.text("The prime benifit is when paried with functions, they act as resulable blocks, conceptually, a component")

st.code(body="""
def greet_person(name:str):
    with st.container():
        prefix = "" if name.startswith("Mr") else "Mr. "
        st.markdown(f"Hello _**{prefix}{name}**_")

greet_person("Elon")
greet_person("Mr Trump")
""")
st.text('Renders 👇🏻')


def greet_person(name: str):
    with st.container():
        prefix = "" if name.startswith("Mr") else "Mr. "
        st.markdown(f"Hello _**{prefix}{name}**_")


greet_person("Elon")
greet_person("Mr Trump")

st.divider()

st.subheader("Expanders")
st.markdown("""
Just like we have `details` tag html, we have expanders in streamlit. The `summary` part goes as string parameter. 
""")
st.code(body="""
with st.expander("Summary"):
    st.text("This is expander content")
    st.text("Blah blah " * 150)
""", language="python")

st.text("Renders this 👇🏻")

with st.expander("Summary"):
    st.text("This is expander content")
    st.text("Blah blah " * 150)

st.divider()

st.subheader("Sidebars")
st.text(
    "Consider these are the side panel that we often see in the documentation "
    "or the filters section that we get in ecom websites. "
)
st.markdown("""
These have the same set of options that we have in streamlit, just that we have to do `st.sidebar.<anything else>`.
""")

st.caption(
    "I have kept the code down here, for article purpose, but its better to keep it on early part of the page for readability")
st.text("Checkout the upper left corner of this page. Click the icon and that's where the content is rendered.")

st.sidebar.title("Sidebar")
st.sidebar.text("The filters and other stuff goes here")

st.code("""
st.sidebar.title("Sidebar")
st.sidebar.text("The filters and other stuff goes here")
""")

st.divider()
st.header("Texts and messaging")
st.subheader('Write')
st.text("Most commonly used, and most versetile. "
        "We can throw any type of data and it'll render it perfectly. "
        "It auto-detects the input type and renders accordingly while accepting n number of arguments.")
st.write("""
- String → text / markdown
- Number → text
- List / dict → pretty print
- DataFrame → table
- Matplotlib / Plotly fig → chart
- Multiple args → spaced output
""")
st.text("Code for this 👆🏻 is here 👇🏻")
st.code(body="""
    st.write(\"""
    - String → text / markdown
    - Number → text
    - List / dict → pretty print
    - DataFrame → table
    - Matplotlib / Plotly fig → chart
    - Multiple args → spaced output
    ""\")
    """)
with st.expander("_**Checkout examples**_"):
    st.text("Some examples")
    text_col, markdown_col, number_col = st.columns(3)
    with text_col:
        st.markdown("**Text Example**")
        st.code("""st.write("Hello Text")""")
        st.write("Hello Text")
        pass
    with markdown_col:
        st.markdown("**Markdown Example**")
        st.code("""st.write("_**Hello markdown**_")""")
        st.write("_**Hello markdown**_")
        pass
    with number_col:
        st.markdown("**Number Example**")
        st.code("""st.write(525, 324)""")
        st.write(525, 324)
        pass
    with st.container():
        st.markdown("**List/Dict Example**")
        st.code("""
        st.write(["Hello", "**World**", 123], {"name":"Sahiba Bali", "occpation":"Actor/Influencer"})
        """)
        st.write(["Hello", 123], {"name": "Sahiba Bali", "occpation": "Actor/Influencer"})
        pass

    with st.container():
        st.markdown("#### Dataframes Examples")
        st.caption("For now they would seem a little too advance, that is why I have placed them here.")
        st.text("These are actually the most real world use cases and what we'll actually be doing in production. ")
        table_df = pd.DataFrame({
            "User": ["Aman", "Riya", "Karan", "Neha", "Ishaan"],
            "Plan": ["Pro", "Free", "Enterprise", "Pro", "Free"],
            "Amount (₹)": [2400, 0, 12000, 2400, 0],
            "Status": ["Success", "Pending", "Success", "Success", "Failed"]
        })
        st.write(table_df)

        # df = pd.DataFrame({
        #     "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        #     "revenue": [120, 150, 100, 180, 160, 220, 200],
        #     "users": [80, 95, 70, 110, 105, 140, 130],
        #     "conversion_rate": [3.2, 3.5, 2.9, 4.1, 3.8, 4.5, 4.3]
        # })
        # fig, ax = plt.subplots(figsize=(21, 9))
        #
        # sns.lineplot(
        #     data=df,
        #     x="day",
        #     y="revenue",
        #     marker="o",
        #     ax=ax
        # )
        #
        # ax.set_title("Daily Revenue Trend")
        # ax.set_ylabel("Revenue")
        # ax.set_xlabel("Day")
        #
        # plt.tight_layout()
        # st.write(fig)

st.divider()
st.subheader("Markdown")
st.text(
    "Streamlit also provides the option to use markdown. We can render any markdown in out UI and it would work fine.")
st.text("I have been using this through out the page. Bullet points are the simple examples.")
st.code(language="python", body="""
 st.markdown(\"""##### Subheaders  

        - Translated to h3 tags
        - Mark subheadings of the section""\")""")
st.caption("Not just these but we can use all the markdown tags")

st.markdown("##### ⚠️Hack")
st.caption("It's not recommended at all, as it breaks the UI consistency and defates the purpose of simplicity")
st.markdown(
    "We can also render html in streamlit, which we shouldn't unless its a must. we need to pass `unsafe_allow_html=True`. Here is an example")
st.code("""
st.markdown("We can also render html in streamlit, which we shouldn't unless its a must. Here is an example"
            "<span style=\"color:red\">This is html<span>", unsafe_allow_html=True)
""")
st.text("Renders 👇🏻")
st.markdown("<span style=\"color:red\">This is html<span>", unsafe_allow_html=True)

st.divider()

st.subheader("Code block")
st.markdown("This is `<code>` with streamlit styling and feature.")
st.markdown("We have three important and very useful parameters here.  ")
st.markdown("""
- body : the code
- width : the width of the block -> "content" | "streach"
- language : the language of the code
""")
st.code(body="""st.code(body="st.code('<code>')", language="python", width="content")""",
        language="python", width="content")

st.divider()

st.subheader("Text")
st.write("""
Usually, used for logs and data that are raw. **It doesn't allow markdown**.
""")

st.code('st.text("Hello World!!")', language="python", width="content")
st.text("Hello World!!")

st.divider()

st.subheader("Callouts")
st.write("""
These are elements used to provide status or key findings, like toast messages or notes blocks. We have 4 options available here.

- info
- error
- warning
- exception
""")

info_col, error_col = st.columns(2)
with info_col:
    st.write("""
    ##### Info
    """)
    st.code("""st.info("Password has to be alpha numeric.", icon="ℹ️")""",
            language="python", width="content")
    st.info("Dashboard API is online now", icon="ℹ️")
with error_col:
    st.write("""
    ##### Error
    """)
    st.code("""st.error("API Key expired", icon="🚨")""", language="python", width="content")
    st.error("Invalid API key", icon="🚨")

warning_col, exception_col = st.columns(2)
with warning_col:
    st.write("""##### Warning""")
    st.code("""st.warning("Password is to expire in 3 days.", icon="⚠️")""", language="python", width="content")
    st.warning("Password is to expire in 3 days.", icon="⚠️")
with exception_col:
    st.write("""##### Exception""")
    st.code("""st.exception(RuntimeError("This is a dummy exception"))""", language="python", width="content")
    st.exception(RuntimeError("This is a dummy exception"))

st.divider()

st.page_link("pages/widgets.py", label="Widgets Link")
# st.sidebar.page_link("pages/widgets.py", label="Widgets")
if st.button("Widget Button"):
    st.switch_page("pages/widgets.py")

