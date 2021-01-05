from django.contrib import admin
from django.urls import path, include
from amazapp import views

urlpatterns = [
    path('idx/', views.idx),
    path('answer_list/', views.answer_list, name='answer_list'),
    path('answer3/', views.answer3, name='answer3'),
]
