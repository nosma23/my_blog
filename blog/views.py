from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

def index(request):
    return render(request, 'index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all().order_by("-posted")[:5]
    })

def view_post(request, slug):
    return render(request, 'view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })


def about_page(request):
    return render(request, 'about.html')


def contact(request):

    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the contact information
            template = get_template('contact_template.txt')
            context = Context({
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
            "New contact form submission",
            content,
            "lifeproficiency.com" + '',
            ['manos@lifeproficiency.com'],
            headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'contactform_form.html', {
        'form': ContactForm,
    })
