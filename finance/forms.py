from django import forms
from . models import vendor


class VendorForm(forms.ModelForm):

    class Meta:
        model = vendor
        fields = ('vendor_id','vendor_name','contact','type_amt','vendor_pan','vendor_gst','payment_duration','mode_of_pay','due_date','email','location','service_provided','cost','status')
        labels = {

            'vendor_id':'Vendor ID',
            'vendor_name':'Vendor Name',
            'contact':'Contact',
            'type_amt':'Type',
            'email':'Email',
            'vendor_pan':'Vendor Pan',
            'vendor_gst':'Vendor Gst',
            'payment_duration':'Payment Duration',
            'mode_of_pay':'Mode of Pay',
            'due_date':'Due Date',
            'location':'Location',
            'service_provided':'Service Provided',
            'cost':'Cost',
            'status':'Status'

            
            
        }