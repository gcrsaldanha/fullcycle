import pytest
from rest_framework.test import APIClient

from inventory.models.category import Category
from inventory.models.product import Product


@pytest.mark.django_db
class TestProductsListView:
    def test_when_products_exist_then_returns_list_of_products(
        self,
        client: APIClient,
    ) -> None:
        category = Category.objects.create(name="Alimentos")
        product_1 = Product.objects.create(name="Arroz", category=category, quantity=10)
        product_2 = Product.objects.create(name="Feijão", category=category, quantity=20)

        response = client.get("/products/")

        assert response.status_code == 200
        assert response.data == {
            "data": [
                {
                    "id": product_1.id,
                    "name": "Arroz",
                    "quantity": 10,
                    "category_id": category.id,
                    "category_name": "Alimentos",
                },
                {
                    "id": product_2.id,
                    "name": "Feijão",
                    "quantity": 20,
                    "category_id": category.id,
                    "category_name": "Alimentos",
                },
            ],
            "meta": {"page": 1},
        }

    def test_when_no_products_exist_then_returns_empty_list(
        self,
        client: APIClient,
    ) -> None:
        response = client.get("/products/")

        assert response.status_code == 200
        assert response.data == {
            "data": [],
            "meta": {"page": 1},
        }


@pytest.mark.django_db
class TestProductsCreateView:
    def test_when_posting_new_product_then_returns_created_response(
        self,
        client: APIClient,
    ) -> None:
        category = Category.objects.create(name="Alimentos")

        response = client.post("/products/", {"name": "Arroz", "category_id": category.id})

        assert response.status_code == 201

    def test_when_name_is_not_provided_then_returns_bad_request(
        self,
        client: APIClient,
    ) -> None:
        category = Category.objects.create(name="Alimentos")

        response = client.post("/products/", {"category_id": category.id})

        assert response.status_code == 400
        assert response.data == {"name": ["This field is required."]}

    def test_when_category_id_is_not_provided_then_returns_bad_request(
        self,
        client: APIClient,
    ) -> None:

        response = client.post("/products/", {"name": "Arroz"})

        assert response.status_code == 400
        assert response.data == {"category_id": ["This field is required."]}

    def test_when_category_does_not_exist_then_returns_bad_request(
        self,
        client: APIClient,
    ) -> None:
        response = client.post("/products/", {"name": "Arroz", "category_id": 1})

        assert response.status_code == 400
        assert response.data == {"category_id": ["Category with id 1 does not exist."]}


@pytest.mark.django_db
class TestProductRetrieveView:
    def test_when_product_does_not_exist_then_return_not_found(self, client: APIClient) -> None:
        response = client.get("/products/1/")

        assert response.status_code == 404
        assert response.data == {"detail": "Not found."}

    def test_when_product_exists_then_return_serialized_product(self, client: APIClient) -> None:
        category = Category.objects.create(name="Alimentos")
        product = Product.objects.create(name="Arroz", quantity=10, category=category)

        response = client.get(f"/products/{product.id}/")

        assert response.status_code == 200
        assert response.data == {
            "id": product.id,
            "name": "Arroz",
            "quantity": 10,
            "category_id": category.id,
            "category_name": "Alimentos",
        }
