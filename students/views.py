from students.serializers import StudentSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
import json

# Create your views here.
@api_view(['GET','POST'])
def student(request):
    if request.method=="GET":
        query=Student.objects.all()
        serializer=StudentSerializer(query,many=True)
        return Response(serializer.data)
    else:
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET','POST'])
def addmark(request):
    if request.method=="POST":
        serializer=AddmarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data) 
    else:
        query=Addmark.objects.all()
        serializer=AddmarkSerializer(query,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def results(request,category):
    if category=="number_of_students":
        query=Student.objects.all().count()
        return Response("Total Number Of Students:"+ str(query))
    elif category=="number_of_students_grade":
        l1=["A","B","C","F"]
        l2=[]
        for i in l1:
            query=Addmark.objects.filter(grade1=i).count()
            l2.append(query)
        dic=dict(zip(l1,l2))
        return Response(dic)
    elif category=="grades":
        query=Addmark.objects.values("grade1")
        return Response(query)
    elif category=="percentage":
        dist=Addmark.objects.filter(grade1="A").count()
        total=Student.objects.all().count()
        fist=Addmark.objects.filter(grade1="B").count()
        clas=Addmark.objects.filter(grade1="C").count()
        f=Addmark.objects.filter(grade1="F").count()
        Distinction=dist/total
        First_class=(fist+clas)/total
        passed=(total-f)/total
        return Response("pass% :"+str(passed)+" "+"firstclass% :"+str(First_class)+" "+"distinction% :"+str(Distinction))
