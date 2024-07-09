import requests

def test_list_of_products():
    r = requests.get('http://localhost:8000/products')
    response = r.json()
    print(response)

test_list_of_products()