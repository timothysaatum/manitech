from .views import IndexView, projectDetails, NewsDetails
from django.urls import path


urlpatterns = [
	path('', IndexView.as_view(), name='home'),
	path('news/details/<int:pk>/', NewsDetails.as_view(), name='news-details'),
	path('projects/details/<int:pk>/', projectDetails.as_view(), name='project-details')
]