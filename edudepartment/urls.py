from django.urls import path
from.import views

urlpatterns = [
	path('',views.index,name='index'),
	path('about',views.about,name='about'),
	path('services',views.services,name='services'),
	path('gallery',views.gallery, name='gallery'),
	path('contact',views.contact,name='contact'),
	path('feedback',views.feedback,name='feedback'),
	path('vision',views.vision,name='vision'),
	path('mision',views.mision,name='mision'),
]