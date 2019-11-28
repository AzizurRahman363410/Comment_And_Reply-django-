from django.shortcuts import render, get_object_or_404,redirect
from . models import Post,Comment
from .forms import CommentForm
# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'home.html',context)
def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post, reply=None)
   
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.user = request.user

            reply_id =request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
                comment.reply = comment_qs
            comment.save()
            return redirect('detail', post.id)
    else:
        form = CommentForm()
    context = {
        'post':post,
        'form':form,
        'comments':comments
    }
    return render(request, 'detail.html',context)