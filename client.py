import requests

def get_all_customers():
    url = 'http://localhost:5000/api/customers'
    response = requests.get(url)

    if response.status_code == "200":
        print("All Customer Data:", response.json())
    else:
        print("Error:", response.json())

def get_customer_data(customer_id):
    url = f'http://localhost:5000/api/customers/{customer_id}'
    response = requests.get(url)
    if response.status_code == 200:
        print("Customer Data:", response.json())
    else:
        print("Error:", response.json())

if __name__ == "__main__":
    get_all_customers()
    # Example: Get customer with ID '1'
    #get_customer_data('1')
