import random
import uuid
from . choices import Page_Choices,State_Choices,Martial_Status_Choices,Employment_Choices,Educational_Choices,Application_Status_Choices
from .validatorExpressions import PAN_Validator,aadhaar_Validator
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from autoslug import AutoSlugField



# Create your models here.
class PassPort(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length = 45,help_text = "(Max 45 Characters)")
    Surname = models.CharField(max_length = 45,help_text = "(Max 45 Characters)",blank = True)
    No_of_Pages = models.IntegerField(choices = Page_Choices)
    PAN = models.CharField(max_length = 500,validators=[RegexValidator(PAN_Validator,message = "Enter a Valid PAN Number")],null = True)
    Aadhaar_Number = models.CharField(max_length = 500,validators=[RegexValidator(aadhaar_Validator,message = "Enter a Valid Aadhar Number")],null = True,help_text = "Enter Aadhaar with requried spaces")
    Gender = models.CharField(max_length = 500)
    Date_of_Birth = models.DateField()
    Place_of_Birth = models.CharField(max_length = 500,help_text = "Village/City/Town")
    House_Name = models.CharField(max_length = 500)
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
    Date_of_Application = models.DateTimeField(auto_now = True)
    Remark = models.TextField(max_length = 500,blank = True)
    def __str__(self):
        return self.user.username
    def save(self, *args, **kwargs):
        if not self.Application_Id:
            self.Application_Id = random.randint(0,10000)
        super(PassPort,self).save(*args,**kwargs)
class Document(models.Model):
    Passport = models.OneToOneField(PassPort,on_delete = models.CASCADE)
    Father_Name = models.CharField(max_length = 100)
    Mother_Name = models.CharField(max_length=100)
    Mobile_Number = PhoneNumberField()
    Telephone_Number = PhoneNumberField(blank = True)
    Email_ID = models.EmailField(blank = True)
    Aadhar_Card = models.FileField(upload_to = "Documents/certificates/aadhar/")
    PAN_Card = models.FileField(upload_to = "Documents/certificates/pan/")
    Certificate = models.FileField(upload_to = "Documents/certificates/birth_marriage/")
    Educational_Certificate = models.FileField(upload_to = "Documents/certificates/education")
    Voter_ID = models.FileField(upload_to = "Documents/certificates/voter_id",blank = True)
    Signature = models.FileField(upload_to = "Documents/certificates/pan/signature/")
    slug = models.SlugField(max_length = 100)
    def __str__(self):
        return str(self.Passport.Application_Id)+'-Document Upload'
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        super(Document,self).save(*args,**kwargs)
    
    