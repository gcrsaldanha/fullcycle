import pytest
from rest_framework.test import APIClient

from inventory.models import Category


@pytest.mark.django_db
class TestCategoriesListCreateView:
    def test_when_categories_exist_then_returns_list_of_categories(
        self,
        client: APIClient,
    ) -> None:
        category_1 = Category.objects.create(name="Alimentos")
        category_2 = Category.objects.create(name="Bebidas")

        response = client.get("/categories/")

        assert response.status_code == 200
        assert response.data == [
            {"id": category_1.id, "name": "Alimentos"},
            {"id": category_2.id, "name": "Bebidas"},
        ]

    def test_when_posting_new_category_then_returns_created_category(
        self,
        client: APIClient,
    ) -> None:
        response = client.post("/categories/", {"name": "Alimentos"})

        assert response.status_code == 201
        assert response.data["name"] == "Alimentos"
        assert response.data["id"] is not None

    def test_when_name_is_not_provided_then_returns_bad_request(
        self,
        client: APIClient,
    ) -> None:
        response = client.post("/categories/", {})

        assert response.status_code == 400
        assert response.data == {"name": ["This field is required."]}

    def test_when_no_categories_exist_then_returns_empty_list(
        self,
        client: APIClient,
    ) -> None:
        response = client.get("/categories/")

        assert response.status_code == 200
