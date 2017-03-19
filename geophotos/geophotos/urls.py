"""geophotos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from photobase import views
from geophotos import settings

from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/sitedocs/$', views.SiteDocView.as_view()),
    url(r'^v1/images/$', views.ImageView.as_view()),
    url(r'^upload/plans/$', views.TestView2.as_view()),
    url(r'^confirm/plans/$', views.TestView3.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
