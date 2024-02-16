
from django.contrib import admin
from django.urls import path
from app import views
# urls.py

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('aboutUs/', views.aboutUs),
    path('course/', views.course),
    path('course/<str:courseid>', views.courseDetails),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

