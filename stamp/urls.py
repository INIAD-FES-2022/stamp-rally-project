from . import views
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.redirect_stamp.as_view(), name='redirect'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("stamp/", views.stamp.as_view(), name="stamp"),
]