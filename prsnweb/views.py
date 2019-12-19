from django.shortcuts import render
from django.http import HttpResponse
from portfolio.models import Resume
import mimetypes
# Create your views here.

def home(request):
        return render(request, 'index.html')


def contact(request):
	return render(request, 'contact.html')

def about(request):
	return render(request, 'about.html')

def dwnload_file(request):

	latest_resume = Resume.objects.latest('res_date')

	f_path = latest_resume.resume_file.path
	filename = 'ArtikBharoliya_resume.pdf'

	f1 = open(f_path, 'rb')
	mime_type = mimetypes.guess_type(f_path)
	print(mime_type)
	response = HttpResponse(f1, content_type = mime_type)
	# print('\n\n\n\n\n\n\n\n\n\n')
	# print('\n\n\n\n\n\n\n\n\n\n')
	
	# print(mime_type)
	# print(response)
	# print('\n\n\n\n\n\n\n\n\n\n')
	# print('\n\n\n\n\n\n\n\n\n\n')
	
	response['Content-Disposition'] = "attachment; filename=%s"% filename
	return response
