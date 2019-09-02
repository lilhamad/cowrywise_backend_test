from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('groups', views.GroupView)
router.register('users', views.UserView)
router.register('payment', views.PaymentView)
router.register('group_search', views.GroupSearchView)

urlpatterns = [
    path('', include(router.urls)),
    path('api/login/', views.login),
    path('api/sampleapi/', views.sample_api),
    path('api-auth/', include('rest_framework.urls'))
]