from django.shortcuts import render
from django.http import FileResponse
import os

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def sitemap_view(request):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sitemap.xml')  # Adjust path if needed
    return FileResponse(open(file_path, 'rb'), content_type='application/xml')

