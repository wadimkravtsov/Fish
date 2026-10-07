from django.shortcuts import render, redirect
from .models import CatSlider, Product, Basket
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

# Create your views here.
def aqua_base(request):
    slider_list = CatSlider.objects.all()
    products_list = Product.objects.all()
    context = {
        'title': 'Магазин аквариумистики "Panda"',
        'slider_list': slider_list,
        'products_list': products_list
    }
    return render(request, 'products/base.html', context)

def products(request, category_id=None):
    search_product = ""
    if request.GET.get('search_product'):
        search_product = request.GET.get('search_product')
    slider_list = CatSlider.objects.all()
    # cat_one = CatSlider.objects.get(id = category_id)

    if category_id:
        pr = Product.objects.filter(category_id=category_id, name__icontains=search_product)
    else:
        pr = Product.objects.filter(name__icontains=search_product)

    page = request.GET.get('page')
    result = 3
    paginator = Paginator(pr, result)

    try:
        pr = paginator.page(page)  # http://127.0.0.1:8000/projects/?page=2
    except PageNotAnInteger:
        page = 1
        pr = paginator.page(page)  # http://127.0.0.1:8000/projects/?page=fgdfgdfg
    except EmptyPage:
        page = paginator.num_pages
        pr = paginator.page(page)

    left_number = int(page) - 2
    if left_number < 1:
        left_number = 1

    right_number = int(page) + 3
    if right_number > paginator.num_pages:
        right_number = paginator.num_pages + 1

    pages_range = range(left_number, right_number)
    context = {
        'title': 'Магазин аквариумистики "Panda"',
        'slider_list': slider_list,
        'products_list': pr,
        'category_id': category_id,
        "paginator": paginator,
        "pages_range": pages_range
        # 'cat_one': cat_one
    }
    return render(request, 'products/products.html', context)

def product(request, pk):
    product_obj = Product.objects.get(id=pk)
    slider_list = CatSlider.objects.all()
    context = {
        'title': 'Магазин аквариумистики "Panda"',
        'slider_list': slider_list,
        'product': product_obj,
    }
    return render(request, 'products/product.html', context)

@login_required
def basket_add(request, product_id):
    current_page = request.META.get("HTTP_REFERER")
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return redirect(current_page)

    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return redirect(current_page)

def basket_minus(request, product_id):
    current_page = request.META.get("HTTP_REFERER")
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if baskets.exists():
        basket = baskets.first()
        if basket.quantity > 1:
            basket.quantity -= 1
            basket.save()
        else:
            basket.delete()
        return redirect(current_page)

def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META.get("HTTP_REFERER"))