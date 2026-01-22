from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=0   # 👈 IMPORTANT: no .00
    )

    class Meta:
        model = Product
        fields = ["id", "name", "price", "category", "description", "image"]
