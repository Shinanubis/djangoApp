from django.contrib import admin
from . import views
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

