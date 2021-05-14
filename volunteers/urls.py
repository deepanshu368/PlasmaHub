
from django.urls import path,include
from . import views


urlpatterns = [
	path('feeddata', views.feeddata ,name='feeddata'),
	path('show_info', views.show_info, name='show_info')

]

