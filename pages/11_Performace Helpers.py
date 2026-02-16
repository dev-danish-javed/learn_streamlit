import os
import time
from datetime import datetime

import streamlit as st
import pandas as pd
from utils import set_page_config, add_navigation, attach_custom_css, get_logger

set_page_config(page_title="Performance Helpers in Streamlit | Danish Javed")
st.title("Performance Helpers")
st.caption("Section under progress, please check back soon 🖖🏻")

logger = get_logger("Performace Helpers")


st.divider()
st.header("`st.cache_data`")
st.write("""
This decorator caches the data. It memorizes the entire exection of the function 
and keeps replaying that without actually executing it.

> **Check the example below :material/keyboard_double_arrow_down:**

""")

st.code("""
@st.cache_data
def load_data():
    logger.info("Loading chocolate dataset ...")
    st.info("Loading chocolate dataset ...", icon=":material/info:")
    return pd.read_csv("assets/kaggle-chocolate-sales-dataset.csv")

df = load_data()

if st.button("Rerun"):
    st.rerun()
st.dataframe(df, height=250)
""")

st.write("> **Play with it a little, and then we continue :material/keyboard_double_arrow_down:**")

@st.cache_data(max_entries=1)
def load_chocolate_data():
    logger.info("Loading chocolate dataset ...")
    st.info("Loading chocolate dataset ...", icon=":material/info:")
    return pd.read_csv("assets/kaggle-chocolate-sales-dataset.csv")

df = load_chocolate_data()

if st.button("Rerun"):
    st.rerun()
st.dataframe(df, height=250)

st.write("""
&nbsp;

Now, let me tell you something interesting. The first time this page is loaded, it loads the file. 
The UI says, "Loading dataset ..." and the logs say the same. 
Thereafter, when you rerun or refesh the page or open the page in another browser, the UI says, "Loading dataset ..." 
but the logs say absolutely nothing. Why?

Because when the app was loaded for the first time and the cached function was executed for the first time,
Streamlilt executed the function and memorized the execution, including the result. After that, whenever
Streamlit has to rerun the function, it doesn't. It just replays the cached result.  

Hence, we get the same result on UI but logs are empty.
""")

st.write("")
st.subheader("Cache expiration")
st.caption("**Now we know how it's cached, but how would the data refresh?**")
st.write("""
We have three options here: 
- We set the expiration time: &nbsp; _parameter_ `ttl`
- We set parameters to watch that'll trigger the cache refresh 
    - Streamlit memroizes the execution, but would be consistent given the input parameters are same
    - If input changes, execution would be required and hence cache would be invalidated
- Manually invalidate the cache

#### ttl
Set the time in timedelta or seconds. The cache would be invalidated after the specified time.
#### `max_entries`
One important parameter is `max_entries`, the max number of variants Streamlit would
rember for this function. If we say 2, it would remember 2 variants of the function and 
wouldn't execute the function again.

&nbsp;  
> **Check the example below :material/keyboard_double_arrow_down:**
""")

st.code("""

@st.cache_data(show_time=True, ttl=10, show_spinner="Loding webseries data", max_entries=2)
def load_webseries_data(random):
    logger.info("Identifier : " + str(random))
    time.sleep(0.5)
    logger.info(f"Loading webseries dataset...")
    return pd.read_csv("assets/kaggle_indian_webseries_ratings.csv")
df = load_webseries_data(1)
df = load_webseries_data(2)
df = load_webseries_data(3)
df = load_webseries_data(3)
df = load_webseries_data(2)
df = load_webseries_data(1)
""")

@st.cache_data(show_time=True, ttl=10, show_spinner="Loding webseries data", max_entries=2)
def load_webseries_data(random):
    logger.info("Identifier : " + str(random))
    time.sleep(0.5)
    logger.info(f"Loading webseries dataset...")
    return pd.read_csv("assets/kaggle_indian_webseries_ratings.csv")
df = load_webseries_data(1)
df = load_webseries_data(2)
df = load_webseries_data(3)
df = load_webseries_data(3)
df = load_webseries_data(2)
df = load_webseries_data(1)

st.write("""
- `ttl`: Time in sec, we can also use timedelta like `pd.Timedelta(days=1)`
    - In our case, it would be invalidated in 10 secs
- `max_entries`: The specifies that Stramlit would remeber 2 variants of the function at max. So, when we call it for the time, it executes and memorizes the execution.
Thereafter, the same happens for the second and third call. Then, we have called it again with the same last two parameters, 3 and 2. Those were already memorized, so 
instead of execting the functions, it replays the cached result. Then when we call it with 1 again, it doesn't finds it because the results were ditched because of the max_entries.
Hence, it executes and memorizes the result again. 

&nbsp;  
> **Here is what the logs look like :material/keyboard_double_arrow_down:**
""")
st.code(body="""
[2026-02-16 09:04:47,283] [INFO] Performace Helpers: Identifier : 1
[2026-02-16 09:04:49,283] [INFO] Performace Helpers: Loading webseries dataset...
[2026-02-16 09:04:49,291] [INFO] Performace Helpers: Identifier : 2
[2026-02-16 09:04:51,293] [INFO] Performace Helpers: Loading webseries dataset...
[2026-02-16 09:04:51,298] [INFO] Performace Helpers: Identifier : 3
[2026-02-16 09:04:53,299] [INFO] Performace Helpers: Loading webseries dataset...
[2026-02-16 09:04:53,304] [INFO] Performace Helpers: Identifier : 1
[2026-02-16 09:04:55,304] [INFO] Performace Helpers: Loading webseries dataset...
""", language="log")

st.write("""
&nbsp;  
#### Hash functions
Now let's dive a little into the boring yet exiting stuff. We know Streamlit memorizes the execution of the functions and replays. But how are these executions stored? Well, as **dict**. 
The hashof parameters act as keys and the execution as values. So, when we call the function with the same parameters, it replays the cached result.
But what if the parameter is complex object and hashing changes based other factors that we don't care about. Well, causes irrelevant cache miss. 

Streamlit provides a way to customize the hashing function. The input objects are hased as per our logic, and we can maximize the cache hit ourselves.

Check out the example below, where we have overriden the hashing function to always return the same value and hence to Streamlit the parameters are always the same.
Hence, the function is executed only once and replayed afterwards. 

_And bro, this was just for experimentation, don't do this to a prodcution system, that won't be cache hit, but a disaster._

""")

st.code("""
class Dummy:
    def __init__(self, x):
        self.x = x

@st.cache_data(show_time=True, ttl=10, show_spinner="Loding webseries data", max_entries=2, hash_funcs={
    Dummy: lambda x: 1
})
def load_webseries_data_with_custom_hashing(random: Dummy):
    logger.info("Custom hashing dentifier : " + str(random))
    time.sleep(0.5)
    logger.info(f"Loading webseries dataset with custom hashing...")
    return pd.read_csv("assets/kaggle_indian_webseries_ratings.csv")
df = load_webseries_data_with_custom_hashing(Dummy(1))
df = load_webseries_data_with_custom_hashing(Dummy(2))
df = load_webseries_data_with_custom_hashing(Dummy(3))
df = load_webseries_data_with_custom_hashing(Dummy(2))
df = load_webseries_data_with_custom_hashing(Dummy(3))
df = load_webseries_data_with_custom_hashing(Dummy(1))
""")

class Dummy:
    def __init__(self, x):
        self.x = x

@st.cache_data(show_time=True, ttl=10, show_spinner="Loding webseries data", max_entries=2, hash_funcs={
    Dummy: lambda x: 1
})
def load_webseries_data_with_custom_hashing(random: Dummy):
    logger.info("Custom hashing dentifier : " + str(random))
    time.sleep(0.5)
    logger.info(f"Loading webseries dataset with custom hashing...")
    return pd.read_csv("assets/kaggle_indian_webseries_ratings.csv")
df = load_webseries_data_with_custom_hashing(Dummy(1))
df = load_webseries_data_with_custom_hashing(Dummy(2))
df = load_webseries_data_with_custom_hashing(Dummy(3))
df = load_webseries_data_with_custom_hashing(Dummy(2))
df = load_webseries_data_with_custom_hashing(Dummy(3))
df = load_webseries_data_with_custom_hashing(Dummy(1))

st.write("""
&nbsp; 
Coming back to chache invalidation. One thing we have already seen is `ttl`. Antoher approach like we discussed is to change the parameters, but the examples we saw were not for production.
Here is how it's done instead. We pass the last modified time of the file in parameters and when that changes, Stremalit executes the function again.

> **Check out the example below :material/keyboard_double_arrow_down:**
""")

st.code("""
@st.cache_data(show_time=True, ttl="1d", show_spinner="Loding webseries data")
def load_webseries_data_with_modified_time(modified_time):
    logger.info(f"Loading webseries dataset with modified time...")
    return pd.read_csv("assets/kaggle_indian_webseries_ratings.csv")

time_s  = os.path.getmtime("assets/kaggle_indian_webseries_ratings.csv")
load_webseries_data_with_modified_time(time_s)
""")

@st.cache_data(show_time=True, ttl="1d", show_spinner="Loding webseries data")
def load_webseries_data_with_modified_time(modified_time):
    logger.info(f"Loading webseries dataset with modified time...")
    return pd.read_csv("assets/kaggle_indian_webseries_ratings.csv")

time_s  = os.path.getmtime("assets/kaggle_indian_webseries_ratings.csv")
load_webseries_data_with_modified_time(time_s)

if st.button("Rerun", key="rerun_button"):
    st.rerun()

st.write("""
Now, this what this code does, it sets the ttl to 1 day and adds modified time of the file in parameters. 
So, whenever the file is modified, it executes the function again. To test it out, load the page and check logs. It 
logs "_Loading webseries dataset with modified time..._" once, and thereafter if we rerun 100 times, it won't and then we change the file
and rerun, it'll log again.

&nbsp;
#### cleaning the logs manually.
We can also clean the logs manually. We can do that by calling `st.cache_data.clear()`. Right now we have seen how the 
function with modified time only refreshes once a day or when a file is changed. Let's implement a button to clear the chache and rerun the page and see what logs say.
```python
if st.button("Clear cache and refresh"):
    st.cache_data.clear()
    st.rerun()
```
""")

if st.button("Clear cache and refresh"):
    st.cache_data.clear()
    st.rerun()


attach_custom_css()
add_navigation(previous_page="pages/10_State & control flow.py", previous_page_title="State & Control Flow",
               next_page="pages/12_UX Helpers.py", next_page_title="UX Helpers")
