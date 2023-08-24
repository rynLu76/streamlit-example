from collections import namedtuple
import altair as alt
import math
import pandas as pd
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


import streamlit as st
import s3fs
import os

fs = s3fs.S3FileSystem(anon=False)

@st.experimental_memo(ttl=600)
def read_file(filename):
    with fs.open(filename) as f:
        return f.read().decode('utf-8')
    
content = read_file("my-linkedin-jobs/final_df.csv")

for line in content.strip().split("\n"):
    print(line)
