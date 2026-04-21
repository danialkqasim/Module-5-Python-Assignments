from django.contrib import admin
from django.urls import path, include # Added include here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # This routes the home page to our blog app
]