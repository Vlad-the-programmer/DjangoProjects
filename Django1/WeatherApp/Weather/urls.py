
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('delete/<str:pk>', views.DeletePosts.as_view(), name='delete_post'),
    ]
