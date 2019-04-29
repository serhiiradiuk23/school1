from django.shortcuts import render
from blog.models import Post
# Create your views here.
from django.views.generic import ListView, DetailView

class PostListView(ListView):
	model = Post

class PostDetailView(DetailView):
	model = Post

	
		
