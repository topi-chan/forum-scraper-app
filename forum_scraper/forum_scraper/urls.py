from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forumscraper.urls')),
    path('advanced/', include('advanced_forumscraper.urls')),
]
