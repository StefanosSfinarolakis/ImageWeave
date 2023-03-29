from django.urls import path
from social import views

urlpatterns = [
    path('<str:pk>', views.profile, name='profile'),
    path('follow', views.follow, name='follow')
]