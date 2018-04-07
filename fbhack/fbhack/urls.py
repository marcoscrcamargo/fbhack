"""fbhack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserViewSet.as_view()),
    url(r'^skill/$', views.SkillList.as_view()),
    url(r'^skill/(?P<pk>[0-9]+)/$', views.SkillwSet.as_view()),
    url(r'^question/$', views.QuestionList.as_view()),
    url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionViewSet.as_view()),
    url(r'^chat/$', views.ChatList.as_view()),
    url(r'^chat/(?P<pk>[0-9]+)/$', views.ChatViewSet.as_view()),
]
