from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
# from st_files_connection import FilesConnection

conn = st.experimental_connection('s3', type=FilesConnection)
df = conn.read("my-linkedin-jobs/final_df.csv", input_format="csv", ttl=600)

# Print results.
for row in df.itertuples():
    print(row)
