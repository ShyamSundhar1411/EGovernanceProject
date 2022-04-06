from . import views
from django.urls import path,include

urlpatterns = [
    path("",views.dashboard,name = "dashboard"),
    path("passport/application",views.passportapplciation,name = "passport_application"),
    path("passport/<int:pk>/<slug:slug>/approve/administrator",views.approveapplication,name = "approve_application")
]