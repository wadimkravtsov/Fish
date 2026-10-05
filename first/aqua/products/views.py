from django.shortcuts import render
from .models import CatSlider, Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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