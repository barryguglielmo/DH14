#gettingstarted/urls.py
from django.conf.urls import include, url


from django.contrib import admin
admin.autodiscover()

import main.views

urlpatterns = [
    url(r'^$', main.views.index, name='index'),
    url(r'^db', main.views.db, name='db'),
	url(r'^Final_Project/', main.views.Final_Project, name = 'Final_Project'),
	url(r'^home/', main.views.home, name = 'home'),
	url(r'^stacked_line/', main.views.stacked_line, name = 'stacked_line'),
	url(r'^doughnut/', main.views.doughnut, name = 'doughnut'),
	url(r'^area/', main.views.area, name = 'area'),
	url(r'^about/', main.views.about, name = 'about'),

	]
