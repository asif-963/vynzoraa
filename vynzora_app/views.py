from django.shortcuts import  render, redirect, get_object_or_404
from django.conf import settings 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
import random
from django.utils import timezone


from .models import ContactModel, ClientReview, Client_Logo, Technologies, Blog, Team, ProjectModel, Certificates, Category, Website, Service, Career_Model, Candidate
from .forms import ContactModelForm, ClientReviewForm, Client_Logo_Form, TechnologiesForm, BlogForm, TeamForm, ProjectModelForm, CertificatesForm, CategoryForm, WebsiteForm, CareerForm, CandidateForm


def index(request):
    technologies = Technologies.objects.all()
    client_logos = Client_Logo.objects.all()
    reviews = ClientReview.objects.all() 
    projects = list(ProjectModel.objects.all())  # Convert QuerySet to list
    random.shuffle(projects)  # Shuffle the list
    projects = projects[:6] 

    if request.method == 'POST':
        id1 = request.POST.get('id1')
        pdf_url = generate_certificate_url(id1)
        if pdf_url:
            messages.success(request, "Your certificate has been successfully generated!")
            return render(request, 'certificate.html', {'pdf_url': pdf_url})
        else:
            messages.error(request, "Oops! No certificate found for the provided ID. Please try again.")
            return redirect('index')
    return render(request, 'index.html',{'technologies': technologies, 'client_logos' : client_logos, 'reviews':reviews,'projects': projects})

def generate_certificate_url(id):
    try:
        certificate = Certificates.objects.get(id1=id)
        return f'{settings.MEDIA_URL}{certificate.pdf_file}'
    except Certificates.DoesNotExist:
        return None

def about(request):
    technologies = Technologies.objects.all()
    client_logos = Client_Logo.objects.all()
    team_members = Team.objects.all()
    if request.method == 'POST':
        id1 = request.POST.get('id1')
        pdf_url = generate_certificate_url(id1)
        if pdf_url:
            return render(request, 'certificate.html', {'pdf_url': pdf_url})
        else:
            messages.error(request, ("Certificate not found for the provided ID!!!"))
            return redirect('about')
    return render(request, 'about.html',{'technologies': technologies, 'client_logos' : client_logos, 'team_members':team_members})

def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been successfully submitted.')
            return redirect('contact')
        else:
            messages.error(request, "Oops! Please try again.")
            return redirect('contact')
    else:
        form = ContactModelForm()
    return render(request, 'contact.html', {'form': form})

def portfolio(request):
    projects = ProjectModel.objects.all()
    return render(request,'portfolio.html', {'projects':projects})

def advertising(request):
    return render(request, 'advertising.html')

def web_development(request):
    return render(request, 'web_development.html')

def digital_marketing(request):
    return render(request, 'digital_marketing.html')

def trademark(request):
    return render(request, 'trademark.html')

def branding(request):
    return render(request, 'branding.html')

def it_solutions(request):
    return render(request, 'it_solutions.html')

def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')

def privacy_and_policy(request):
    return render(request, 'privacy_and_policy.html')

def careers(request):
    careers = Career_Model.objects.filter(post_end_date__gte=timezone.now())  # Fetch active jobs
    return render(request, 'careers.html', {'careers': careers})

def submit_application(request):
    job_positions = Career_Model.objects.all()
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been successfully submitted.')
            return redirect('careers')  # Redirect after successful submission
        else:
            messages.error(request, "Oops! Please try again.")
            return redirect('careers')
    else:
        form = CandidateForm()

    return render(request, 'careers.html', {'form': form, 'job_positions':job_positions})

def blog(request):
    blogs = Blog.objects.all().order_by('-created_date')
    return render(request, 'blog.html', {'blogs': blogs})

def blog_details(request, slug):  
    blog = get_object_or_404(Blog, slug=slug)  # Get blog by slug
    recent_posts = Blog.objects.exclude(id=blog.id).order_by('-created_date')[:6]  # Use blog.id instead of blog_id
    return render(request, 'blog_details.html', {'blog': blog, 'recent_posts': recent_posts})


# Admin Side
@csrf_protect
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, Admin!")
            return redirect('dashboard')
        else:   
            messages.error(request, "There was an error logging in, try again.")
            return redirect('user_login')
    return render(request, 'authenticate/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('user_login')


#  dashboard
@login_required(login_url='user_login')
def dashboard(request):
    return render(request,'admin_pages/dashboard.html')


# Contact 
@login_required(login_url='user_login')
def contact_view(request):
    contacts = ContactModel.objects.all().order_by('-id')
    return render(request,'admin_pages/contact_view.html',{'contacts':contacts})


@login_required(login_url='user_login')
def delete_contact(request,id):
    contact = ContactModel.objects.get(id=id)
    contact.delete()
    return redirect('contact_view')


# Client Reviews
@login_required(login_url='user_login')
def add_client_review(request):
    if request.method == 'POST':
        form = ClientReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews') 
    else:
        form = ClientReviewForm()

    return render(request, 'admin_pages/add_client_review.html', {'form': form})


@login_required(login_url='user_login')
def view_client_reviews(request):
    client_reviews = ClientReview.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_client_reviews.html', {'client_reviews': client_reviews})


@login_required(login_url='user_login')
def update_client_review(request, id):
    client_reviews = get_object_or_404(ClientReview, id=id)
    if request.method == 'POST':
        form = ClientReviewForm(request.POST, request.FILES, instance=client_reviews)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews')
    else:
        form = ClientReviewForm(instance=client_reviews)
    return render(request, 'admin_pages/update_client_review.html', {'form': form, 'client_reviews': client_reviews})

    

@login_required(login_url='user_login')
def delete_client_review(request,id):
    client_reviews = ClientReview.objects.get(id=id)
    client_reviews.delete()
    return redirect('view_client_reviews')


#  Client Logo
@login_required(login_url='user_login')
def add_clients_logo(request):
    if request.method == 'POST':
        form = Client_Logo_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_clients_logo') 
    else:
        form = Client_Logo_Form()

    return render(request, 'admin_pages/add_clients_logo.html', {'form': form})

@login_required(login_url='user_login')
def view_clients_logo(request):
    logo = Client_Logo.objects.all().order_by('-id')
    return render(request,'admin_pages/view_clients_logo.html',{'logo':logo})

@login_required(login_url='user_login')
def update_clients_logo(request,id):
    logos = get_object_or_404(Client_Logo, id=id)
    if request.method == 'POST':
        form = Client_Logo_Form(request.POST, request.FILES, instance=logos)
        if form.is_valid():
            form.save()
            return redirect('view_clients_logo')
    else:
        form = Client_Logo_Form(instance=logos)
    return render(request, 'admin_pages/update_clients_logo.html', {'form': form, 'logos': logos})

@login_required(login_url='user_login')
def delete_clients_logo(request,id):
    logos = Client_Logo.objects.get(id=id)
    logos.delete()
    return redirect('view_clients_logo')



#  Technologies
@login_required(login_url='user_login')
def add_technologies(request):
    if request.method == 'POST':
        form = TechnologiesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_technologies') 
    else:
        form = Client_Logo_Form()

    return render(request, 'admin_pages/add_technologies.html', {'form': form})

@login_required(login_url='user_login')
def view_technologies(request):
    logo = Technologies.objects.all().order_by('-id')
    return render(request,'admin_pages/view_technologies.html',{'logo':logo})

@login_required(login_url='user_login')
def update_technologies(request,id):
    logos = get_object_or_404(Technologies, id=id)
    if request.method == 'POST':
        form = TechnologiesForm(request.POST, request.FILES, instance=logos)
        if form.is_valid():
            form.save()
            return redirect('view_technologies')
    else:
        form = TechnologiesForm(instance=logos)
    return render(request, 'admin_pages/update_technologies.html', {'form': form, 'logos': logos})

@login_required(login_url='user_login')
def delete_technologies(request,id):
    logos = Technologies.objects.get(id=id)
    logos.delete()
    return redirect('view_technologies')



@login_required(login_url='user_login')
def add_blog_details(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_blog_details') 
    else:
        form = BlogForm()

    return render(request, 'admin_pages/add_blog_details.html', {'form': form})


@login_required(login_url='user_login')
def view_blog_details(request):
    blogs = Blog.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_blog_details.html', {'blogs': blogs})


@login_required(login_url='user_login')
def update_blog_details(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('view_blog_details')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'admin_pages/update_blog_details.html', {'form': form, 'blog': blog})

@login_required(login_url='user_login')
def delete_blog_details(request,id):
    blogs = Blog.objects.get(id=id)
    blogs.delete()
    return redirect('view_blog_details')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

@csrf_exempt
def ckeditor_upload(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        upload = request.FILES['upload']
        file_extension = os.path.splitext(upload.name)[1].lower()
        
        # Check if the uploaded file is an image or a PDF
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
            folder = 'images'
        elif file_extension == '.pdf':
            folder = 'pdfs'
        else:
            return JsonResponse({'uploaded': False, 'error': 'Unsupported file type.'})

        # Save the file in the appropriate folder
        file_name = default_storage.save(f'{folder}/{upload.name}', ContentFile(upload.read()))
        file_url = default_storage.url(file_name)
        return JsonResponse({
            'uploaded': True,
            'url': file_url
        })
    
    return JsonResponse({'uploaded': False, 'error': 'No file was uploaded.'})


    
#Team
@login_required(login_url='user_login')
def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_team') 
    else:
        form = TeamForm()

    return render(request, 'admin_pages/add_team.html', {'form': form})


@login_required(login_url='user_login')
def view_team(request):
    client_reviews = Team.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_team.html', {'client_reviews': client_reviews})


@login_required(login_url='user_login')
def update_team(request, id):
    client_reviews = get_object_or_404(Team, id=id)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=client_reviews)
        if form.is_valid():
            form.save()
            return redirect('view_team')
    else:
        form = TeamForm(instance=client_reviews)
    return render(request, 'admin_pages/update_team.html', {'form': form, 'client_reviews': client_reviews})

    

@login_required(login_url='user_login')
def delete_team(request,id):
    client_reviews = Team.objects.get(id=id)
    client_reviews.delete()
    return redirect('view_team')


#  404 view\
def page_404(request, exception):
    return render(request, '404.html', status=404)




# Portfolio 

@login_required(login_url='user_login')
def add_project(request):
    if request.method == 'POST':
        form = ProjectModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_projects') 
    else:
        form = ProjectModelForm()

    return render(request, 'admin_pages/add_project.html', {'form': form})

@login_required(login_url='user_login')
def view_projects(request):
    projects = ProjectModel.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_projects.html', {'projects': projects})

@login_required(login_url='user_login')
def update_projects(request, id):
    projects = get_object_or_404(ProjectModel, id=id)
    if request.method == 'POST':
        form = ProjectModelForm(request.POST, request.FILES, instance=projects)
        if form.is_valid():
            if 'remove_image' in request.POST:
                projects.project_image.delete() 
                projects.project_image = None 
            form.save()
            return redirect('view_projects')
    else:
        form = ProjectModelForm(instance=projects)
    return render(request, 'admin_pages/update_projects.html', {'form': form, 'projects': projects})

@login_required(login_url='user_login')
def delete_projects(request,id):
    projects = ProjectModel.objects.get(id=id)
    projects.delete()
    return redirect('view_projects')


# Certificate
@login_required(login_url='user_login')
def add_certificates(request):
    if request.method == 'POST':
        form = CertificatesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_certificates') 
    else:
        form = CertificatesForm()

    return render(request, 'admin_pages/add_certificates.html', {'form': form})

@login_required(login_url='user_login')
def view_certificates(request):
    certificates = Certificates.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_certificates.html', {'certificates': certificates})


@login_required(login_url='user_login')
def update_certificates(request,id):
    certificates = get_object_or_404(Certificates, id=id)
    if request.method == 'POST':
        form = CertificatesForm(request.POST, request.FILES, instance=certificates)
        if form.is_valid():
            form.save()
            return redirect('view_certificates')
    else:
        form = CertificatesForm(instance=certificates)
    return render(request, 'admin_pages/update_certificates.html', {'form': form, 'certificates': certificates})


@login_required(login_url='user_login')
def delete_certificates(request,id):
    certificates = Certificates.objects.get(id=id)
    certificates.delete()
    return redirect('view_certificates')


def category_website_detail(request, category_slug, website_slug):
    category = get_object_or_404(Category, slug=category_slug)

    # Ensure the category slug is correct
    correct_slug = slugify(category.name)
    if category.slug != correct_slug:
        return redirect('website_detail', category_slug=correct_slug, website_slug=website_slug)

    # Fetch website correctly
    website = get_object_or_404(Website, slug=website_slug, category=category)

    # Retrieve related services
    services = Service.objects.filter(website=website)

    return render(
        request,
        'website_detail.html',
        {'category': category, 'website': website, 'services': services}
    )





# addd Catgeoory
@login_required(login_url='user_login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_category') 
    else:
        form = CategoryForm()

    return render(request, 'admin_pages/add_category.html', {'form': form})

@login_required(login_url='user_login')
def view_category(request):
    categories = Category.objects.all().order_by('-id')
    return render(request, "admin_pages/view_category.html", {"categories": categories})




from django.utils.text import slugify

@login_required(login_url='user_login')
def update_category(request, id):
    category = get_object_or_404(Category, id=id)  # Fetch category by ID
    old_slug = category.slug  # Store old slug

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            updated_category = form.save(commit=False)
            updated_category.slug = slugify(updated_category.name)  # Generate new slug
            updated_category.save()

            # Redirect all related website URLs
            return redirect('view_category')

    else:
        form = CategoryForm(instance=category)

    return render(request, 'admin_pages/update_category.html', {'form': form, 'category': category})


@login_required(login_url='user_login')
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # ✅ Fetch category properly
    category.delete()
    return redirect("view_category")


# Websitee

@login_required(login_url='user_login')
def add_website(request):
    categories = Category.objects.all()

    if request.method == "POST":
        category_id = request.POST.get("category")
        name = request.POST.get("name")
        slug = request.POST.get("slug") or slugify(name)  # Ensure slug is generated
        meta_title = request.POST.get("meta_title")
        meta_description = request.POST.get("meta_description")
        description = request.POST.get("description")
        add_description = request.POST.get("add_description")
        image = request.FILES.get("image")

        # Ensure unique slug per category
        base_slug = slug
        counter = 1
        while Website.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        website = Website.objects.create(
            category_id=category_id,
            name=name,
            slug=slug,
            meta_title=meta_title,
            meta_description=meta_description,
            description=description,
            add_description=add_description,
            image=image,
        )

        # Handling multiple services
        service_headings = request.POST.getlist("service_heading[]")
        service_descriptions = request.POST.getlist("service_description[]")

        for heading, desc in zip(service_headings, service_descriptions):
            if heading.strip():
                Service.objects.create(website=website, heading=heading, description=desc)

        # messages.success(request, "Website and services added successfully!")
        return redirect(f"/{website.category.slug}/{website.slug}/")

    return render(request, "admin_pages/add_website.html", {"categories": categories})


@login_required(login_url='user_login')
def view_websites(request):
    websites = Website.objects.prefetch_related('services').all().order_by('-id')
    return render(request, 'admin_pages/view_website.html', {'websites': websites})

@login_required(login_url='user_login')
def update_website(request, website_id):
    website = get_object_or_404(Website, id=website_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        # Update website details
        website.category_id = request.POST.get('category')
        website.name = request.POST.get('name')
        website.slug = request.POST.get('slug')
        website.meta_title = request.POST.get('meta_title')
        website.meta_description = request.POST.get('meta_description')
        website.description = request.POST.get('description')
        website.add_description = request.POST.get('add_description')

        # Handle Image Upload
        if 'image' in request.FILES:
            website.image = request.FILES['image']

        website.save()

        # Clear existing services and add new ones
        website.services.all().delete()  # Delete old services
        service_headings = request.POST.getlist('service_heading[]')
        service_descriptions = request.POST.getlist('service_description[]')

        for heading, description in zip(service_headings, service_descriptions):
            if heading and description:  # Ensure fields are not empty
                Service.objects.create(website=website, heading=heading, description=description)

        # messages.success(request, "Website updated successfully!")
        return redirect('view_websites')  # Redirect to the view_websites page

    return render(request, 'admin_pages/update_website.html', {'website': website, 'categories': categories})

@login_required(login_url='user_login')
def delete_website(request, website_id):
    website = get_object_or_404(Website, id=website_id)
    website.delete()
    # messages.success(request, "Website deleted successfully!")
    return redirect('view_websites') 



@login_required(login_url='user_login')
def add_job_details(request):
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_job_details') 
    else:
        form = CareerForm()

    return render(request, 'admin_pages/add_job_details.html', {'form': form})

@login_required(login_url='user_login')
def view_job_details(request):
    job_details = Career_Model.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_job_details.html', {'job_details': job_details})

@login_required(login_url='user_login')
def update_job_details(request, id):
    job_details = get_object_or_404(Career_Model, id=id)
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES, instance=job_details)
        if form.is_valid():
            form.save()
            return redirect('view_job_details')
    else:
        form = CareerForm(instance=job_details)
    return render(request, 'admin_pages/update_job_details.html', {'form': form, 'job_details': job_details})


@login_required(login_url='user_login')
def delete_job_details(request,id):
    job_details = Career_Model.objects.get(id=id)
    job_details.delete()
    return redirect('view_job_details')

@login_required(login_url='user_login')
def view_candidate_details(request):
    certificates = Candidate.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_candidate_certificates.html', {'certificates': certificates})


@login_required(login_url='user_login')
def delete_candidate_certificates(request, id):
    candidate = get_object_or_404(Candidate, id=id)
    candidate.delete()
    return redirect('view_candidate_details')
