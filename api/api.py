import requests
from aiohttp import ClientSession


async def get_products() -> list[dict]:
    async with ClientSession() as session:
        async with session.get(url="https://dummyjson.com/products") as response:
            response = await response.json()
            return response['products']
    # response = requests.get(url="https://dummyjson.com/products").json()
    # return response['products']


async def get_single_product(product_id: int) -> dict:
    async with ClientSession() as session:
        async with session.get(url=f"https://dummyjson.com/products/{product_id}") as response:
            return await response.json()
    # return requests.get(url=f"https://dummyjson.com/products/{product_id}").json()
