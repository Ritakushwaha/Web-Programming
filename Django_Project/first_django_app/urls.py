from django.urls import path
# from Django_Project.first_django_app import views
# is same as below import
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rita", views.rita, name="rita"),
    path("girwar", views.girwar, name="girwar")
]