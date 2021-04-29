from django.shortcuts import render
from .models import GalleryImage
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, "index.html", context={})


def contact(request):
    return render(request, "contact.html", context={})


def gallery(request):
    gallery_images = GalleryImage.objects.all()
    template = loader.get_template("gallery.html")
    context_dict = {"gallery": gallery_images}
    return HttpResponse(template.render(context_dict, request))
