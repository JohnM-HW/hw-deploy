import streamlit as st
from google.cloud import firestore
import pandas as pd
import datetime


# Page Setup 

st.set_page_config(
    page_title="Hw-Deploynments",
    page_icon="https://play-lh.googleusercontent.com/eJ2engLkD5uSTQohucDnGP0U6Q8A7LWOb436BgmPbLtzTvpvcmwGTUXknViF6-z94P4",
    layout="wide",
    initial_sidebar_state="expanded"
)

col1, col2 = st.columns(2)
col2.image("https://www.hostelworldgroup.com/~/media/Images/H/Hostelworld-v2/image-gallery/logos/master-lock-up-light-backgrounds.png", width=150)
col1.title("Deployments Dashboard 🎈")

# sidebar 
st.sidebar.markdown("# Deployments Dashboard 🎈")
st.subheader('Note: This is only apps using the shared Jenkins Deployment Pipeline (More to be added)', divider='rainbow')


@st.cache_data(ttl=180)  # Cache results for 180 seconds
def get_deployments_data():
    # Initialize Firestore client
    db = firestore.Client()

    # Get the deployments collection
    deployments_collection = db.collection("deployments")

    # Calculate the date 30 days ago from today
    thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)

    # Query the collection for documents from the past 30 days
    query = deployments_collection.where("timestamp", ">=", thirty_days_ago)

    prod_data = []
    all_data = []
    stg_data = []
    test_data = []

    for deployment in query.stream():
        # Extract data from each document
        doc_id = deployment.id
        app_name = deployment.get("app_name")
        deployment_version = deployment.get("deployment_version")
        env = deployment.get("env")
        rollback_version = deployment.get("rollback_version")
        timestamp_st = deployment.get("timestamp")

        # Given timestamp
        timestamp = timestamp_st

        # Convert to regular date and time format
        formatted_datetime = timestamp.strftime('%Y-%m-%d')

        # Extract day from timestamp
        time = timestamp.strftime('%H:%M:%S')

        if env == "production":
            # Only add data to the list if env = production
            prod_data.append({
                "app_name": app_name,
                "deployment_version": deployment_version,
                "env": env,
                "rollback_version": rollback_version,
                "timestamp": formatted_datetime,
                "Time": time
            })

        elif env == "staging":
            # Only add data to the list if env = staging
            stg_data.append({
                "app_name": app_name,
                "deployment_version": deployment_version,
                "env": env,
                "rollback_version": rollback_version,
                "timestamp": formatted_datetime,
                "Time": time
            })

        elif env.find("test") != -1:
            # Only add data to the list if env = test (lots of different names used )
            test_data.append({
                "app_name": app_name,
                "deployment_version": deployment_version,
                "env": env,
                "rollback_version": rollback_version,
                "timestamp": formatted_datetime,
                "Time": time
            })    

        # Add all the data to the list
        all_data.append({
            "app_name": app_name,
            "deployment_version": deployment_version,
            "env": env,
            "rollback_version": rollback_version,
            "timestamp": formatted_datetime,
            "Time": time
        })

    return (all_data, prod_data, stg_data, test_data)


# Retrieve deployment data from Firestore for each list
all_data = get_deployments_data()[0]
prod_data = get_deployments_data()[1]
stg_data = get_deployments_data()[2]
test_data = get_deployments_data()[3]

# Create pandas DataFrame
df = pd.DataFrame(all_data)
df_prod = pd.DataFrame(prod_data)
df_stg = pd.DataFrame(stg_data)
df_test = pd.DataFrame(test_data)


df["timestamp"] = pd.to_datetime(df["timestamp"])
date_range = pd.date_range(start=df["timestamp"].min(), end=df["timestamp"].max())
grouped_data = df.groupby("timestamp").size().to_frame(name='RecordCount')

result = grouped_data.reindex(date_range).fillna(0)

st.bar_chart(result)
weekly_data = result.resample('W').sum()
st.table(weekly_data)


latest_versions = df.groupby('app_name').apply(lambda x: x.loc[x['timestamp'].idxmax(), 'deployment_version'])
st.dataframe(latest_versions)
st.table(latest_versions)

count_of_latest_versions = len(latest_versions)

st.metric("Total", count_of_latest_versions)
### Overall Data 

# Sort DataFrame by timestamp
df.sort_values(by="timestamp", inplace=True, ascending=False)

# Count unique app names
unique_app_names = df["app_name"].nunique()
unique_app_prod = df_prod["app_name"].nunique()
unique_app_stg = df_stg["app_name"].nunique()
unique_app_test = df_test["app_name"].nunique()

st.subheader("Number of deployments per ENV")

# Count timestamps per day
timestamp_counts_per_day = df["timestamp"].value_counts()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total", unique_app_names)
col2.metric("PROD", unique_app_prod, (unique_app_prod - unique_app_stg))
col3.metric("Staging", unique_app_stg, (unique_app_stg - unique_app_test ))
col4.metric("TEST", unique_app_test)

# Calculate average of timestamp counts per day
avg_deployments_per_day = timestamp_counts_per_day.mean()
rounded_avg_deployments_per_day = round(avg_deployments_per_day, 1)

st.metric(label="Average deployments per day across All ENVs:", value=rounded_avg_deployments_per_day)



# Count timestamps per day
timestamp_counts_per_day = df["timestamp"].value_counts()

# Create a bar chart of timestamp counts per day
st.caption("Number of deployments per day across all ENVs")
st.bar_chart(timestamp_counts_per_day)

# st.caption("Number of deployments per day across all ENVs")
# st.line_chart(timestamp_counts_per_day)


# Display the Todays Deployments
st.caption("Todays Deployments")
df_today = df[df['timestamp'] == str(datetime.datetime.now().strftime('%Y-%m-%d'))]
st.dataframe(df_today)

st.caption("All Deployments")
df.sort_values(by="timestamp", inplace=True, ascending=False)
st.dataframe(df)