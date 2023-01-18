from django.shortcuts import render, get_object_or_404
from blogapp.models import postdb, postab, sidepost, aboutme
from  .models import postdb
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render




# Create your views here.
def blog(request):
   blogpost_all = postdb.objects.all()
   about = postab.objects.all()
   side = sidepost.objects.all()
   aboutnew = aboutme.objects.all()

   paginator = Paginator(blogpost_all, 3)  # Show 5 posts per page
   page = request.GET.get('page')
   posts = paginator.get_page(page)

   return render(request, 'index.html', {'posts': posts,
                                         'about': about,
                                         'side': side,
                                         'aboutnew': aboutnew,
                                         'paginator': paginator})


def single(request,blogapp_id):
   singleblog=postdb.objects.get(id=blogapp_id)
   return render(request,'single.html',{'singleblog':singleblog})

def side(request, side_id):
   sideblog= sidepost.objects.get(id=side_id)
   return render(request,'side.html',{'sideblog':sideblog})

def about(request, about_id):
   aboutblog= aboutme.objects.get(id=about_id)
   return render(request,'about.html',{'aboutblog':aboutblog})




