from django.urls import path

from . import views

urlpatterns = [
    path('techportal/<str:username>',views.techportal,name="techportal"),
    path('logout/<str:Employee_id>',views.logout,name="logout"),
    path('view_tech/<str:Employee_id>',views.view_tech,name="view_tech"),
    path('view_annountech/<str:Employee_id>',views.view_annountech,name='view_annountech'),
    path('new_annountech/<str:Employee_id>',views.new_annountech,name='new_annountech'),
    path('leave_requesttech/<str:Employee_id>',views.leave_requesttech,name="leave_requesttech"),
    path('view_leavetech/<str:Employee_id>',views.view_leavetech,name="view_leavetech"),
    path('Salarytech/<str:Employee_id>',views.Salarytech,name='Salarytech'),
    path('newprotech/<str:Employee_id>',views.newprotech,name='newprotech'),
    path('assignedproject/<str:Employee_id>',views.assignedproject,name='assignedproject'),
    path('accept/<int:id>/<str:Employee_id>',views.accept,name='accept'),
    path('files/<int:id>/<str:Employee_id>',views.files,name='files'),



   
  

]