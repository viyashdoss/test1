from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'


class AddmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Addmark
        fields='__all__'
        

        
        