from re import A
from . choices import Page_Choices
from .validatorExpressions import PAN_Validator,aadhaar_Validator
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User



# Create your models here.
class PassPort(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    No_of_Pages = models.IntegerField(choices = Page_Choices)
    PAN_Card = models.CharField(max_length = 500,validators=[RegexValidator(PAN_Validator,message = "Enter a Valid PAN Number")],blank = True,null = True)
    Aadhaar_Card = models.CharField(max_length = 500,validators=[RegexValidator(aadhaar_Validator,message = "Enter a Valid Aadhar Number")],blank = True,null = True)
    Gender = models.CharField(max_length = 500)
    Date_of_Birth = models.DateField(max_length = 8)
    Alias_Names = models.BooleanField(default = False,blank = True,null = True)
    Name_Change = models.BooleanField(default = False)
    def __str__(self):
        return self.user.username
    
        
    
    
    