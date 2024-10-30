import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
    [data-testid="stMetricValue"] {
        font-size: 100px; 
    }
    .stCaption {
    font-size: 16px; /* Adjust font size as needed */
    font-weight: bold;
    color: red; /* Adjust color as needed */
    }
    </style>
    """, unsafe_allow_html=True)


