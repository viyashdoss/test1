from django.db import models

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=50)
    Roll_Number=models.IntegerField(primary_key=True)
    Dob=models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.Name



class Addmark(models.Model):
    choice=(
        ("A","A"),
        ("B","B"),
        ("C","C"),
        ("F","F")
    )
    rollnum=models.ForeignKey(Student,on_delete=models.CASCADE)
    marks=models.IntegerField()
    grade1=models.CharField(max_length=50,choices=choice)

    def __str__(self):
        return self.rollnum


    