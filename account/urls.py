
from django.urls import path
from . import views

urlpatterns = [
path('',views.startpage, name='startpage'),
path('home', views.index, name='index'),
path('settings', views.settings, name='settings'),
path('signup', views.signup, name='signup'),
path('signin', views.signin, name='signin'),
path('logout', views.logout, name='logout'),
path('aboutus', views.aboutus, name='aboutus'),
path('testpage', views.testpage, name='testpage'),
]