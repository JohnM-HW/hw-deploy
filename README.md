# Deployment Tracker

Deployment Tracker is a tool for tracking deployments using Firebase and Streamlit. It monitors all deployments executed through Jenkins.

## Features

- Track deployments in real-time
- Visualize deployment history
- Integrate seamlessly with Jenkins

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/deployment-tracker.git
    ```
2. Navigate to the project directory:
    ```bash
    cd deployment-tracker
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Open your web browser and go to `http://localhost:8501` to access the app.

## Configuration

- Ensure your Firebase credentials are set up in the `firebase_config.json` file.
- Configure Jenkins to send deployment data to the app.

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

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please open an issue or contact us at your-email@example.com.
