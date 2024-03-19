from django.contrib import admin
from django.urls import path, include
from Kasirmini import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('Menu/', include('Menu.urls')),
]
