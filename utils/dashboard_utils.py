import streamlit as st
import pandas as pd
import datetime

def setup_page():
    st.set_page_config(
        page_title="Hw-Deployments",
        page_icon="https://play-lh.googleusercontent.com/eJ2engLkD5uSTQohucDnGP0U6Q8A7LWOb436BgmPbLtzTvpvcmwGTUXknViF6-z94P4",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.sidebar.markdown("# Deployments Dashboard 🎈")
    st.subheader('Note: This is only apps using the shared Jenkins Deployment Pipeline (More to be added)', divider='rainbow')

    col1, col2 = st.columns(2)
    col1.title("HW Deployments Dashboard 🎈")
    col2.image("https://www.hostelworldgroup.com/~/media/Images/H/Hostelworld-v2/image-gallery/logos/master-lock-up-light-backgrounds.png", width=150)

def display_metrics(df):
    latest_versions = df.groupby('app_name').apply(lambda x: x.loc[x['timestamp'].idxmax(), 'deployment_version'])
    count_of_latest_versions = len(latest_versions)
    st.metric("Total Number of Services Deployed", count_of_latest_versions)

    st.subheader("Today's Deployments")
    df_today = df[df['timestamp'] == str(datetime.datetime.now().strftime('%Y-%m-%d'))]
    st.table(df_today)

    latest_versions_df = latest_versions.reset_index()
    latest_versions_df.columns = ['App Name', 'Latest Deployment Version']
    st.subheader("Latest Versions")
    st.table(latest_versions_df)

    st.subheader("Deploys the Last 30days")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    date_range = pd.date_range(start=df["timestamp"].min(), end=df["timestamp"].max())
    grouped_data = df.groupby("timestamp").size().to_frame(name='RecordCount')
    result = grouped_data.reindex(date_range).fillna(0)
    st.bar_chart(result)

    st.table(df)
