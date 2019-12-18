from django.shortcuts import render
from django.http import HttpResponse
import mimetypes
# Create your views here.

def home(request):
        return render(request, 'index.html')


def dwnload_file(request):
	f_path = 'media/resume/ArtikBharoliya_resume.pdf'
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
