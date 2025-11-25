from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from app.forms import CustomUserCreationForm, ProductForm, PurchaseForm
from app.models import product, purchase
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = '/'

class ProductCreateView(CreateView):
    model = product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = '/home/'

# def product_list(request):
#     products = product.objects.all()
#     return render(request, 'product_list.html', {'products': products})
class ProductListView(ListView):
    model = product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PurchaseForm()
        return context


class PurchaseCreateView(CreateView):
    model = purchase
    form_class = PurchaseForm
    template_name = 'product_list.html'
    success_url = '/home/'

# def create_purchase(request):
#     if request.method == "POST":
#         product_id = request.POST.get('product_id')
#         day = request.POST.get('day')
#         month = request.POST.get('month')
#         year = request.POST.get('year')

#         product_ = get_object_or_404(product, id=product_id, is_available=True)

#         # Optional: Prevent duplicate purchase
#         if purchase.objects.filter(
#             user=request.user,
#             product=product_,
#             purchase_date=day,
#             purchase_month=month,
#             purchase_year=year
#         ).exists():
#             messages.error(request, "You already purchased this on that date.")
#             return redirect('product-list')

#         purchase.objects.create(
#             product=product_,
#             user=request.user,
#             purchase_date=int(day),
#             purchase_month=month,
#             purchase_year=int(year)
#         )

#         messages.success(request, f"Successfully purchased {product_.name}!")
#         return redirect('product-list')  # or wherever you list products

#     return redirect('product-list')

#api endpoints
def product_list_api(request):
    products = product.objects.all().values()
    return JsonResponse(list(products), safe=False)

def purchase_list_api(request):
    purchases = purchase.objects.select_related("user", "product")

    data = []

    for p in purchases:
        data.append({
            # PURCHASE FIELDS
            "id": p.id,
            "purchase_date": p.purchase_date,
            "purchase_month": p.purchase_month,
            "purchase_year": p.purchase_year,
            "province": p.province,
            "contact": p.contact,
            "status": p.status,
            "last_digits": p.last_digits,
            "shipping_address": p.shipping_address,

            # USER FIELDS (SAFE FIELDS ONLY)
            "user": {
                "id": p.user.id,
                "username": p.user.username,
                "first_name": p.user.first_name,
                "last_name": p.user.last_name,
                "email": p.user.email,
                "is_staff": p.user.is_staff,
                "is_active": p.user.is_active,
                "date_joined": p.user.date_joined,
            },

            # PRODUCT FIELDS
            "product": {
                "id": p.product.id,
                "name": p.product.name,
                "description": p.product.description,
                "price": p.product.price,
                "discounted_price": p.product.discounted_price,
                "is_available": p.product.is_available,
                "status": p.product.status,
                "category": p.product.category,
                "sku": p.product.sku,
                "stock": p.product.stock,
                "image_url": request.build_absolute_uri(p.product.image.url) if p.product.image else None,
            }
        })

    return JsonResponse(data, safe=False)
