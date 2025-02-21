from django.contrib import admin

from carts.admin import CartUserAdmin
from orders.admin import OrderTabularAdmin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'first_name', 'last_name', 'email')

    inlines = (CartUserAdmin, OrderTabularAdmin)
