from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.utils import timezone

class ContactModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Contact"


# Client Reviews
class ClientReview(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    client_image = models.ImageField(upload_to='client_images/', null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.client_name} - {self.designation}"

# Clients Logo

class Client_Logo(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    logo = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name


# Technologies
class Technologies(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    logo = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name

# Blog
class Blog(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/',blank=True, null=True)
    created_date = models.DateTimeField(default=now,blank=True, null=True)

    def __str__(self):
        return self.name

#  Team
class Team(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    client_image = models.ImageField(upload_to='client_images/', null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
   
    def __str__(self):
        return f"{self.client_name} - {self.designation}"


    # Portfolio 
class ProjectModel(models.Model):
    project_name = models.CharField(max_length=100, null=True, blank=True)
    website_link = models.CharField(max_length=200, null=True, blank=True)
    project_image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    def __str__(self):
        return self.project_name


# Certificate
class Certificates(models.Model):
    id1 = models.CharField(max_length=100)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    join_date = models.DateField(null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/')  
    def __str__(self):
        return f"{self.id1}"