import streamlit as st
import pandas as pd
from core import data_variables

st.set_page_config(
    page_title="Smart Traffic Violation Pattern Detector Dashboard", 
    page_icon="🚗",
    layout="wide"
)

st.markdown(
    """
    <style>
    .marquee-container {
        overflow: hidden;
        white-space: nowrap;
        box-sizing: border-box;
        background: #111;
        padding: 8px 0;
        border-radius: 4px;
    }
    .marquee-text {
        display: inline-block;
        padding-left: 100%;
        animation: marquee 15s linear infinite;
        color: #fff;
        font-weight: 500;
    }
    @keyframes marquee {
        0%   { transform: translateX(0%); }
        100% { transform: translateX(-100%); }
    }
    </style>

    <div class="marquee-container">
        <span class="marquee-text">
            🚦 Smart Traffic Management System · Real-time dashboard · Data-driven city safety · Drive responsibly ❤️
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Smart Traffic Violation Pattern Detector Dashboard")
st.write("This app allows you to analyze traffic violation patterns in a given dataset.")

