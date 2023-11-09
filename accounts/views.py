from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
import requests
from .forms import BlogForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .models import Blog
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import BlogSerializer, BlogCreateSerializer
 


# Create your views here.

# This is a home view
@login_required
def home(request):
    # Fetch news articles from the API
    api_key = 'fd95e85fc5e54fa4a6c06611ffcbd0e3' 
    api_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(api_url)
    blogs = Blog.objects.all()
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        
    else:
        articles = []

    return render(request, 'base.html', {'articles': articles,'blogs': blogs})

    

#This is the register form
#rounak, rounakpatel
def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully.')
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
          
            
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#logout views
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

#article detail

def article_detail(request, article_url):
    # You can fetch the article content from the original source or API based on the article URL.
    # For simplicity, let's pass the article URL to the template.
    return render(request, 'article_detail.html', {'article_url': article_url})


#new blog form
@login_required
def create_blog(request):
    print("User:", request.user)
    
    if request.method == 'POST':
        print("POST request received")
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            print("Blog created successfully")
            return redirect('home')
    else:
        print("GET request received")
        form = BlogForm()

    return render(request, 'create_blog.html', {'form': form})


#delete blog

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    # Ensure the logged-in user is the owner of the blog
    if request.user == blog.user:
        blog.delete()

    return redirect('dashboard')  # Redirect to the dashboard after successful deletion
#dashboard
@login_required
def blog_dashboard(request):
    blogs = Blog.objects.filter(user=request.user)  
    return render(request, 'dashboard.html',{'blogs': blogs})

#serializers
class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUser]

class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUser]

class BlogListAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = BlogSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BlogCreateSerializer
        return BlogSerializer
