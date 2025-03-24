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
    slug = models.SlugField(unique=True, max_length=255, help_text="Unique URL-friendly identifier for the blog")
    meta_title = models.CharField(max_length=200, help_text="SEO-friendly title for the blog")
    meta_description = models.TextField(help_text="SEO-friendly description for the blog")
    name = models.CharField(max_length=200,blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/',blank=True, null=True)
    created_date = models.DateTimeField(default=now,blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Auto-generate slug from title
        super().save(*args, **kwargs)

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


# Websss
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, max_length=255, help_text="Unique URL identifier for the category")
    created_date = models.DateTimeField(default=now, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # If updating an existing category
            old_category = Category.objects.get(pk=self.pk)
            if old_category.name != self.name:  # Check if name is changed
                self.slug = slugify(self.name)  # Generate new slug

                # Update related Website URLs
                from vynzora_app.models import Website  # Import inside to avoid circular import
                Website.objects.filter(category=self).update(category=self)  # Update category reference

        else:
            self.slug = slugify(self.name)  # Generate slug for new category

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Website(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="websites"
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    image = models.ImageField(upload_to="website_images/", blank=True, null=True)
    created_date = models.DateTimeField(default=now, blank=True, null=True)
    add_description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it's empty
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Website.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug  # Assign the unique slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Service(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name="services")
    heading = models.CharField(max_length=200, verbose_name="Service Heading")
    description = models.TextField(verbose_name="Service Description")

    class Meta:
        constraints = []  # ❌ Removed uniqueness constraint on (website, heading)

    def __str__(self):
        return f"{self.heading} - {self.website.name}"


# Careeers
class Career_Model(models.Model):    
    job_position = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    salary = models.IntegerField()
    job_details = RichTextField(max_length=20000)
    posted_date = models.DateField()
    end_date = models.DateField()
    post_end_date = models.DateTimeField()
    
    def is_active(self):
        return self.post_end_date >= timezone.now()

# Cadidate
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdfs/')
    job_position = models.ForeignKey(Career_Model, on_delete=models.CASCADE, related_name='candidates', null=True)
    
    def __str__(self):
        return self.name