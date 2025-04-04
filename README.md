# Flask Customer Management API

A modern RESTful API for customer data management built with Flask and Python Requests.

## 🚀 Features

- RESTful API endpoints for customer management
- JSON response format
- Simple and efficient data retrieval
- Error handling and status codes
- Easy-to-use client implementation

## 🛠️ Tech Stack

- **Backend**: Flask
- **HTTP Client**: Python Requests
- **Data Format**: JSON
- **Language**: Python 3.6+

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/customers` | Retrieve all customers |
| GET | `/api/customers/<customer_id>` | Retrieve a specific customer |

## 🔧 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Git

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/camaramohamadou/simple-flask-requests-demo.git
   cd simple-flask-requests-demo
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   # For Unix/macOS
   python -m venv venv
   source venv/bin/activate

   # For Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Application

### Start the Server
```bash
python server.py
```
The server will start at `http://0.0.0.0:5000`

### Run the Client
```bash
python client.py
```

## 📝 Example Usage

### Server Response Format

```json
{
    "1": {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30
    },
    "2": {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "age": 25
    }
}
```

### Client Usage
```python
import requests

# Get all customers
response = requests.get('http://localhost:5000/api/customers')
print(response.json())

# Get specific customer
response = requests.get('http://localhost:5000/api/customers/1')
print(response.json())
```

## 🔍 Error Handling

The API returns appropriate HTTP status codes:
- 200: Success
- 404: Customer not found
- 500: Server error

## 🛣️ Roadmap

- [ ] Add database integration
- [ ] Implement authentication
- [ ] Add CRUD operations
- [ ] Create web interface
- [ ] Add data validation
- [ ] Implement testing
- [ ] Add documentation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Mohamadou Camara** - *Initial work*

## 🙏 Acknowledgments

- Flask documentation
- Python Requests library
- All contributors and users of this project

## 📞 Contact

- GitHub: [@camaramohamadou](https://github.com/camaramohamadou)
