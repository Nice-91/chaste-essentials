from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)  # <-- Use ImageField here

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'description', 'image']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.image:
            rep['image'] = instance.image.url
        else:
            rep['image'] = None
        return rep
