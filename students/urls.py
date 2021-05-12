
from django.urls import path,include
from .views import *


'''category={number_of_students,number_of_students_grade,grades,percentage} use any oh this to get result'''
urlpatterns = [
    
    path('/students',student),
    path('/students/add-mark',addmark),
    path('/students/results/<str:category>/',results),
]
