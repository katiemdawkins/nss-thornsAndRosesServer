"""thornsNRoses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from thornsNRosesAPI.views.distributor_view import DistributorView
from thornsNRosesAPI.views import login_user, register_user
from thornsNRosesAPI.views.flower_view import FlowerView
from thornsNRosesAPI.views.nurseryFlowerPrice_view import NurseryFlowerPriceView
from thornsNRosesAPI.views.nursery_view import NurseryView
from thornsNRosesAPI.views.retailer_view import RetailerView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'flowers', FlowerView, 'flower')
router.register(r'nurseries', NurseryView, 'nursery')
router.register(r'distributors', DistributorView, 'distributor')
router.register(r'retailers', RetailerView, 'retailer')
router.register(r'nurseryFlowerPrices', NurseryFlowerPriceView, 'nurseryFlowerPrice')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]
