from django.db import models
from datetime import datetime 
# Create your models here.

class Resume(models.Model):
	res_version_name = models.CharField(max_length = 30)
	resume_file = models.FileField(upload_to = "reume")
	res_date =  models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.res_version_name



#model for the PortfolioProjects


class port_projects(models.Model):

	port_id = models.AutoField(primary_key=True)
	port_name = models.CharField(max_length = 50)
	port_date = models.DateField()
	port_description = models.TextField()
	port_image = models.ImageField(upload_to = 'portfolioimages')
	port_clientname = models.CharField(max_length = 50)

	def __str__(self):
		return self.port_name

