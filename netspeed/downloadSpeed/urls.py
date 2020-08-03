from django.conf.urls import url
from .import views

urlpatterns = [
    url('',views.downloadSpeed),
    url('getSpeed',views.showSpeed),
]

#  background-image: url( '/static/img/bg.jpg' );