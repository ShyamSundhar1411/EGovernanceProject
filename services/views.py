from . models import PassPort
from . forms import PassPortApplicationForm
from django.shortcuts import render,redirect
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,"services/home.html")
def dashboard(request):
    return render(request,"services/dashboard.html")
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
            passport.save()
            messages.success(request,"Passport Application Successful. You may find the Application Status in the dashboard of your Account")
            return redirect("dashboard")
        else:
            return render(request,"services/passportapplication.html",{"form":passportform})
    return render(request,"services/passportapplication.html",{"form":PassPortApplicationForm()})