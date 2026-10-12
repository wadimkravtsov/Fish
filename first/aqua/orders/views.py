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
    success_url = reverse_lazy('full-order')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Store - Оформление заказа"
        # context['slider_list'] = "slider_list"
        return context

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)

def full_order(request):
    order = Order.objects.all().order_by('created').last()
    order.update_after_payment()
    return render(request, 'orders/success.html')

class OrderListView(ListView):
    model = Order
    template_name = 'orders/orders.html'
    ordering = ("-created",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Store - Заказы"
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(initiator=self.request.user)

class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order.html'
    # context_object_name = 'obj11111'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Store - Заказ #{self.object.id}"
        return context

# Create your views here.
