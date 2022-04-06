from . import views
from django.urls import path,include

urlpatterns = [
    path("passport/application",views.passportapplciation,name = "passport_application"),
]