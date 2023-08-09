import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_user_can_add_and_remove_products_from_stock(client: APIClient) -> None:
    # Create a new category
    response = client.post("/categories/", {"name": "Alimentos"})
    category_id = response.data["id"]

    # Assert new category is now listed
    response = client.get("/categories/")
    assert response.data[0]["id"] == category_id

    # Create a new product
    response = client.post("/products/", {"name": "Arroz", "category_id": category_id})
    product_id = response.data["id"]

    # Assert new product is now listed with quantity = 0
    response = client.get("/products/")
    assert response.data["data"][0]["id"] == product_id
    assert response.data["data"][0]["quantity"] == 0

    # Add 10 units of the product to stock
    response = client.post(f"/inventory/add/", {"product_id": product_id, "quantity": 10})
    assert response.status_code == 200

    # Assert product quantity is now 10
    response = client.get(f"/products/{product_id}/")
    assert response.data["quantity"] == 10

    # Remove 5 units of the product from stock
    response = client.post(f"/inventory/sub/", {"product_id": product_id, "quantity": 5})
    assert response.status_code == 200

    # Assert product quantity is now 5
    response = client.get(f"/products/{product_id}/")
    assert response.data["quantity"] == 5
