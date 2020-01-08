from django.urls import path,include
from post import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post',views.PostViewSet,basename="POST")
app_name='post'
urlpatterns=[
    path('',include(router.urls)),


]
