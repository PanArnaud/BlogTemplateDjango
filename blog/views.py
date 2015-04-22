from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    blog_list = Blog.objects.all().order_by('-posted')
    paginator = Paginator(blog_list, 1)

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    posts = Blog.objects.all().order_by('-posted')[:5]

    return render_to_response('index.html', {
        'blogs': blogs,
        'categories': categories,
        'posts': posts,
    })


def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug),
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })

