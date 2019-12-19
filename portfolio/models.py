from django.db import models
from datetime import datetime 
# Create your models here.

class Resume(models.Model):
	res_version_name = models.CharField(max_length = 30)
	resume_file = models.FileField(upload_to = "reume")
	res_date =  models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.res_version_name