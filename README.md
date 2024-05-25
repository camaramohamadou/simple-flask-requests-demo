# Flask Requests Demo

This project is a simple demonstration of using Flask to create a web server and the `requests` library to interact with it. The server provides endpoints to fetch customer data, and the client fetches and displays this data.

## Project Structure

- `server.py`: Contains the Flask server implementation.
- `client.py`: Contains the client code that uses the `requests` library to interact with the Flask server.
- `README.md`: Project documentation.
- `requirements.txt`: Lists the Python dependencies for the project.
- `.gitignore`: Specifies files and directories to be ignored by git.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/camaramohamadou/simple-flask-requests-demo.git
    cd flask_requests_demo
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Server

1. Start the Flask server:
    ```sh
    python server.py
    ```

2. The server will be running on `http://0.0.0.0:5000`.

### Running the Client

1. Run the client script to fetch and display customer data:
    ```sh
    python client.py
    ``

## Endpoints

- `GET /api/customers`: Retrieves all customer data.
- `GET /api/customers/<customer_id>`: Retrieves data for a specific customer by ID.

## Example Output

When running the client, you should see output similar to the following:

```sh
All Customer Data: {"1": {"name": "John Doe", "email": "john.doe@example.com", "age": 30}, "2": {"name": "Jane Smith", "email": "jane.smith@example.com", "age": 25}, "3": {"name": "Emily Johnson", "email": "emily.johnson@example.com", "age": 35}}
Customer Data: {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
