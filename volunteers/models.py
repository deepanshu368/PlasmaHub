from django.db import models

# Create your models here.

class Donator(models.Model):
	username=models.CharField(max_length=100,default="")
	email=models.CharField(max_length=100,default="")
	adhar_no = models.CharField(max_length=100, primary_key=True, default="Noaddharnumber")
	dob = models.CharField(max_length=100,default="")

	first_name= models.CharField(max_length=100,default="")
	last_name= models.CharField(max_length=100,default="")

	age = models.CharField(max_length=100,default="")
	sex = models.CharField(max_length=100,default="")

	address = models.TextField()
	district = models.CharField(max_length=100, default='Delhi')

	pin = models.IntegerField()
	mob=models.CharField(max_length=100)

	blood_grp=models.CharField(max_length=100, default="")
	weight = models.IntegerField(default="")

	diabetic = models.CharField(max_length=100,default="")
	disease = models.CharField(max_length=100,default="")
