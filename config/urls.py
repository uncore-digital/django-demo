from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
]
## This will return the proper URL pattern for serving static files to your already defined pattern list. Use it like this:
## https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/
urlpatterns += staticfiles_urlpatterns()