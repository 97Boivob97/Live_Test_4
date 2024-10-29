from django.shortcuts import render, redirect
from .import forms
from .import models
from .models import Post
from categories.models import Category

def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    
    return redirect ('homepage')

def search_by_category(request):
    posts = Post.objects.all()  
    categories = Category.objects.all()  

    category_filter = request.GET.get('category')
    if category_filter:
        posts = posts.filter(category__name=category_filter)

    return render(request, 'search_by_category.html', {
        'posts': posts,
        'categories': categories,
        'category_filter': category_filter,
    })

def search_by_title(request):
    posts = Post.objects.all() 
    categories = Category.objects.all() 

    title_query = request.GET.get('title')  
    category_filter = request.GET.get('category')  

    if title_query:
        posts = posts.filter(title__icontains=title_query)  

    if category_filter:
        posts = posts.filter(category__id=category_filter) 

    return render(request, 'search_by_title.html', {
        'posts': posts,
        'categories': categories,
        'title_query': title_query,
        'category_filter': category_filter,
    })

