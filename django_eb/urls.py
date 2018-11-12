from django.conf.urls import include, url
from django.contrib import admin
from smarturls import surl

from blog.views import BlogAPIView

urlpatterns = [
    surl('admin/', include(admin.site.urls)),
    surl('blog/', BlogAPIView.as_view(), name='blog')
]
