from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cadastro/', include('cadastro.urls')),
    path('admin/', admin.site.urls),
]