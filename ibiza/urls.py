

from django.urls import path
from ibiza import views

app_name = 'ibiza'

urlpatterns=[
	path('', views.home, name='home'),
	path('blog/', views.blog, name='blog'),
	]