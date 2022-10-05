from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path ("",views.login,name="login"),
   path ("index",views.index,name="home"),
   path("admission",views.admission,name="admission"),
   path("technicalclubs",views.technicalclubs,name="technicalclubs"),
   path("nontechnicalclubs",views.nontechnicalclubs,name="nontechnicalclubs"),
   path("login",views.login,name="login"),
   path("signup",views.signup,name="signup"),
   path("user_logout",views.user_logout,name="user_logout")
   ]