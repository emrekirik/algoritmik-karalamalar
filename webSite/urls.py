from django.contrib import admin
from django.urls import include, path
from blogSitesi import views
from django.conf.urls import url
from django.template import loader

urlpatterns = [
    path('blogSitesi/', include('blogSitesi.urls')),
    path('admin/', admin.site.urls),
    url(r'^$', views.gonderi_listesi, name='gonderi_listesi'),
]