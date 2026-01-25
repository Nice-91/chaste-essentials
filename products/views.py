from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Product
from .serializers import ProductSerializer


# ======================
# ADMIN LOGIN
# ======================
class AdminLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"message": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"message": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Optional: restrict to staff/superuser
        if not user.is_staff:
            return Response(
                {"message": "You are not allowed to access admin"},
                status=status.HTTP_403_FORBIDDEN
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "username": user.username,
                "is_staff": user.is_staff,
            },
            status=status.HTTP_200_OK
        )


# ======================
# PRODUCTS
# ======================
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("-id")
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        """
        ✅ Public users: READ (GET)
        🔒 Admin only: CREATE / UPDATE / DELETE
        """
        if self.request.method in ["GET", "HEAD", "OPTIONS"]:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        queryset = Product.objects.all().order_by("-id")

        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category=category)

        return queryset
