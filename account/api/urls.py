from django.urls import path

from account.api import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('user/', views.ManageUser.as_view(), name='manage_user  ')
    # path('user/', views.manage_user, name='manage_user  ')
]
