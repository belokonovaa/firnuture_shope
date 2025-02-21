from django.contrib import admin

from products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'quantity', 'price', 'discount')
    list_editable = ('discount',)
    search_fields = ('name', 'description')
    list_filter = ('discount', 'quantity', 'category')
    fields = (
        ('name', 'quantity'),
        'category',
        'slug',
        'description',
        ('price', 'discount'),
        'image',
    )

