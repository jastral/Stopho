from django.urls import path
from . import views
#from django.contrib.auth.views import login

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path(r'^(?P<image_slug>[-\w]+)/$', views.image_list, name='image_list'),
    # path(r'^(?P<id>[-\w]+)/(?P<slug>[-\w]+)/$', views.image_detail, name='image_detail'),
    path('search/',views.search),
]
