import streamlit as st

from utils import attach_custom_css, add_navigation, sidebar_expander

sidebar_expander("Input Widgets", """
- [Input](#input)
- [Text Area](#text-area) 
- [Number Input](#number-input)
- [Slider](#slider)
- [Selectbox](#selectbox)
- [Checkbox](#checkbox)
- [Radio Button](#radio-button)
- [Toggle Button](#toggle-button)
- [Button](#button)
""")

st.title("Input Widgets")
st.caption("We'll explore different type of inputs available in streamlit")

st.divider()

st.header("Input")
st.caption("Takes simple text input in string format (parse to type as required)")

st.write("""
Its pretty simple, renders a text box and returns the value. There are some customizations available with optional parameters:
- help : Adds icon that, when hovered, displays help text
- label : Displayed right above input
- icon : Adds icon in the beginging of the input. can be used for currency e.t.c.
- type : "default" | "password"
- value : the default value
- placeholder
- **on_change** : we'll discuss it later in the section
""")

st.code("""
email = st.text_input(
    label="Email",
    placeholder="Enter your email",
    help="Promise 🤙🏼 we won't spam you",
    key="email"
)

password = st.text_input(
    label="Password",
    type="password",
    placeholder="Enter your password"
)

st.write(f""\"
    **Values updated when user taps out of the input**
    - Email : {email}
    - Password : {password}
""\")
""")

st.caption("**Renders the content below** :material/keyboard_double_arrow_down:. Try to input something in the fields")

email = st.text_input(
    label="Email",
    placeholder="Enter your email",
    help="Promise 🤙🏼 we won't spam you",
    key="email"
)

password = st.text_input(
    label="Password",
    type="password",
    placeholder="Enter your password"
)

st.write(f"""
    **Values updated when user taps out of the input**
    - Email : {email}
    - Password : {password}
""")

st.divider()

st.header("Text Area")
st.caption("Similar to input, but can take multi line text")
st.empty()
profile_summary = st.text_area(label="Describe your profile",
                               placeholder="I'm a software developer ...",
                               )
st.write(profile_summary)

st.divider()

st.header("Number Input")
st.write("""
Take a number input. No need to parse seperately. And comes with inbuilt validations.
- label
- step : The increment/decrement value on arrow key up/down
- min_value
- max_value
- help
- placeholder : _(not very useful here)_

> **Important : The return type of number input, depends on the type of parameter values passed** 

Checkout this example below:
""")
st.code("""
num = st.number_input(label="How many projects have you delivered on ?", step=1.0, min_value=1.0, max_value=5.0,
                      help="Your hike will be 5x percent of the number of projects you delivered")
st.write("Hike (_5x % of projects_) : ", str(num*5), '%')
""")

st.write("""> **Renders** :material/keyboard_double_arrow_down:""")

num = st.number_input(label="How many projects have you delivered on ?", step=1.0, min_value=1.0, max_value=5.0,
                      help="Your hike will be 5x percent of the number of projects you delivered")
st.write("Hike (_5x % of projects_) : ", str(num*5), '%')

st.divider()

st.header("Slider")
st.write("Simple slider to pick from a range of value. Like simple volume selector or temperature selector")

st.code("""
volume = st.slider(label="Select volume", min_value=1, max_value=5, step=1, help="Select volume")
st.write("Selected volume : ", str(volume))
""")

st.write("> **Renders this :material/keyboard_double_arrow_down:**")

volume = st.slider(label="Select volume", min_value=1, max_value=100, step=1, help="Select volume")
st.write("Selected volume : ", str(volume))

st.code("""
temprature = st.slider(label="Select temperature", min_value=0.2, max_value=1.0, step=0.05, help="Select temperature")
st.write("Selected temprature : ", str(temprature))
""")

st.write("> **Renders this :material/keyboard_double_arrow_down:**")

temprature = st.slider(label="Select temperature", min_value=0.2, max_value=1.0, step=0.05, help="Select temperature")
st.write("Selected temprature : ", str(temprature))


st.divider()

st.header("Selectbox")
st.caption('A simple drop down menu')

st.write("""
We have two important parameters here :
- options : The list of options to choose from
- index : The index of default selected element from the list 
""")

st.code("""
region = st.selectbox(label="Region", options=["US", "EU", "India"],
                      index=None, help="Server would be deployed in the region")
st.write("Selected region : ", region)
""")

st.write("> **Renders this :material/keyboard_double_arrow_down:**")

region = st.selectbox(label="Region", options=["US", "EU", "India"],
                      index=0, help="Server would be deployed in the region")
st.write("Selected region : ", region)

st.divider()
st.header("Multiselect")
st.caption("Similar to selectbox, except that multiple selections are possible")

st.code("""
regions = st.multiselect(label="Region", options=["US", "EU", "India"],  help="Server would be deployed to these regions")
st.write("Selected regions : ", regions)
""")

regions = st.multiselect(label="Region", options=["US", "EU", "India"],  help="Server would be deployed to these regions")
st.write("Selected regions : ", regions)

st.divider()

st.header("Checkbox")
st.caption("Pretty straight forward.")
st.code("""
user_agrees = st.checkbox("Opt for our newsletter", value=True)
st.write("Cool, we'll keep you updated" if user_agrees else "You'll miss important updates from ourside")
""")
st.write("> **Renders this :material/keyboard_double_arrow_down:**")
user_agrees = st.checkbox("Opt for our newsletter", value=True)
st.write("Cool, we'll keep you updated" if user_agrees else "You'll miss important updates from ourside")

st.divider()

st.header("Radio Button")
st.caption("Simple as hell again")

st.code("""
user_gender = st.radio(label="Gender", options=["Male", "Female", "Trans", "Non Binary", "Yet to decide"], index=None, help="Select you gender")
st.write("Selected gender : ", user_gender)
""")

st.write("> **Renders this :material/keyboard_double_arrow_down:**")

user_gender = st.radio(label="Gender", options=["Male", "Female", "Trans", "Non Binary", "Yet to decide"], index=None, help="Select you gender")
st.write("Selected gender : ", user_gender)

st.divider()

st.header("Toggle Button")
st.write("Modern checkbox, to be used when state is focused, not option. Like 'Opt for optional emails' is a checkbox, but dark mode is a toggle")

st.code("""
is_public_profile = st.toggle(label="Public profile", help="Your profile be availabe on web search results")
st.write(f"Your profile {"**not**" if not is_public_profile else ""} will be listed in web search results")
""")

st.write("> **Renders this :material/keyboard_double_arrow_down:**")
is_public_profile = st.toggle(label="Public profile", help="Your profile be availabe on web search results")
st.write(f"Your profile {"**not**" if not is_public_profile else ""} will be listed in web search results")

st.divider()

st.header("Button")
st.caption("Simple button that can trigger an action")

st.code("""
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increase counter"):
    st.session_state.counter += 1
    with st.empty():
        st.write("Counter value : ", st.session_state.counter)
""")

st.write("> **Renders this :material/keyboard_double_arrow_down:, focus only on button trigger the update**")

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increase counter"):
    st.session_state.counter += 1
    with st.empty():
        st.write("Counter value : ", st.session_state.counter)

attach_custom_css()

add_navigation(previous_page="Structure and Layout.py",
               previous_page_title="Structure and Layout",
               next_page_title="Structure and Layout",
               next_page="Structure and Layout.py"
               )

