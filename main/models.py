from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
	first_name  = models.CharField(max_length=100)
	last_name   = models.CharField(max_length=100)
	username 	= models.CharField(max_length=100)

	phone_number = models.CharField(max_length=20, null=True, blank=True)
	email 		= models.EmailField(unique=True)
	profile_picture = models.ImageField(default='heart.png', null=True, blank=True, upload_to='profile')

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ["first_name", "last_name", "username"]
	
	def __str__(self):
		return self.first_name+ " "+self.last_name

	class Meta:
		ordering = ['first_name']




class Student(models.Model):
	added_by = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200)
	last_name  = models.CharField(max_length=200)

	student_department= models.CharField(max_length=200)
	registered_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name+ " "+self.last_name


class News(models.Model):
	added_by = models.ForeignKey(User, on_delete=models.CASCADE)
	title    = models.CharField(max_length=200)
	body     = models.TextField()
	like     = models.ManyToManyField(Student, blank=True, null=True)
	added_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
		
	class Meta:
		ordering = ['-added_at']

class Department(models.Model):
	added_by = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name