"""authsysproject URL Configuration

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
# from django.contrib import admin
# from django.urls import path, include

# from django.views.generic import TemplateView
# from django.contrib.auth.views import LogoutView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('users.urls')),
#     path('', TemplateView.as_view(template_name="home.html")),
#     path('accounts/', include('allauth.urls')),
#     path('logout', LogoutView.as_view())
# ]
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', TemplateView.as_view(template_name="home.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('oauth/', include('social_django.urls', namespace='social')),

   
    # path('searchnews',views.searchnews, name = 'searchnews'),
    path('myprofile',views.my_profile, name='myprofile'),
    path('myinvites',views.invite_received_view, name = 'myinvites'),
    path('allprofiles/',views.ProfileListView.as_view(),name = 'allprofileview'),
    path('toinvitelist', views.invite_profile_list_view,name = 'toinvitelist'),
    path('sendinvite', views.send_invitation,name = 'sendinvite'),
    path('removefriend', views.remove_friends,name = 'removefriend'),
    path('myinvites/accept',views.accept_invitation, name = 'accept_invite'),
    path('myinvites/reject',views.reject_invitation, name = 'reject_invite'),


]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)