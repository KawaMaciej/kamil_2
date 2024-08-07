import streamlit as st
import pandas as pd 
from ydata_profiling import ProfileReport
from streamlit_ydata_profiling import st_profile_report

data = pd.read_csv('heart.csv')
pr = ProfileReport(data, minimal=True, orange_mode=True, explorative=True)
st_profile_report(pr, navbar=True)