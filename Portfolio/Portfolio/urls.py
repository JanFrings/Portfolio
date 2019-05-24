"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),

    path('portfolio', views.PortfolioView.as_view(), name='portfolio_index'),
    path('Projects/', views.ProjectsView.as_view(), name='projects'),

    path('nfl/', include('nfl.urls')),
    path('blog/', include('blog.urls')),
    path('emailcontact/', include('emailcontact.urls')),

    path('blog/register/', include('django.contrib.auth.urls')),
    path('test/', views.TestView.as_view(), name='test'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('resume/download/eng', views.resume_download_english, name='resume_download_eng'),
    path('resume/download/ger', views.resume_download_german, name='resume_download_ger'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
