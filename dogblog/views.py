from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from models.py import Dog, Competition, DogPhoto, LikePhoto 

# Create your views here.

class PostDetail(View):
    """ get request """
    def get(self, request, slug, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "like_details.html",
            {
                "post": post,
                "liked": liked
            },
            )
