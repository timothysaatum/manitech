from django.contrib import admin

from .models import (
		HomeSection, 
		AboutSection, 
		WhyManitech, 
		ValueProposition, 
		ProductsSection, 
		Testimonies,
		NewsAndProjects, 
		Team, 
		Contact, 
		Gallery, 
		Project
	)


class HomeSectionAdmin(admin.ModelAdmin):

	list_display = ('id', 'title', 'content', 'image', 'video_link')


class AboutSectionAdmin(admin.ModelAdmin):

	list_display = ('id', 'image', 'content', 'value_proposition_1', 
		'value_proposition_2', 'value_proposition_3', 'assuarance', 
		'video_link', 'video_background')


class WhyManitechAdmin(admin.ModelAdmin):

	list_display = ('id', 'why_us')


class ValuePropositionAdmin(admin.ModelAdmin):

	list_display = ('id', 'header', 'short_notes')


class ProductsSectionAdmin(admin.ModelAdmin):

	list_display = ('id', 'category', 'image', 'short_notes', 'price')


class TestimoniesAdmin(admin.ModelAdmin):

	list_display = ('id', 'testimony', 'name_of_customer', 'occupation', 'rating')



class NewsAndProjectsAdmin(admin.ModelAdmin):

	list_display = ('id', 'title', 'content', 'image')

class TeamAdmin(admin.ModelAdmin):

	list_display = ('id', 'name', 'role', 'description', 'profile_image', 
		'facebook_url', 'x_url', 'instagram_url', 'linkedin_url')


class ContactAdmin(admin.ModelAdmin):

	list_display = ('id', 'name', 'occupation', 'email', 'subject', 'message', 'phone_number')


class GalleryAdmin(admin.ModelAdmin):

	list_display = ('id', 'image', 'alt')



class ProjectAdmin(admin.ModelAdmin):

	list_display = ('id', 'project_type', 'title', 'content')

admin.site.register(HomeSection, HomeSectionAdmin)
admin.site.register(AboutSection, AboutSectionAdmin)
admin.site.register(WhyManitech, WhyManitechAdmin)
admin.site.register(ValueProposition, ValuePropositionAdmin)
admin.site.register(ProductsSection, ProductsSectionAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Testimonies, TestimoniesAdmin)
admin.site.register(NewsAndProjects, NewsAndProjectsAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Project, ProjectAdmin)