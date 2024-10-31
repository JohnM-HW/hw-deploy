import streamlit as st
import pandas as pd
from utils.css_utils import apply_custom_css
from utils.firestore_utils import get_deployments_data, get_full_data
from utils.data_processing import process_data, process_full_data
from utils.dashboard_utils import setup_page, display_metrics


# Page Setup
setup_page()

# Apply custom CSS
apply_custom_css()


# Loading Data

@st.cache_data(ttl=180)
def load_full_data():
    full_data = get_full_data()
    return process_full_data(full_data)

full_data = load_full_data()





st.dataframe(full_data)

