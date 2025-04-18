"""coders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import handler404
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import sitemap_view  # adjust import as needed


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('contact/', include('contact.urls')),
    path('faq/', include('faq.urls')),
    path('book/', include('book.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('sitemap.xml', sitemap_view, name='sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # this causes the media folder to work.  # noqa: E501


handler404 = 'coders.views.handler404'
