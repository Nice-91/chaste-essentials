from rest_framework import serializers
from .models import Product
import cloudinary


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'description', 'image']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None
