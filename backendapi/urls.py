from django.contrib import admin
from django.urls import path
from authApp.views import  SignUpAPI, LoginAPI, LogoutAPI
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static


urlpatterns = [
    path('admin', admin.site.urls),
    path('api/signup', SignUpAPI.as_view(), name='api-signup'),
    path('api/login', LoginAPI.as_view(), name='api-login'),
    path('api/logout', LogoutAPI.as_view(), name='api-logout'),
    path('api/', include('cars.urls')),
    path('api/', include('bookings.urls')),
]


