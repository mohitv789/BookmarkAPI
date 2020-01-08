from django.urls import path,include
from project import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project',views.ProjectViewSet,basename="PROJECTS")

urlpatterns=[
    path('',include(router.urls)),
]
