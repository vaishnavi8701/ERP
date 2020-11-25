from django.urls import path

from . import views

urlpatterns = [

    path('marportal/<str:username>',views.marportal,name="marportal"),
    path('logout/<str:Employee_id>',views.logout,name="logout"),
    path('view_mar/<str:Employee_id>',views.view_mar,name="view_mar"),
    path('view_announmar/<str:Employee_id>',views.view_announmar,name='view_announmar'),
    path('new_announmar/<str:Employee_id>',views.new_announmar,name='new_announmar'),
    path('leave_requestmar/<str:Employee_id>',views.leave_requestmar,name="leave_requestmar"),
    path('view_leavemar/<str:Employee_id>',views.view_leavemar,name="view_leavemar"),
    path('Salarymar/<str:Employee_id>',views.Salarymar,name='Salarymar'),
    path('addclient/<str:Employee_id>',views.addclient,name='addclient'),
    path('view_client/<int:id>',views.view_client,name='view_client'),
    path('<int:id>', views.client_form,name='update_client'), 
    path('quotation/<str:clientid>',views.quotation,name='quotation'),
    path('quot/<str:quotation_id>/<str:clientid>',views.quot,name='quot'),
    path('submit/<str:clientid>',views.submit,name='submit'),
    path('viewquot/<str:Employee_id>',views.viewquot,name='viewquot'),
    path('view/<str:clientid>',views.view,name='view'),
    path('quotdown/<str:clientid>',views.quotdown,name='quotdown'),
    path('amount/<str:Employee_id>',views.amount,name='amount'),
    path('payment/<str:Employee_id>',views.payment,name='payment'),
    path('quotview/<str:clientid>',views.quotview,name='quotview'),


   
  

]