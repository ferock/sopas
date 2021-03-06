"""AquiSopas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconfw
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from .app import application
from django.conf import settings
from paybac.views import *

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url(r'^redirect/', RedirectView.as_view(), name='gocardless-redirect'),
    url(r'^confirm/', ConfirmView.as_view(), name='gocardless-response'),
    url(r'^cancel/', CancelView.as_view(), name='gocardless-cancel'),
    url(r'', include(application.urls)),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
