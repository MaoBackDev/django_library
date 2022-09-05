from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.authors.urls')),
    path('', include('apps.books.urls')),
    path('', include('apps.loans.urls')),
]
