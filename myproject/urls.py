
from django.contrib import admin
from django.urls import path
from .views import login, sample_api
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', login),
    path('api/sampleapi', sample_api),
    path('todoapis/v1/', include('todoapis.urls')),

]
