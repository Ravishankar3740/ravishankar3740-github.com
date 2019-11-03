
from django.urls import path
from .import views
urlpatterns = [
    path("",views.allblogs,name='blogsss'),
    path("Twitter/",views.enquiry,name='enquiry'),
    path('<int:blog_id>/',views.detail),
    path("inquiry/",views.inquiry,name='inquiry'),

]