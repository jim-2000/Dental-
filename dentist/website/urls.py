from django.urls import path
from .import views

urlpatterns = [
    path('',views.HOME, name="HOME" ),
    path('contuct/', views.contuct, name="Contuct"),
    path('service/', views.service, name="Service"),
    path('about/', views.about, name="About"),
    path('blog/', views.blog, name="Blog"),
    path('blog_details/', views.bdetails, name= "B_Details"),
    path('price/', views.price, name='Price'),
    path('base/', views.base, name="base"),
    path('log/', views.log, name="LOG_In"),
    path('reg/', views.reg, name="Registration"),
    path('appoinment/', views.appoinment, name="Appoinment")
]
