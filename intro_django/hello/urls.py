from django.urls import path
from . import views

# all the urls in your django application

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("emmanuel", views.emmanuel, name="emmanuel")
]