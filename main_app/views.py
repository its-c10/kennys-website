from django.shortcuts import render
from .models import GalleryImage
from .models import Service
from .forms import ContactForm

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def index(request):
    return render(request, "home/index.html", context={})


# def contact(request):
#     return render(request, "contact/contact.html", context={})


def services(request):
    services = Service.objects.all()
    context_dict = {"services": services}
    return render(request, "services/services.html", context_dict)


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


def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)
        if form.is_valid():
            mail_form_info(form)

    form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})


def mail_form_info(form):

    email = form.cleaned_data["email"]
    first_name = form.cleaned_data["firstName"]
    last_name = form.cleaned_data["lastName"]
    phone_number = form.cleaned_data["phoneNumber"]
    num_vehicles_detailed = form.cleaned_data["numVehiclesDetailed"]
    service = form.cleaned_data["service"]
    other_service = form.cleaned_data["other_service"]
    nature_ack = form.cleaned_data["nature_ack"]
    photos_ack = form.cleaned_data["photos_ack"]
    photos_no = form.cleaned_data["photos_no"]

    subject = "Custom Contact Notice"
    html_message = render_to_string("mail/mail_template.html", {"context": "values"})
    plain_message = strip_tags(html_message)
    from_email = "From <caleb.ja.owenss@gmail.com>"
    to = "calebotherstuff@gmail.com"

    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)