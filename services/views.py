from . models import PassPort
from . forms import PassPortApplicationForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request,"services/home.html")
@login_required
def dashboard(request):
    if request.user.is_superuser:
        passports = PassPort.objects.prefetch_related("user").all()
    else:
        passports = PassPort.objects.prefetch_related("user").filter(user = request.user)
    return render(request,"services/dashboard.html",{"Passports":passports})
@login_required
def passportapplciation(request):
    if request.method == "POST":
        application = PassPort.objects.prefetch_related("user").filter(user = request.user,Application_Status = "In Queue").exists()
        passportform = PassPortApplicationForm(request.POST)
        if passportform.is_valid():
            passport = passportform.save(commit = False)
            passport.user = request.user
            if application:
                passport.Application_Status = "Cancelled"
            else:
                passport.Application_Status = "In Queue"
            #passport.
            passport.save()
            messages.success(request,"Passport Application Successful. You may find the Application Status in the dashboard of your Account")
            return redirect("dashboard")
        else:
            return render(request,"services/passportapplication.html",{"form":passportform})
    return render(request,"services/passportapplication.html",{"form":PassPortApplicationForm()})