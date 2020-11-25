from django import forms
from . models import addemployee,addservices,announcement


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = addemployee
        fields = ('full_name','father_name','contact','aadhar','pan','whrs','oemail','pemail','designation','dept','Gender','doj','address','job_loc','bank_name','ba_no','pfno','salary')
        labels = {

            'full_name':'Full Name',
            'father_name': "Father's Name",
            'contact':'Contact No',
            'aadhar':'Aadhar Card No',
            'pan':'PAN No',
            'whrs':'Working hours',
            'oemail':'Official Email id',
            'pemail':'Personal Email id',
            'designation':'Designation',
            'dept':'Department',
            'Gender':'Gender',
            'doj':'Date of Join',
            'address':'Residential Address',
            'job_loc':'Job location',
            'bank_name':'Bank Name',
            'ba_no':'Bank Account No',
            'pfno':'Provident Fund No',
            'salary':'Salary',
            
        }

class ServiceForm(forms.ModelForm):

    class Meta:
        model = addservices
        fields=('service_name','category','cost','technology')
        label={
           
            'service_name':'Service Name',
            'category':'Category',
            'cost':'Cost',
            'technology':'Technology',

        }


        
class announce(forms.ModelForm):

    class Meta:
        model = announcement
        fields=('announce_to','message')
        label={
           'announce_to':'To',
           'message':'Message',


        }
       

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = addemployee
        fields = ('image',)


        