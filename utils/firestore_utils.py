from google.cloud import firestore
import datetime

def get_deployments_data():
    db = firestore.Client()
    deployments_collection = db.collection("deployments")
    thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)
    query = deployments_collection.where("timestamp", ">=", thirty_days_ago)

    prod_data, all_data, stg_data, test_data = [], [], [], []

    for deployment in query.stream():
        doc_id = deployment.id
        app_name = deployment.get("app_name")
        deployment_version = deployment.get("deployment_version")
        env = deployment.get("env")
        rollback_version = deployment.get("rollback_version")
        timestamp_st = deployment.get("timestamp")
        formatted_datetime = timestamp_st.strftime('%Y-%m-%d')
        time = timestamp_st.strftime('%H:%M:%S')

        data = {
            "app_name": app_name,
            "deployment_version": deployment_version,
            "env": env,
            "rollback_version": rollback_version,
            "timestamp": formatted_datetime,
            "Time": time
        }

        if env == "production":
            prod_data.append(data)
        elif env == "staging":
            stg_data.append(data)
        elif "test" in env:
            test_data.append(data)

        all_data.append(data)

    return all_data, prod_data, stg_data, test_data



def get_full_data():
    db = firestore.Client()
    deployments_collection = db.collection("deployments")

    full_data = []

    for deployment in deployments_collection.stream():
        doc_id = deployment.id
        app_name = deployment.get("app_name")
        deployment_version = deployment.get("deployment_version")
        env = deployment.get("env")
        rollback_version = deployment.get("rollback_version")
        timestamp_st = deployment.get("timestamp")
        formatted_datetime = timestamp_st.strftime('%Y-%m-%d')
        time = timestamp_st.strftime('%H:%M:%S')

        data = {
            "app_name": app_name,
            "deployment_version": deployment_version,
            "env": env,
            "rollback_version": rollback_version,
            "timestamp": formatted_datetime,
            "Time": time
        }
        
        full_data.append(data)

    return full_data
