from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminPage.as_view(), name='admin'),
    path('additem/', views.PostItem.as_view(), name='additem')
]