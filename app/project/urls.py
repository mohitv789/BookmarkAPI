from django.urls import path,include
from project import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project',views.ProjectViewSet)
app_name='project'
urlpatterns=[
    path('',include(router.urls)),


]
