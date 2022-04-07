from . models import Document,PassPort
from . forms import DocumentUploadForm, PassPortApplicationForm
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
        application = PassPort.objects.prefetch_related("user").filter(user = request.user,Application_Status = "In Queue").exists() or PassPort.objects.prefetch_related("user").filter(user = request.user,Application_Status = "Awaiting Document Upload").exists()
        passportform = PassPortApplicationForm(request.POST)
        if passportform.is_valid():
            passport = passportform.save(commit = False)
            passport.user = request.user
            if application:
                passport.Application_Status = "Cancelled"
                passport.Remark = "Cancelled due to mutiple applications in queue"
            else:
                passport.Application_Status = "Awaiting Documents Upload"
            #passport.
            passport.save()
            messages.success(request,"Passport Application Saved Successfully.Upload the documents inorder to send it for approval. You may find the Application Status in the dashboard of your Account")
            return redirect("dashboard")
        else:
            return render(request,"services/passportapplication.html",{"form":passportform})
    return render(request,"services/passportapplication.html",{"form":PassPortApplicationForm()})
@login_required
def upload_document(request,pk,slug):
    Passport = PassPort.objects.prefetch_related("user").get(id = pk,slug = slug,user = request.user)
    if Passport != None:
        if request.method == "POST":
            documentform = DocumentUploadForm(request.POST,request.FILES)
            if documentform.is_valid():
                documents = documentform.save(commit = False)
                documents.Passport = Passport
                Passport.Application_Status = "In Queue"
                Passport.save()
                documents.save()
                messages.success(request,"Document Upload Successful.You may find the Application Status in the dashboard of your Account")
                return redirect("dashboard")
            else:
                return render(request,"services/documentupload.html",{"form":documentform})
        else:
            return render(request,"services/documentupload.html",{"form":DocumentUploadForm()})
    else:
        messages.error(request,"Error Processing Request")
        return redirect("dashboard")
              
@login_required
def approvalapplicationpage(request,pk,slug):
    if request.user.is_superuser:
        Application = PassPort.objects.prefetch_related("user").get(id = pk,slug = slug)
        Documents = Document.objects.prefetch_related("Passport").get(Passport = Application)
        return render(request,"services/approveapplication.html",{"Application":Application,"Document":Documents})
    else:
        return redirect("dashboard")
def approveapplication(request,pk,slug):
    Application = PassPort.objects.prefetch_related("user").get(id = pk,slug = slug)
    if request.method == "POST" and request.user.is_superuser:
        Application.Application_Status = "Processed and Approved"
        Application.save()
        messages.success(request,"Approved Application successfully")
        return redirect("approve_application",pk = pk,slug = slug)
    else:
        messages.error(request,"Error While Processing Request")
        return redirect("approve_application",pk = pk,slug = slug)
def cancelapplication(request,pk,slug):
    Application = PassPort.objects.prefetch_related("user").get(id = pk,slug = slug)
    if request.method == "POST" and request.user.is_superuser:
        Application.Application_Status = "Cancelled"
        Application.Remark = "Cancelled Due to some issues or discrepancy with Documents Uploaded"
        Application.save()
        messages.success(request,"Approved Application successfully")
        return redirect("approve_application",pk = pk,slug = slug)
    else:
        messages.error(request,"Error While Processing Request")
        return redirect("approve_application",pk = pk,slug = slug)