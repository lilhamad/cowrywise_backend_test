from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('groups', views.GroupView)
router.register('users', views.UserView)
router.register('group_search', views.GroupSearchView)
router.register('login', views.login)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]