from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Articles
from .forms import CommentForm


class ArticlesList(generic.ListView):
    queryset = Articles.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/home.html'



class ArticlesDetail(generic.DetailView):
    model = Articles
    slug_field = 'blog_slug'
    slug_url_kwarg = 'blog_slug'
    template_name = 'blog/details.html'
 



# def home(request):
     


# def about(request):
#     return render(request,'blog/about.html',context=None)
