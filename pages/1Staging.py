import streamlit as st
import pandas as pd
from utils.css_utils import apply_custom_css
from utils.firestore_utils import get_deployments_data
from utils.data_processing import process_data
from utils.dashboard_utils import setup_page, display_metrics

# Page Setup
setup_page()

# Apply custom CSS
apply_custom_css()



# Loading Data
@st.cache_data(ttl=180)
def load_data():
    all_data, prod_data, stg_data, test_data = get_deployments_data()
    return process_data(all_data, prod_data, stg_data, test_data)

df, df_prod, df_stg, df_test, result = load_data()


display_metrics(df_stg)
