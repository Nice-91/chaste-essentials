from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'description', 'image']

    def get_image(self, obj):
        if obj.image:
            try:
                # Use obj.image.url directly if available
                return obj.image.url
            except Exception as e:
                print(f"Cloudinary error: {e}")
                return None
        return None
