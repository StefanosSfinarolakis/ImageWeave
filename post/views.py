from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post, LikePost

# Create your views here.
# @login_required(login_url='signin')
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

# @login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)
    
    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.number_of_likes = post.number_of_likes+1
        post.save()
        return redirect('/home/')
    else:
        like_filter.delete
        post.number_of_likes = post.number_of_likes+1
        post.save()
        return redirect('/home/')

# @login_required(login_url='signin')
def upload(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/home/')

    else:
        return redirect('/home/')
    

    