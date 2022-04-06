import random
from . choices import Page_Choices,State_Choices,Martial_Status_Choices,Employment_Choices,Educational_Choices,Application_Status_Choices
from .validatorExpressions import PAN_Validator,aadhaar_Validator
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from autoslug import AutoSlugField



# Create your models here.
class PassPort(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length = 45,help_text = "(Max 45 Characters)")
    Surname = models.CharField(max_length = 45,help_text = "(Max 45 Characters)",blank = True)
    No_of_Pages = models.IntegerField(choices = Page_Choices)
    PAN = models.CharField(max_length = 500,validators=[RegexValidator(PAN_Validator,message = "Enter a Valid PAN Number")],blank = True,null = True)
    Aadhaar_Number = models.CharField(max_length = 500,validators=[RegexValidator(aadhaar_Validator,message = "Enter a Valid Aadhar Number")],null = True,help_text = "Enter Aadhaar with requried spaces")
    Gender = models.CharField(max_length = 500)
    Date_of_Birth = models.DateField()
    Place_of_Birth = models.CharField(max_length = 500,help_text = "Village/City/Town")
    State = models.CharField(choices=State_Choices,max_length=255,)
    District = models.CharField(max_length = 255)
    Marital_Status = models.CharField(max_length = 100,choices = Martial_Status_Choices)
    Citizenship_of_India = models.CharField(max_length = 255)
    Employment_Type = models.CharField(max_length = 500,choices = Employment_Choices)
    Government_Servant = models.BooleanField(default = False)
    Educational_Qualification = models.CharField(max_length = 500,choices = Educational_Choices)
    Non_ECR_Category = models.BooleanField(default = False)
    Visible_Distinguishing_Mark = models.CharField(max_length = 100,blank = True)
    Application_Status = models.CharField(max_length = 200,choices = Application_Status_Choices)
    Application_Id = models.PositiveBigIntegerField(blank = True)
    slug = AutoSlugField(populate_from = "Name",unique=True)
    def __str__(self):
        return self.user.username
    def save(self, *args, **kwargs):
        if not self.Application_Id:
            self.Application_Id = random.randint(0,10000)
        super(PassPort,self).save(*args,**kwargs)
