#main/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Final_Project/', views.Final_Project, name='Final_Project'),
	url(r'^home/', views.home, name='home'),
	url(r'^stacked_line/', views.stacked_line, name='stacked_line'),
	url(r'^area/', views.area, name='area'),
	url(r'^about/', views.about, name='about'),

]
