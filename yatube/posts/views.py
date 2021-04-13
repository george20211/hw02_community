from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})
