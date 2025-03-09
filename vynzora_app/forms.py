from django import forms
from .models import ContactModel, ClientReview, Client_Logo, Technologies, Blog, Team, ProjectModel, Certificates



# Contact us
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

# Clien Review
class ClientReviewForm(forms.ModelForm):
    class Meta:
        model = ClientReview
        fields = '__all__'

# Clients Logo
class Client_Logo_Form(forms.ModelForm):
    class Meta:
        model = Client_Logo
        fields = '__all__'

# Technologies
class TechnologiesForm(forms.ModelForm):
    class Meta:
        model = Technologies
        fields = '__all__'


# Blog
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

# Team
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


# Portfolio 

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = '__all__'

# Certificate

class CertificatesForm(forms.ModelForm):
    class Meta:
        model = Certificates
        fields = '__all__'