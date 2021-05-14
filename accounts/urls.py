
from django.urls import path,include
from . import views

urlpatterns=[
	path('register', views.register,name='register'),
	path('login', views.login , name='login'),
	path('Org_Register', views.Org_Register, name='Org_Register'),

	path('logout', views.logout, name='logout')

]


