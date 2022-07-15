from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView,ListView

class IndexView(ListView):
    model =Post
    template_name ='index.html'

def page_view(request, page_id):
    news =Post.objects.get(pk=page_id)
    context ={
        'news':news
    }
    return render(request, 'page_detail.html', context)

def cat_view(request, cat_id):
    cat_news =Categorie.objects.get(pk=cat_id)
    post_news =Post.objects.filter(Category=cat_news)
    #cat_title =Categorie.objects.all()
    context ={
        "cat_news":cat_news,
        "post_news":post_news
    }
    return render(request, 'cat_detail.html', context)
