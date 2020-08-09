from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def home(request):
    return render(request,'home.html')

def blog(request):
    return render(request,'demo/index.html')
# def post_list(request):
#     postd = Post.publish.all()
#     return render(request,'list.html',{'posts':posts})

# def post_details(request,year,month,day,post):
#     post = get_object_or_404(Post, slug=post,
#                                     status='published',
#                                     publish__year=year,
#                                     publish__month=month,
#                                     publish__day=day)
#     return render(request,'detail.html',{'post':post})