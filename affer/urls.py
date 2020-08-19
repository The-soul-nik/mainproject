from django.urls import path
from .views import *
from .import views

app_name = "affer"


urlpatterns = [
    path('taga/',  views.tags_list, name="tags_list_url"),
    path('taga/<str:slug>/', views.tags_detail, name="tags_detail_url"),
    path('tags/', views.tags_list, name="tags_list_url"),
    path('tag/create', TagCreate.as_view(), name="tag_create_url"),


]
