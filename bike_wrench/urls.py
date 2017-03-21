from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^bike/', include('bike.urls', namespace='bike')),
    url(r'^$', TemplateView.as_view(template_name='users/index.html'), name='index'),
]
