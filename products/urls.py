from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, AdminLoginView

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")

urlpatterns = [
    path("login/", AdminLoginView.as_view()),
    path("", include(router.urls)),
]
