from django.urls import path
from user_profile import views

app_name = 'user_profile'

urlpatterns = [

    path('create/',views.CreateUserView.as_view(),name='create'),
    path('token/',views.CreateTokenView.as_view(),name='token'),
    path('me/',views.ManageUserView.as_view(),name='me'),
]
