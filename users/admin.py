from django.contrib import admin
from .models import User
from products.admin import BasketAdmin
# Register your models here.

@admin.register(User)
class UsrerAdmin(admin.ModelAdmin):
    list_display = ('username', )
    inlines = (BasketAdmin,)

