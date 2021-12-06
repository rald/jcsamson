from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path('contactus/', include('contactus.urls')),
    path('admin/', admin.site.urls),
]
