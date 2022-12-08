from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name='home'),
    #path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('settings', views.settings, name='settings'),
    path('signup/', views.register, name='signup'),
    path('settings', views.settings, name = 'settings'),
    path('like-news', views.like_news, name = 'like-news'),
    path('search', views.search, name='search'),
    path('follow', views.follow, name = 'follow'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),  
]
# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_view

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('index/', views.index, name='index'),
#     #path('register/', views.register, name='register'),
#     path('profile/', views.profile, name='profile'),
#     path('settings', views.settings, name = 'settings'),
#     path('signup', views.register, name='signup'),
#     path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
#     path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
# ]


