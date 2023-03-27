
from django.urls import path
from . import views

urlpatterns = [
path('',views.trending, name='trending'),
path('home', views.index, name='index'),
path('settings', views.settings, name='setting'),
path('signup', views.signup, name='signup'),
path('signin', views.signin, name='signin'),
path('logout', views.logout, name='logout'),

]