from django.db import models

# Create your models here.

# Create your models here.



class PersonalInformation(models.Model):
    Name = models.CharField(max_length = 250)
    DateofBirth = models.CharField(max_length = 250)
    PermanentAddress =models.CharField(max_length=250)
    PresentAddress =models.CharField(max_length=250)
    Education =models.CharField(max_length = 250)
    University=models.CharField(max_length = 250)
    GraduationDate=models.CharField(max_length = 250)
    Contact =models.CharField(max_length=250)
    EmailAddress =models.EmailField(max_length=100)
    LinkedIn_id = models.CharField(max_length = 250)
    Facebook_id = models.CharField(max_length = 250)
    github_id =models.CharField(max_length = 250)



class Myobjective(models.Model):
    SoftwareEngineering = models.CharField(max_length=1000)
    ComputerEngineering = models.CharField(max_length=1000)
    skills = models.CharField(max_length=500)

class myprojects(models.Model):
    pdf_file = models.FileField()
    matlab_file= models.FileField()
    excel_file =  models.FileField()


class Messages(models.Model):

        Name = models.CharField(max_length=300)
        body = models.TextField(max_length = 5000)
        Email = models.EmailField(max_length=20)

