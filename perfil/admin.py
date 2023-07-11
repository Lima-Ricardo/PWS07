from django.contrib import admin
from .models import Conta, Categoria
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Conta)