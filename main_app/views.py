from django.shortcuts import render
from .models import GalleryImage
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, "index.html", context={})


def contact(request):
    return render(request, "contact.html", context={})


def gallery(request, view_type="none"):

    view_type = request.GET.get("view_type")
    gallery_images = GalleryImage.objects.all()
    selected_gallery_images = []

    if view_type != None and view_type != "all":
        for image in gallery_images:
            print("VIEW TYPE", view_type)

            detail_type = image.detail_type
            proper_detail_type_name = detail_type.lower().replace(" ", "_")
            print("DETAIL TYPE", proper_detail_type_name)
            if proper_detail_type_name == view_type:
                selected_gallery_images.append(image)
    else:
        selected_gallery_images = gallery_images

    context_dict = {"gallery": selected_gallery_images}
    return render(request, "gallery.html", context_dict)


def gallery_redirect(request):
    return gallery(request)