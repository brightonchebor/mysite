from django.shortcuts import render, get_object_or_404 
from .models import Post, Comment
from .forms import NewCommentForm

# Create your views here.
def home(request):

    all_posts = Post.newmanager.all()

    return render(request, 'index.html', {'posts': all_posts})

def post_single(request, post):

    post = get_object_or_404(Post, slug=post, status='published')
    comments = post.comments.flter(status=True)
    user_comment = None

    if request.method == "POST":
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)




    