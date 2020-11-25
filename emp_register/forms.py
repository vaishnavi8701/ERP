from django import forms
from . models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
 
        fields = ('fullname','father_name','mobile','aadhar','pan','whrs','oemail','pemail','designation','department','Gender','doj','address','job_loc','bank_name','ba_no','pfno','salary')

        labels = {
            'fullname':'Full Name',
            'father_name': "Father's Name",
            'mobile':'Contact No',
            'aadhar':'Aadhar Card No',
            'pan':'PAN No',
            'whrs':'Working hours',
            'oemail':'Official Email id',
            'pemail':'Personal Email id',
            'designation':'Designation',
            'department':'Department',
            'Gender':'Gender',
            'doj':'Date of Join',
            'address':'Residential Address',
            'job_loc':'Job location',
            'bank_name':'Bank Name',
            'ba_no':'Bank Account No',
            'pfno':'Provident Fund No',
            'salary':'Salary',
            
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Select"
        
       
