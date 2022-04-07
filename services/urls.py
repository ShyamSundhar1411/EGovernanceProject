from . import views
from django.urls import path,include

urlpatterns = [
    path("",views.dashboard,name = "dashboard"),
    path("passport/application",views.passportapplciation,name = "passport_application"),
    path("passport/<int:pk>/<slug:slug>/approve/administrator",views.approvalapplicationpage,name = "approve_application"),
    path("passport/<int:pk>/<slug:slug>/approve/application/administrator",views.approveapplication,name = "approval_confirmation"),
    path("passport/<int:pk>/<slug:slug>/cancel/application/administrator",views.cancelapplication,name = "cancellation_confirmation"),
    path("passport/<int:pk>/document/<slug:slug>/upload",views.upload_document,name = "upload_document")
]