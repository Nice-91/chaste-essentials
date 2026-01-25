from django.contrib import admin
from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Product


class ProductAdminForm(forms.ModelForm):
    image = CloudinaryFileField()

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm


admin.site.register(Product, ProductAdmin)
