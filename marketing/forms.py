from django import forms
from . models import client


class ClientForm(forms.ModelForm):

    class Meta:
        model = client
        fields = ('clientname','company_name','client_address','contact','alcontact','company_email','meeting','remarks','status')
        labels = {

            'clientname':'Client Name',
            'company_name':'company_name',
            'client_address':'Client Address',
            'contact':'Contact',
            'alcontact':'Alternative Contact',
            'company_email':'Email',
            'meeting':'Meeting',
            'remarks':'Remarks',
            'status':'Status'

            
            
        }