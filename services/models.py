from re import A
from . choices import Page_Choices,State_Choices,Martial_Status_Choices,Employment_Choices,Educational_Choices,Application_Status_Choices
from .validatorExpressions import PAN_Validator,aadhaar_Validator
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from autoslug import AutoSlugField



# Create your models here.
class PassPort(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length = 45)
    Surname = models.CharField(max_length = 45)
    No_of_Pages = models.IntegerField(choices = Page_Choices)
    PAN_Card = models.CharField(max_length = 500,validators=[RegexValidator(PAN_Validator,message = "Enter a Valid PAN Number")],blank = True,null = True)
    Aadhaar_Card = models.CharField(max_length = 500,validators=[RegexValidator(aadhaar_Validator,message = "Enter a Valid Aadhar Number")],null = True)
    Gender = models.CharField(max_length = 500)
    Date_of_Birth = models.DateField()
    Alias_Names = models.BooleanField(default = False,blank = True,null = True)
    Name_Change = models.BooleanField(default = False)
    Birth_in_Indian = models.BooleanField(default = None)
    State = models.CharField(choices=State_Choices,max_length=255,)
    District = models.CharField(max_length = 255)
    Marital_Status = models.CharField(max_length = 100,choices = Martial_Status_Choices)
    Citizenship_of_India = models.CharField(max_length = 255)
    Employment_Type = models.CharField(max_length = 500,choices = Employment_Choices)
    Government_Servant = models.BooleanField()
    Educational_Qualification = models.CharField(max_length = 500,choices = Educational_Choices)
    Non_ECR_Category = models.BooleanField()
    Visible_Distinguishing_Mark = models.CharField(max_length = 100,blank = True)
    Application_Status = models.CharField(max_length = 200,choices = Application_Status_Choices)
    slug = AutoSlugField(populate_from = "Name",unique=True)
    def __str__(self):
        return self.user.username
    
        
    
    
    