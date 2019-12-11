"""mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from poleplanner import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^map/', views.get_map,name='check'),
    url(r'^map/', views.get_data,name='check'),
    url(r'^poleplanner/', views.get_poleplanner),

    #url(r'^get_result/(?P<news_id>.+)/$',views.get_result,name="image"),
    #url(r'^map/(?P<news_id>.+)/$',views.get_data,name="image"),
]
