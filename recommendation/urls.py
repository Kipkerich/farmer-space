# urls.py
from django.urls import path,include
from .import views
urlpatterns = [
    path("result/", views.result, name= "result-url"),
    path('submit_recommendation/', views.submit_recommendation_view, name='submit_recommendation'),
    
]
