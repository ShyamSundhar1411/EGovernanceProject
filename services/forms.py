from . models import PassPort,Document
from . choices import *
from django import forms

class PassPortApplicationForm(forms.ModelForm):
    No_of_Pages = forms.CharField(widget = forms.RadioSelect(choices = Page_Choices))
    House_Name = forms.CharField(label = "House/Street Name")
    Gender = forms.CharField(widget = forms.RadioSelect(choices = Gender_Choices))
    Date_of_Birth = forms.DateInput(format = "%d%M%Y")
    Citizenship_of_India = forms.CharField(widget = forms.RadioSelect(choices = Citizenship_Choices),label = "Cirizenship of India by")
    Government_Servant = forms.BooleanField(label = "Is either of your parent (in case of minor)/spouse, a government servant?",required = False)
    Non_ECR_Category = forms.BooleanField(label = " Is applicant eligible for Non-ECR category?",required = False)
    class Meta:
        model = PassPort
        fields = ["Name","Surname","Gender","Place_of_Birth","House_Name","State","District","Date_of_Birth","Marital_Status","Citizenship_of_India","PAN","Aadhaar_Number","Employment_Type","Government_Servant","Educational_Qualification","Non_ECR_Category","Visible_Distinguishing_Mark","No_of_Pages"]
class DocumentUploadForm(forms.ModelForm):
    Certificate = forms.FileField(label = "Birth Certificate/Marriage Certificate")
    Father_Name = forms.CharField(label = "Father's Name")
    Mother_Name = forms.CharField(label = "Mother's Name")
    class Meta:
        model = Document
        fields = ["Father_Name","Mother_Name","Mobile_Number","Telephone_Number","Email_ID","Aadhar_Card", "PAN_Card","Certificate","Educational_Certificate","Voter_ID"]