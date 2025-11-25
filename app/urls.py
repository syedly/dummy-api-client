from django.contrib.auth.views import LoginView
from django.urls import path
from .views import home, RegisterView, ProductCreateView, product_list_api, ProductListView, purchase_list_api, PurchaseCreateView #create_purchase, product_list
# 
urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', home, name='home'),
    path('product-create/', ProductCreateView.as_view(), name='product-create'),
    # path('products/', product_list, name='product-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('purchase/create/', PurchaseCreateView.as_view(), name='create_purchase'),
    # path('purchase/create/', create_purchase, name='create_purchase'),
    #api endpoints
    path('api/products/', product_list_api, name='product-list-api'),
    path('api/purchase/', purchase_list_api, name='purchase-list-api'),
]