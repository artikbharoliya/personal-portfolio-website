
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


from . import settings
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('portfolio/', include('portfolio.urls')),
    path('download_resume', views.dwnload_file),
    path('contact', views.contact),
    path('about', views.about)
]
