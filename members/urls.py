from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('git', views.git),
    path('gugu', views.gu),
    path('test', views.test),
    path('signup', views.signup),
    path('login',views.login),
    path('logout', views.logout),
    path('members', views.login_after),
    
]
