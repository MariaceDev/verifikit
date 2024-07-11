from django.contrib import admin
from django.urls import path
from. import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.process_url, name='process_url'),
    path('process_api/', views.process_api, name='process_api'),
]
