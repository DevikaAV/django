from django .urls import path
from home import views
urlpatterns = [
     path('',views.about),
     path('user',views.login),
     path('adminlogin',views.adminlogin),
     path('adminsign',views.adminsign),
     path('Quizhtml',views.home),
     path('add',views.addQuestion),
     
 ]