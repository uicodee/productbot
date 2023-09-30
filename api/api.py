import requests


def get_products() -> list[dict]:
    response = requests.get(url="https://dummyjson.com/products").json()
    return response['products']


def get_single_product(product_id: int) -> dict:
    return requests.get(url=f"https://dummyjson.com/products/{product_id}").json()
