from django.db import models
from django.utils import timezone




class BaseModel(models.Model):

	date_added = models.DateField(auto_now_add=True)
	date_modified = models.DateField(auto_now=True)

	class Meta:
		abstract = True



class HomeSection(BaseModel):

	title = models.CharField(max_length=100)
	content = models.CharField(max_length=150)
	image = models.ImageField(upload_to='manitech/images')
	video_link = models.URLField()

	def __str__(self):

		return self.title



class AboutSection(BaseModel):

	image = models.ImageField(upload_to='manitech/images')
	content = models.CharField(max_length=150)
	value_proposition_1 = models.CharField(max_length=130)
	value_proposition_2 = models.CharField(max_length=130)
	value_proposition_3 = models.CharField(max_length=130)
	assuarance = models.CharField(max_length=300)
	video_link = models.URLField()
	video_background = models.ImageField(upload_to='manitech/images')

	def __str__(self):
		return self.content



class WhyManitech(BaseModel):

	why_us = models.TextField()

	class Meta:
		verbose_name_plural = 'Why Manitech'



class ValueProposition(models.Model):
	header = models.CharField(max_length=50)
	short_notes = models.CharField(max_length=100)

	def __str__(self):
		return self.header



class ProductsSection(BaseModel):
	TYPES = [
		('Cassava Flour', 'Cassava Flour'),
		('Animal Feed', 'Animal Feed'),
		('Cassava Starch', 'Cassava Starch')
	]

	category = models.CharField(choices=TYPES, max_length=100)
	image = models.ImageField(upload_to='manitech/images')
	short_notes = models.CharField(max_length=50)
	price = models.FloatField()

	def __str__(self):
		return self.category



class Testimonies(BaseModel):

	testimony = models.CharField(max_length=250)
	name_of_customer = models.CharField(max_length=150)
	occupation = models.CharField(max_length=150)
	rating = models.PositiveIntegerField()
	profile_image = models.ImageField(upload_to='manitech/images', default='avatar.png')


	class Meta:
		verbose_name_plural = 'Testimonies'

	def __str__(self):
		return self.name_of_customer



class NewsAndProjects(BaseModel):

	image = models.ImageField(upload_to='manitech/images')
	title = models.CharField(max_length=100)
	content = models.TextField()
	

	class Meta:
		verbose_name_plural = 'News And Projects'

	def __str__(self):
		return self.title




class Team(BaseModel):

	name = models.CharField(max_length=150)
	role = models.CharField(max_length=120)
	description = models.CharField(max_length=150)
	profile_image = models.ImageField(upload_to='manitech/images')
	facebook_url = models.URLField()
	x_url = models.URLField()
	instagram_url = models.URLField()
	linkedin_url = models.URLField()

	def __str__(self):
		return self.name



class Contact(BaseModel):

	name = models.CharField(max_length=150)
	occupation = models.CharField(max_length=150)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField()
	phone_number = models.CharField(max_length=150)


	def __str__(self):
		return self.name



class Gallery(BaseModel):

	image = models.ImageField(upload_to='manitech/images')
	alt = models.CharField(max_length=100, default='gallery image')

	class Meta:
		verbose_name_plural = 'Gallery'


	def __str__(self):
		return self.alt



PROJECTYPE = [
	('Social', 'Social')
]


class Project(models.Model):

	project_type = models.CharField(max_length=100, choices=PROJECTYPE)
	title = models.CharField(max_length=155)
	content = models.TextField()

	def __str__(self):
		return self.title