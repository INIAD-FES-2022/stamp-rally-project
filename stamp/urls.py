from . import views
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.views import LoginView, LogoutView
from pathlib import Path
import os, environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Get env
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get('DJANGO_DEBUG') == 'True' else False

urlpatterns = [
    path('', views.redirect_stamp.as_view(), name='redirect'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("stamp/", views.stamp.as_view(), name="stamp"),
    path("stamp/get/<str:sponser>/", views.stamp_get.as_view(), name="stamp_get"),
    path("stamp/map/", views.stamp_map.as_view(), name="stamp_map"),
]
if DEBUG:
    urlpatterns[-1] = path('test/', views.my_test_500_view, name='test')
