from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
from django.forms import PasswordInput
from django.contrib.auth.models import User,auth
from . models import ProfileSetting,Profile
import profile
#API_KEY='6bb8ca8426ee4ae3b16be1246f0e2934'
API_KEY='d0b69496c18e463f888a273cb521ea9f'

def home(request):
    return render(request, 'users/home.html')



# def register(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Hi {username}, your account was created successfully')
#             return redirect('home')
#     else:
#         form = UserRegisterForm()

#     return render(request, 'users/register.html', {'form': form})
# def register(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')            
#             #user = User.objects.create_user(username=username)
            
#             #email = form.cleaned_data.get('email')
#             messages.success(request, f'Hi {username}, your account was created successfully')
#             user_model = User.objects.get(username=username)
#             new_profile = Profile.objects.create(user = user_model, id_user=user_model.id)
#             new_profile.save()
#             return redirect('settings')
#     else:
#         form = UserRegisterForm()


#     return render(request, 'users/register.html',{'form':form})

# def signup(request):

#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']

#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email Taken')
#                 return redirect('signup')
#             elif User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username Taken')
#                 return redirect('signup')
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save()

#                 #log user in and redirect to settings page
#                 user_login = auth.authenticate(username=username, password=password)
#                 auth.login(request, user_login)

#                 #create a Profile object for the new user
#                 user_model = User.objects.get(username=username)
#                 new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
#                 new_profile.save()
#                 return redirect('settings')
#         else:
#             messages.info(request, 'Password Not Matching')
#             return redirect('signup')
        
#     else:
#         return render(request, 'users/register.html')


@login_required()
def profile(request):
    return render(request, 'users/profile.html')

 
def index(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    user_profile = ProfileSetting.objects.get(user=request.user.id)
    preference = user_profile.Category
    preference_c = user_profile.location
  

 


    if country and category:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={API_KEY}'
        cr_news= requests.get(url).json()
        a = cr_news['articles']
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        cr_news= requests.get(url).json()
        a = cr_news['articles']
    elif preference or preference_c:
        url = f'https://newsapi.org/v2/top-headlines?category={preference}&country={preference_c}&apiKey={API_KEY}'
        cr_news= requests.get(url).json()
        a = cr_news['articles']
    elif country:
         url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
         cr_news= requests.get(url).json()
         a = cr_news['articles'] 
    else:
        url="https://newsapi.org/v2/everything?q=Top&from=2022-11-10&sortBy=popularity&apiKey=6bb8ca8426ee4ae3b16be1246f0e2934"
        cr_news= requests.get(url).json()
        a=cr_news['articles']


    # url="https://newsapi.org/v2/everything?q=Top&from=2022-11-10&sortBy=popularity&apiKey=6bb8ca8426ee4ae3b16be1246f0e2934"

    description=[]
    img=[]
    title=[]
    url=[]
    # author=[]
    # publishat=[]
    # name=[]

    for i in range(len(a)):
        f=a[i]
        title.append(f['title'])
        description.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    #     author.append(f['author'])
    #     publishat.append(f['publishedAt'])
    #     name.append(f['source.name'])
        

    listofnews=zip(title,description,img,url)
    context = {'mylist':listofnews}
    return render(request,'users/home.html',context)


# def settings(request):

#     user_profile = Profile.objects.get(user=request.user)

#     if request.method == 'POST':
        
#         if request.FILES.get('image') == None:
#             image = user_profile.profileimg
#             bio = request.POST['bio']
#             location = request.POST['location']

#             user_profile.profileimg = image
#             user_profile.bio = bio
#             user_profile.location = location
#             user_profile.save()
#         if request.FILES.get('image') != None:
#             image = request.FILES.get('image')
#             bio = request.POST['bio']
#             location = request.POST['location']

#             user_profile.profileimg = image
#             user_profile.bio = bio
#             user_profile.location = location
#             user_profile.save()
        
#         return redirect('settings')
#     return render(request, 'users/setting.html', {'user_profile':user_profile})


def settings(request):

    user_profile = ProfileSetting.objects.get(user=request.user.id)

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            Category = request.POST['Category']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.Category = Category
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']
            Category = request.POST['Category']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.Category = Category
            user_profile.save()
        
        return redirect('settings')
    return render(request, 'users/setting.html', {'user_profile': user_profile})

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                #user.save(commit = True)

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = ProfileSetting.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('home')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'users/signup.html')         

def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile':profile}
    return render(request,'profile.html',context)

def invite_received_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invitations_received(profile)
    result = list(map(lambda x: x.sender, qs)) 
    is_empty = False
    if len(result) == 0:
        is_empty = True
    context = {'is_empty':is_empty,
        'qs':result}
    print(context)
    return render(request, 'myinvites.html', context )