from django.urls import path

from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('adlogin',views.adlogin,name="adlogin"),
    path('emplogin',views.emplogin,name="emplogin"),
    path('forgotpass',views.forgotpass,name="forgotpass"),
    path('resetpass/<int:id>',views.resetpass,name="resetpass"),
    path('<int:id>',views.otp,name="otp")
    
    


]