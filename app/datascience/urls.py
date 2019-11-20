from django.urls import path,include
from datascience import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('datascience',views.MachineLearningModelViewSet)
app_name='datascience'
urlpatterns=[
    path('',include(router.urls)),


]
