from django.db import models

# ✅ DEFINE THIS FIRST
CATEGORY_CHOICES = [
    ("men", "Men"),
    ("women", "Women"),
    ("beauty", "Beauty"),
    ("accessories", "Accessories"),
]


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name
