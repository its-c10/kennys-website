from django.shortcuts import render
from .models import GalleryImage
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, "home/index.html", context={})


def contact(request):
    return render(request, "contact/contact.html", context={})


def services(request):
    return render(request, "services/services.html", context={})


def gallery(request, view_type="none"):

    view_type = request.GET.get("view_type")
    gallery_images = GalleryImage.objects.all()
    selected_gallery_images = []

    if view_type != None and view_type != "all":
        for image in gallery_images:
            detail_type = image.detail_type
            proper_detail_type_name = detail_type.lower().replace(" ", "_")
            if proper_detail_type_name == view_type:
                selected_gallery_images.append(image)
    else:
        selected_gallery_images = gallery_images

    context_dict = {"gallery": selected_gallery_images}
    return render(request, "gallery/gallery.html", context_dict)


def gallery_redirect(request):
    return gallery(request)