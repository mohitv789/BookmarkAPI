from django.urls import path
from user_profile import views

app_name = 'user_profile'

urlpatterns = [

    path('create/',views.CreateUserView.as_view(),name='create'),
    path('token/',views.CreateTokenView.as_view(),name='token'),
    path('me/',views.ManageUserView.as_view(),name='me'),
    path('posts/', views.PostList.as_view(),name="posts"),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('users/', views.UserList.as_view(),name="users"),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('', views.api_root),
    path('posts/<int:pk>/highlight/', views.PostHighlight.as_view()),
]
