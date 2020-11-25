from django.urls import path

from . import views

urlpatterns = [
    path('adminportal',views.adminportal,name="adminportal"),
    path('addemp',views.addemp,name="addemp"),
    path('logout',views.logout,name="logout"),
    path('new',views.new_emp,name="new_emp"),
    path('exist_emp',views.exist_emp,name="exist_emp"),
    path('<int:id>', views.employee_form,name='update'), 
    path('new_services',views.new_services,name='new_services'),
    path('view_services',views.view_services,name='view_services'),
    path('<int:id>/', views.new_services,name='service_update'),
    path('delete/<int:id>/',views.services_delete,name='service_delete'),
    path('discount>',views.discounts,name='discount'),
    path('new_announce',views.new_announce,name='new_announce'),
    path('view_announce',views.view_announce,name='view_announce'),
    path('upload_photo/<str:Employee_id>',views.upload_photo,name="upload_photo"),
    path('upload_photo1/<str:Employee_id>',views.upload_photo1,name="upload_photo1"),
    path('upload_photo2/<str:Employee_id>',views.upload_photo2,name="upload_photo2"),
    path('upload_photo3/<str:Employee_id>',views.upload_photo3,name="upload_photo3"),
    path('change_pass/<str:Employee_id>',views.change_pass,name="change_pass"),
    path('change_pass1/<str:Employee_id>',views.change_pass1,name="change_pass1"),
    path('change_pass2/<str:Employee_id>',views.change_pass2,name="change_pass2"),
    path('change_pass3/<str:Employee_id>',views.change_pass3,name="change_pass3"),
    path('submit/<str:pemail>',views.submit,name="submit"),
    path('new_approve',views.new_approve,name="new_approve"),
    path('view_approve',views.view_approve,name="view_approve"),
    path('approve/<int:id>',views.approve,name="approve"),
    path('reject/<int:id>',views.reject,name="reject"),
    path('adpay',views.adpay,name="adpay"),
    path('vpay',views.vpay,name="vpay"),
    path('taxad',views.taxad,name="taxad"),
    path('viewvendor',views.viewvendor,name="viewvendor"),
    path('exreceiptad',views.exreceiptad,name="exreceiptad"),
    path('proclient',views.proclient,name="proclient"),
    path('proall',views.proall,name="proall"),
    path('exclient',views.exclient,name="exclient"),
    path('clientdata/<str:clientid>',views.clientdata,name="clientdata"),
    path('clientda/<str:clientid>',views.clientda,name="clientda"),
     path('clienthist',views.clienthist,name="clienthist"),
    path('ven_form/<int:id>', views.ven_form,name='ven_form'), 





   
  

]
