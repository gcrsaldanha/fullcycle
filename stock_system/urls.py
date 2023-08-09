from django.contrib import admin
from django.urls import path

from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', views.CategoriesListCreateView.as_view(), name='categories-list-create'),
    path('products/', views.ProductsListCreateView.as_view(), name='products-create'),
    path('products/<int:pk>/', views.ProductRetrieveView.as_view(), name='products-retrieve'),
    path('inventory/add/', views.add_to_inventory, name='inventory-add'),
    path('inventory/sub/', views.remove_from_inventory, name='inventory-sub'),
    path('auth/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', views.CustomTokenRefreshView.as_view(), name='token_refresh'),
]
