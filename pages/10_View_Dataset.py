import streamlit as st
import pandas as pd
from core import (
    sidebar,
    data_variables
)

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="Dataset Summary - Smart Traffic Violation Pattern Detector Dashboard", 
    page_icon="📝", 
    layout="wide"
)

# ------------------------------
# LOAD DATA
# ------------------------------
st.title("📝 Dataset Summary")
st.markdown("Visualize and analyze traffic violation data.")

df = sidebar.render_sidebar()
total_data_records = len(df)
st.metric(label="Total Data Records", value=total_data_records)

if set(data_variables.TRAFFIC_VIOLATION_COLUMNS).issubset(set(df.columns)):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        input_query_violation_type =  st.text_input("Violations Type Search",help="Search for violations Type")
    with col2:
        input_query_driver_gender =  st.text_input("Driver Gender Search",help="Search for driver gender")
    with col3:
        input_query_driver_age =  st.text_input("Driver Age Search",help="Search for driver age")
    with col4:
        input_query_driver_license =  st.text_input("Driver License Search",help="Search for driver license")

# Filter the dataset
df_filtered = df

if set(data_variables.TRAFFIC_VIOLATION_COLUMNS).issubset(set(df.columns)):
    if input_query_violation_type:
        df_filtered = df_filtered[df_filtered['Violation_Type'].astype(str).str.contains(input_query_violation_type, case=False, na=False)]
    if input_query_driver_gender:
        df_filtered = df_filtered[df_filtered['Driver_Gender'].astype(str).str.contains(input_query_driver_gender, case=False, na=False)]
    if input_query_driver_age:
        df_filtered = df_filtered[df_filtered['Driver_Age'].astype(str).str.contains(input_query_driver_age, case=False, na=False)]
    if input_query_driver_license:
        df_filtered = df_filtered[df_filtered['Driver_License'].astype(str).str.contains(input_query_driver_license, case=False, na=False)]

    st.write(f"## Search Results:`{df_filtered.shape[0]}` Records Found")
st.data_editor(df_filtered)