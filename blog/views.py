from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Blog, Category
from .forms import ContactForm

def index(request):
    queryset_list = Blog.objects.filter(publish__lte=timezone.now()).order_by("-posted")
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(Q(title__icontains=query) | Q(body__icontains=query)).distinct()
    paginator = Paginator(queryset_list, 5)  # Show 5 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {
        'categories': Category.objects.all(),
        'posts': queryset,
        'page_request_var': page_request_var
    })

def view_post(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    context = {'post': post, }
    return render(request, 'view_post.html', context)


def about_page(request):
    return render(request, 'about.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the contact information

            subject = 'Site contact form'
            from_email = settings.EMAIL_HOST_USER
            to_email = ['manos@lifeproficiency.com']
            contact_message = '%s: %s via %s' % (
                contact_name,
                form_content,
                contact_email)
            send_mail(subject,
                      contact_message,
                      from_email,
                      to_email, fail_silently=True)

    return render(request, 'contactform_form.html', {
        'form': form,
    })
