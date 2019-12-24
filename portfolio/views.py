from django.shortcuts import render
from django.http import HttpResponse
from portfolio.models import port_projects
# Create your views here.

def index(request):

	Portfolios_querry = port_projects.objects.all()

	# for p in Portfolios_querry:
	# 	print(p.port_name)

	# portfolios = {'name' : Portfolios_querry.port_name,
	# 				'discription' : Portfolios_querry.port_description,
	# 				'img_path' : Portfolios_querry.port_image,
	# 				'date' : Portfolios_querry.port_date,
	# 				'client' : Portfolios_querry.port_clientname
	# 				}

	return render(request, 'portfolio.html', {'portfolios' : Portfolios_querry})

