import streamlit as st
from utils.firestore_utils import get_deployments_data
from utils.data_processing import process_data

st.set_page_config(
    page_title="Hw-Deployments",
    page_icon="https://play-lh.googleusercontent.com/eJ2engLkD5uSTQohucDnGP0U6Q8A7LWOb436BgmPbLtzTvpvcmwGTUXknViF6-z94P4",
    layout="wide",
    initial_sidebar_state="expanded"
)

col1, col2, col3 = st.columns(3)
col2.title("Deployments Dashboard 🎈")
col1.image("https://www.hostelworldgroup.com/~/media/Images/H/Hostelworld-v2/image-gallery/logos/master-lock-up-light-backgrounds.png", width=100)
col3.image("https://www.hostelworldgroup.com/~/media/Images/H/Hostelworld-v2/image-gallery/logos/master-lock-up-light-backgrounds.png", width=150)


st.sidebar.markdown("# Deployments Dashboard 🎈")
st.subheader('Note: This is only apps using the shared Jenkins Deployment Pipeline (More to be added)', divider='rainbow')

@st.cache_data(ttl=180)
def load_data():
    all_data, prod_data, stg_data, test_data = get_deployments_data()
    return process_data(all_data, prod_data, stg_data, test_data)

df, df_prod, df_stg, df_test, result = load_data()

latest_versions = df.groupby('app_name').apply(lambda x: x.loc[x['timestamp'].idxmax(), 'deployment_version'])


count_of_latest_versions = len(latest_versions)
st.metric("Total Number of Deployments", count_of_latest_versions)

st.table(latest_versions)
