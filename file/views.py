from file.forms import FileForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import File, Download
from django.contrib import messages
from django.contrib.auth.models import User
import os
# Create your views here.


def Home(request):
    return render(request, "home/home.html")


def file(request):
    return render(request, "file.html")


def upload_file(request):
    form = FileForm()
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        
        if form.is_valid():
            fileobj = request.FILES.get('path')
            size = fileobj.size
            ctype = fileobj.content_type
            fd = form.save(commit=False)
            fd.extension = ctype
            fd.size = size
            fd.save()
            messages.success(request,'file uploaded')
            return redirect("views")
    ctx = {'form':form}
    return render(request, "file/upload.html",ctx)


def profile(request):

    return render(request, "file/profile.html")


def views(request):
    file = File.objects.all()
    return render(request, "file/views.html", {"file": file})


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            pass
        pass
    else:
        return HttpResponseRedirect('/login/')
