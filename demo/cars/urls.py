from django.conf.urls import url, include
from cars import views

urlpatterns = [
    url(r'^login/$', views.user_login),
    url(r'^logout/$', views.user_logout),
    url(r'^register/$', views.register),
    url(r'^search/', views.search_form),
    url(r'^search-results/', views.search),
    url(r'^profile/', views.profile),
    url(r'^compare/', views.compare),
    url(r'^404/', views.error404),
    url(r'^500/', views.error500),
    url(r'^about/', views.aboutus),
    url(r'^game/', views.game),
    url(r'^frame/', views.frame),
    url(r'^dealer-admin/$', views.admin_render),
    # url(r'^cars/(?P<slug>[\w\-]+)/', views.)
    url(r'^cars/(?P<manufacturer>[\w\-]+)/(?P<slug>[\w-]+)/$', views.car_details),
]