from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .forms import OrderForm
from products.models import CatSlider
from django.urls import reverse_lazy
from .models import Order

class OrderCreateView(CreateView):
    slider_list = CatSlider.objects.all()
    form_class = OrderForm
    template_name = 'orders/order-create.html'
    success_url = reverse_lazy('order-create')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Store - Оформление заказа"
        # context['slider_list'] = "slider_list"
        return context

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)

# Create your views here.
