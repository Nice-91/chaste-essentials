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
            try:
                # Generate the Cloudinary URL dynamically from the public_id
                url, _ = cloudinary.utils.cloudinary_url(obj.image.public_id)
                return url
            except Exception as e:
                print(f"Cloudinary error: {e}")
                return None
        return None
