"""PhilsNotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from PhilsNotesApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.joblist, name="joblist"),
    url(r'^jobnotes/(?P<job_id>\d+)/$', views.jobnotes, name="jobnotes"),
    url(r'^jobnotes/(?P<job_id>\d+)/savenote/$', views.savenote, name="savenote"),
    url(r'^jobedit/(?P<pk>\d+)/$', views.jobedit, name="jobedit"),
    url(r'^jobdelete/(?P<pk>\d+)', views.jobdelete, name="jobdelete"),
    url(r'^jobadd/$', views.jobadd, name="jobadd"),
    url(r'^builderadd/$', views.builder_add, name="builder_add"),
    url(r'^builderedit/(?P<pk>\d+)/$', views.builder_edit, name="builder_edit"),
    url(r'^builders/', views.builder_list, name='builder_list'),
    url(r'^builderdelete/(?P<pk>\d+)/$', views.builder_delete, name='builder_delete'),

]
