# Deployment Tracker

Deployment Tracker is a tool for tracking deployments using Firebase and Streamlit. It monitors all deployments executed through Jenkins.

## Features

- Track deployments in real-time
- Visualize deployment history

## WIP 
- Adding a github action



## Installation

1. Clone the repository:
    ```bash
    git clone git@github.com:JohnM-HW/hw-deploy.git
    ```
2. Navigate to the project directory:
    ```bash
    cd hw-deploy
    ```
3. Build the container:
    ```bash
    docker build -t hw-deploy .
    ```
4. Run the container:
    ```bash
    docker run -p 8501:8501 -v $(pwd)/credentials.json:/app/credentials.json -e GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json hw-deploy
    ```
5. Open your web browser and go to `http://localhost:8501` to access the app.

## Run Locally

1. Start the Streamlit app:
    ```bash
    streamlit run main.py
    ```
2. Open your web browser and go to `http://localhost:8501` to access the app.



## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Open a pull request.

## Contact

For any questions or suggestions, please open an issue or contact us at sre@hostelworld.com
