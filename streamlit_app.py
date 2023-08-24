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
import os
from st_files_connection import FilesConnection

conn = st.experimental_connection('s3', type=FilesConnection)
df = conn.read("my-linkedin-jobs/final_df.csv", input_format="csv", ttl=600)

# Print results.
for row in df.itertuples():
    print(row)
