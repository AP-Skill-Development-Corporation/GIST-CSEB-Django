from django.urls import path
from . import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('about/',views.about,name="ab"),
	path('reg/',views.register,name="rg"),
	path('lgn/',ad.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('lgou/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
]