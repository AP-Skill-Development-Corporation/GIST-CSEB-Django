"""CSEBProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DemoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('h/',views.demo),
    path('k/<str:v>/',views.sample),
    path('q/<str:h>/<int:y>/',views.nme),
    path('v/<str:b>/',views.naveen),
    path('a/<str:e>/<int:h>/',views.color),
    path('p/',views.jk),
    path('r/',views.pyk),
    path('kw/<str:y>/',views.four),
    path('zy/',views.bjk),
    path('jk/<str:b>/',views.hyk),
    path('gb/<str:ab>/<str:bd>/<int:cd>/',views.surya),
    path('rg/',views.reg),

]





