from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('reg/',views.register,name="rg"),
	path('stdnt/',views.student,name="st"),
	path('stdup/<int:h>/',views.studup,name="stp"),
	path('stdl/<int:u>/',views.studlte,name="std"),
]