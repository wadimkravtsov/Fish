from django.contrib import admin
from .models import CatSlider, Product, Photo, Basket
from django.utils.safestring import mark_safe



class PhotoAdd(admin.StackedInline):
    model = Photo
    fields = ('product', 'add_photo')
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_image', 'category', 'price', 'quantity')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    inlines = [PhotoAdd]
    fields = ('id', 'name', 'image', 'get_html_image_big', 'category', 'price', 'quantity')
    readonly_fields = ('id', 'get_html_image_big')

    def get_html_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='70'>")

    def get_html_image_big(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='300'>")

    get_html_image.short_description = "Миниатюра"
    get_html_image_big.short_description = "Миниатюра"



class PhotoAdmin(admin.ModelAdmin):
    list_display = ('product', 'add_photo')

admin.site.register(CatSlider)
admin.site.register(Product,ProductAdmin)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(Basket)