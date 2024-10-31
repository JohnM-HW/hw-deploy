import streamlit as st
import pandas as pd
import datetime
from utils.css_utils import apply_custom_css
from utils.firestore_utils import get_deployments_data
from utils.data_processing import process_data





# Page Setup 
st.set_page_config(
    page_title="Hw-Deployments",
    page_icon="https://play-lh.googleusercontent.com/eJ2engLkD5uSTQohucDnGP0U6Q8A7LWOb436BgmPbLtzTvpvcmwGTUXknViF6-z94P4",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.sidebar.markdown("# Deployments Dashboard 🎈")
st.subheader('Note: This is only apps using the shared Jenkins Deployment Pipeline (More to be added)', divider='rainbow')

col1, col2 = st.columns(2)
col1.title("HW Deployments Dashboard - PROD 🎈")
col2.image("https://www.hostelworldgroup.com/~/media/Images/H/Hostelworld-v2/image-gallery/logos/master-lock-up-light-backgrounds.png", width=150)




# Apply custom CSS
apply_custom_css()


# Loading Data
@st.cache_data(ttl=180)
def load_data():
    all_data, prod_data, stg_data, test_data = get_deployments_data()
    return process_data(all_data, prod_data, stg_data, test_data)
df, df_prod, df_stg, df_test, result = load_data()

# Strip out the latest Deployments 
latest_versions = df_prod.groupby('app_name').apply(lambda x: x.loc[x['timestamp'].idxmax(), 'deployment_version'])


# Count the Lastest Versions
count_of_latest_versions = len(latest_versions)
st.metric("Total Number of Services Deployed", count_of_latest_versions)

# Todays Deployments
st.subheader("Today's Deployments")
df_today = df_prod[df_prod['timestamp'] == str(datetime.datetime.now().strftime('%Y-%m-%d'))]
st.table(df_today)

# Latest Versions 
latest_versions_df = latest_versions.reset_index()
latest_versions_df.columns = ['App Name', 'Latest Deployment Version']
st.subheader("Latest Versions")
st.table(latest_versions_df)


# Bar Chart of Latest Deploys in PROD

st.subheader("Deploys the Last 30days")
df_prod["timestamp"] = pd.to_datetime(df_prod["timestamp"])
date_range = pd.date_range(start=df_prod["timestamp"].min(), end=df_prod["timestamp"].max())
grouped_data = df_prod.groupby("timestamp").size().to_frame(name='RecordCount')
result = grouped_data.reindex(date_range).fillna(0)
st.bar_chart(result)

# 30 day data
st.table(df_prod)







