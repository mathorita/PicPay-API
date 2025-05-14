from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from picpay.views import UserViewSet,TransactionViewSet

router = routers.DefaultRouter()
router.register('user',UserViewSet,basename='Users')
router.register('transaction',TransactionViewSet,basename='Transactions')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
