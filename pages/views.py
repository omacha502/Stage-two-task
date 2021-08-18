from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return HttpResponse('<h1>Thank you for submitting</h1>'
                            'My Stage two task Submission'
                            'The contact form responses are stored in the django database,'
                            'you will have to login to the django admin dashboard to see responses'
                            '')
    return render(request, 'index.html')
