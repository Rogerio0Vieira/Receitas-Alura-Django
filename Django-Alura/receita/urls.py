import addreceita
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('addreceita.urls')),
    path('admin/', admin.site.urls),
]
