from django.urls import path
from clara import views

urlpatterns = [
    path('', views.index, name='My_index'),
    path('about/', views.about, name='My_about'),
    path('contact/', views.contact, name='My_contact us')
]
