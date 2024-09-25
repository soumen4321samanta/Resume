from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get cleaned data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Create the email content
            subject = f"Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Send the email
            send_mail(subject, body, email, [settings.ADMIN_EMAIL], fail_silently=False)

            # Redirect or show a success message
            return redirect('success_page')  # You can create a success page
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})