from django.db import models

class CatSlider(models.Model):
    cat_name = models.CharField(max_length=200, verbose_name="Название")
    cms_img = models.ImageField(upload_to='cat_img/', verbose_name="Изображение")
    cms_title = models.CharField(max_length=200, verbose_name="Заголовок")
    cms_text = models.CharField(max_length=200, verbose_name='Текст')
    cms_css = models.CharField(max_length=20, default='-', verbose_name='CSS класс')

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название товара")
    image = models.ImageField(upload_to="products_images/", blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name="Описание")
    short_description = models.CharField(max_length=100, blank=True, verbose_name="Краткое описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(CatSlider, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    add_photo = models.ImageField(upload_to="products_images/add/", blank=True, verbose_name='Фото')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'