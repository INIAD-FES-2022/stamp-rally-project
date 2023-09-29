from . import views
from django.urls import path

urlpatterns = [
    path("", views.redirect_stamp.as_view(), name="redirect"),
    path("stamp/", views.stamp.as_view(), name="stamp"),
]