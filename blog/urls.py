from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="blogIndex"),
    # ex: /articles/5/
    path('article/<int:article_id>/', views.detail, name='blogDetail'),
]