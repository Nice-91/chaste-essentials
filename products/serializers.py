from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)  # Accept image uploads

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'description', 'image']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['image'] = instance.image.url if instance.image else None
        return ret
