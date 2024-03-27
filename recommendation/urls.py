# urls.py
from django.urls import path,include
from .views import my_view
from .views import submit_recommendation_view
urlpatterns = [
    path("result/", my_view, name= "result-url"),
    path('submit_recommendation/', submit_recommendation_view, name='submit_recommendation'),
]
