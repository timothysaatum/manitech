from django.shortcuts import render
from django.views.generic import (
		TemplateView, 
		ListView,
		DetailView
	)
from .models import (
		HomeSection, 
		AboutSection, 
		WhyManitech, 
		Gallery, 
		ProductsSection, 
		Testimonies, 
		NewsAndProjects, 
		Team, 
		Contact,
		Project
	)


class IndexView(TemplateView):
	template_name = 'backend/index.html'

	def get_context_data(self, **kwargs):

		context = super(IndexView, self).get_context_data(**kwargs)
		context['homedata'] = HomeSection.objects.all().first()
		context['aboutdata'] = AboutSection.objects.all().first()
		context['manitech'] = WhyManitech.objects.all().first()
		context['testimonies'] = Testimonies.objects.all()[:4]
		context['news_and_projects'] = NewsAndProjects.objects.all()[:3]
		context['team_members'] = Team.objects.all()
		context['gallery'] = Gallery.objects.all()[:8]
		context['social_project'] = Project.objects.get(project_type='Social')

		return context



class projectDetails(DetailView):

	model = Project
	slug_url_kwarg = 'slug'
	template_name = 'backend/details.html'
	context_object_name = 'project'

class NewsDetails(DetailView):

	model = NewsAndProjects
	slug_url_kwarg = 'slug'
	template_name = 'backend/details.html'
	context_object_name = 'news'