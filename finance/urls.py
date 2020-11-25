from django.urls import path

from . import views

urlpatterns = [
    path('finportal/<str:username>',views.finportal,name="finportal"),
    path('logout/<str:Employee_id>',views.logout,name="logout"),
    path('view_fin/<str:Employee_id>',views.view_fin,name="view_fin"),
    path('view_announfin/<str:Employee_id>',views.view_announfin,name='view_announfin'),
    path('new_announfin/<str:Employee_id>',views.new_announfin,name='new_announfin'),
    path('leave_requestfin/<str:Employee_id>',views.leave_requestfin,name="leave_requestfin"),
    path('view_leavefin/<str:Employee_id>',views.view_leavefin,name="view_leavefin"),
    path('Salaryfin/<str:Employee_id>',views.Salaryfin,name='Salaryfin'),
    path('emppayfin/<str:Employee_id>',views.emppayfin,name='emppayfin'),
    path('emppayfin1/<str:Employee_id>',views.emppayfin1,name='emppayfin1'),
    path('emppay/<str:Employee_id>',views.emppay,name='emppay'),
    path('emp2/<str:Employee_id>',views.emp2,name='emp2'),
    path('emp1/<str:Employee_id>',views.emp1,name='emp1'),
    path('pastpay/<str:Employee_id>',views.pastpay,name='pastpay'),
    path('addvendor/<str:Employee_id>',views.addvendor,name='addvendor'),
    path('viewsvendor/<int:id>',views.viewsvendor,name='viewsvendor'),
    path('taxfin/<str:Employee_id>',views.taxfin,name='taxfin'),
    path('<str:Employee_id>/<int:id>', views.vendor_form,name='viewven'), 
    path('venpay/<str:Employee_id>/<int:id>', views.venpay,name='venpay'), 
    path('venpay1/<str:Employee_id>', views.venpay1,name='venpay1'), 
    path('newpay/<str:Employee_id>', views.newpay,name='newpay'), 
    path('addreceipt/<str:Employee_id>/<str:clientid>', views.addreceipt,name='addreceipt'),
    path('addreceipt1/<str:Employee_id>', views.addreceipt1,name='addreceipt1'),
    path('exreceipt/<str:Employee_id>', views.exreceipt,name='exreceipt'),
    path('receipt/<str:receipt_id>',views.receipt,name='receipt'),
    path('recprint/<str:receipt_id>',views.recprint,name='recprint'),
    path('receiptdown/<str:receipt_id>',views.receiptdown,name='receiptdown'),
    




   


   
  

]