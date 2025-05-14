from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from picpay.views import UserViewSet,TransactionViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('users',UserViewSet,basename='Users')
router.register('transactions',TransactionViewSet,basename='Transactions')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
