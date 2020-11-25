from django.urls import path

from . import views

urlpatterns = [
    path('hrportal/<str:username>',views.hrportal,name="hrportal"),
    path('logout/<str:Employee_id>',views.logout,name="logout"),
    path('view_profile/<str:Employee_id>',views.view_profile,name="view_profile"),
    path('new_announhr/<str:Employee_id>',views.new_announhr,name="new_announhr"),
    path('view_announhr/<str:Employee_id>',views.view_announhr,name='view_announhr'),
    path('exist_emphr/<int:id>',views.exist_emphr,name='exist_emphr'),
    path('addemphr/<str:Employee_id>',views.addemphr,name="addemphr"),
    path('leave_requesthr/<str:Employee_id>',views.leave_requesthr,name="leave_requesthr"),
    path('view_leavehr/<str:Employee_id>',views.view_leavehr,name="view_leavehr"),
    path('new_approvehr/<str:Employee_id>',views.new_approvehr,name="new_approvehr"),
    path('view_approvehr/<str:Employee_id>',views.view_approvehr,name="view_approvehr"),
    path('approvehr/<str:emp_id>/<int:id>',views.approvehr,name="approvehr"),
    path('rejecthr/<str:emp_id>/<int:id>',views.rejecthr,name="rejecthr"),
    path('<int:id>', views.employee_form1,name='updatehr'), 
    path('viewsalhr/<str:Employee_id>',views.viewsalhr,name='viewsalhr'),
    path('view_salaryhr/<str:Employee_id>',views.view_salaryhr,name='view_salaryhr'),
    path('gensal/<str:Employee_id>',views.gensal,name='gensal'),
    path('salaryslip/<str:Employee_id>',views.salaryslip,name='salaryslip'),
    path('Salaryhr/<str:Employee_id>',views.Salaryhr,name='Salaryhr'),
    path('salary_slip/<int:id>',views.salary_slip,name='salary_slip'),
     path('salary_down/<int:id>',views.salary_down,name='salary_down')
    

   
  

]