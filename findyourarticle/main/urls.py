from django.conf.urls import url
from findyourarticle.main import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
