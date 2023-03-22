from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
# @login_required(login_url='signin')
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

# @login_required(login_url='signin')
def upload(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/')

    else:
        return redirect('/')
    

    