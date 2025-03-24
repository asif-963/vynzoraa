from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # User Side
    path('', views.index, name= 'index'),
    path('about', views.about, name= 'about'),
    path('portfolio', views.portfolio, name= 'portfolio'),
    path('contact', views.contact, name= 'contact'),
    path('advertising', views.advertising, name= 'advertising'),
    path('web-development', views.web_development, name= 'web_development'),
    path('digital-marketing', views.digital_marketing, name= 'digital_marketing'),
    path('trademark', views.trademark, name= 'trademark'),
    path('branding', views.branding, name= 'branding'),
    path('it-solutions', views.it_solutions, name= 'it_solutions'),
    path('privacy-and-policy', views.privacy_and_policy, name= 'privacy_and_policy'),
    path('terms-and-conditions', views.terms_and_conditions, name= 'terms_and_conditions'),

    path('careers/', views.careers, name= 'careers'),
    path('submit_application/', views.submit_application, name='submit_application'),

    path('view_candidate_details',views.view_candidate_details,name='view_candidate_details'),
    path('delete_candidate_certificates/<int:id>',views.delete_candidate_certificates,name='delete_candidate_certificates'),
    
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_details, name='blog_details'),

    # Admin Side
     # Admin Login
    path('login',views.user_login,name='user_login'),
    path('logout-user', views.logout_user, name='logout_user'),

    # admin dashboard
    path('dashboard',views.dashboard,name='dashboard'),

     # Contact us
    path('contact-view',views.contact_view,name='contact_view'),
    path('delete-contact/<int:id>/',views.delete_contact,name='delete_contact'),

        # client reviews
    path('add-client-review',views.add_client_review,name='add_client_review'),
    path('view-client-reviews',views.view_client_reviews,name='view_client_reviews'),
    path('update-client-review/<int:id>/',views.update_client_review,name='update_client_review'),
    path('delete-client-review/<int:id>/',views.delete_client_review,name='delete_client_review'),

        # clients logo
    path('add-clients-logo',views.add_clients_logo,name='add_clients_logo'),
    path('view-clients-logo',views.view_clients_logo,name='view_clients_logo'),
    path('update-clients-logo/<int:id>/',views.update_clients_logo,name='update_clients_logo'),
    path('delete-clients-logo/<int:id>/',views.delete_clients_logo,name='delete_clients_logo'),

        # Technologies 
    path('add_technologies',views.add_technologies,name='add_technologies'),
    path('view_technologies',views.view_technologies,name='view_technologies'),
    path('update_technologies/<int:id>/',views.update_technologies,name='update_technologies'),
    path('delete_technologies/<int:id>/',views.delete_technologies,name='delete_technologies'),

        # Blogs
    path('add_blog_details', views.add_blog_details, name='add_blog_details'),
    path('view_blog_details',views.view_blog_details,name='view_blog_details'),
    path('update_blog_details/<int:id>/',views.update_blog_details,name='update_blog_details'),
    path('delete_blog_details/<int:id>/',views.delete_blog_details,name='delete_blog_details'),

     path('ckeditor_upload/', views.ckeditor_upload, name='ckeditor_upload'),

    # Team
    path('add_team',views.add_team,name='add_team'),
    path('view_team',views.view_team,name='view_team'),
    path('update_team/<int:id>/',views.update_team,name='update_team'),
    path('delete_team/<int:id>/',views.delete_team,name='delete_team'),

    #portfolio
     path('add_project',views.add_project,name='add_project'),
    path('view_projects',views.view_projects,name='view_projects'),
    path('update_projects/<int:id>/',views.update_projects,name='update_projects'),
    path('delete_projects/<int:id>/',views.delete_projects,name='delete_projects'),

    # Certificate
    path('add_certificates',views.add_certificates,name='add_certificates'),
    path('view_certificates',views.view_certificates,name='view_certificates'),
    path('update_certificates/<int:id>/',views.update_certificates,name='update_certificates'),
    path('delete_certificates/<int:id>/',views.delete_certificates,name='delete_certificates'),

    # Webb sites
    # Category URLs first (avoid conflicts with slugs)
    path("add-category/", views.add_category, name="add_category"),
    path("view-category/", views.view_category, name="view_category"),
    path('update-category/<int:id>/', views.update_category, name='update_category'),
    path("delete-category/<int:category_id>/", views.delete_category, name="delete_category"),

   

    path('add-website/', views.add_website, name='add_website'),
    path("view-website/", views.view_websites, name="view_websites"),
    path('update-website/<int:website_id>/', views.update_website, name='update_website'),
    path('delete-website/<int:website_id>/', views.delete_website, name='delete_website'), 

    # jobs 
    path('add-job-details',views.add_job_details,name='add_job_details'),
    path('view-job-details',views.view_job_details,name='view_job_details'),
    path('update-job-details/<int:id>',views.update_job_details,name='update_job_details'),
    path('delete-jobdetails/<int:id>',views.delete_job_details,name='delete_job_details'),
 
    path('<slug:category_slug>/<slug:website_slug>/', views.category_website_detail, name='website_detail'),

    # Website details (should come last)
    





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'vynzora_app.views.page_404'
