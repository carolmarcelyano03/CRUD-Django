from django import forms  
from employee.models import Employee
from employee.models import Education
from employee.models import Experience
from employee.models import Picture
from django.forms import fields

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__" 

class EducationForm(forms.ModelForm):  
    class Meta:  
        model = Education  
        fields = "__all__"  

class ExperienceForm(forms.ModelForm):  
    class Meta:  
        model = Experience 
        fields = "__all__" 

class PictureForm(forms.ModelForm):  
    class Meta:  
        model = Picture
        fields = "__all__"   