from . import views
from django.urls import path, include

urlpatterns = [
    path("",views.home, name= "home-url"),
    path("blog/", views.blog, name= "blog-url"),
    path("recommend/", views.recommend, name= "recommend-url"),
    path("auth/", include('auth.urls')),
]