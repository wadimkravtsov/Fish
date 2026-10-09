from django.contrib import admin
from .models import Order

class OrderAdm(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = ('id', 'status', 'created',
              ('first_name', 'last_name'),
              ('email', 'address'),
              'basket_history', 'initiator')
    readonly_fields = ('id', 'created')

admin.site.register(Order,OrderAdm)

# Register your models here.
