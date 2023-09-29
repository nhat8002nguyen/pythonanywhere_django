from django.urls import path
from scraping_example import views

urlpatterns = [
	path('', view=views.get_file_format, name='get_name'),
	path('download/', views.download_file)
]
