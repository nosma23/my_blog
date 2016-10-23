from blog.views import index, view_post, about_page, contact
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse

app_name = 'blog'

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$', index, name='index'),

    url(r'^about/$', about_page, name='about'),

    url(r'contact/$', contact, name='contact'),

    url(r'(?P<slug>[^\.]+)/$', view_post, name='view_blog_post'),

    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"), name="robots_file"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)