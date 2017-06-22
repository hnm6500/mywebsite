__author__ = 'moholkar.hrishikesh2'
from django.conf.urls import url
from .import views

urlpatterns = [
      url(r'^profile$',views.show_profile,name='profile'),
   # url(r'^KnowMe$',views.show_profile,name='profile'),
      url (r'^homepage$',views.homepage,name='homepage'),
       url (r'^project$',views.projectdetails,name='projectdetails'),
    url (r'^detail1$',views.detail1,name='detail1'),
    url (r'^detail2$',views.detail2,name='detail2'),
    url (r'^detail3$',views.detail3,name='detail3'),
    url (r'^detail4$',views.detail4,name='detail4'),
    url (r'^detail5$',views.detail5,name='detail5'),
    url (r'^detail6$',views.detail6,name='detail6'),
    url (r'^detail7$',views.detail7,name='detail7'),

    url(r'^Forum',views.get_message,name='Forum')

]
