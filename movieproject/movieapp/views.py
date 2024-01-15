from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Movie



# Create your views here.
def index(request):
    obj=Movie.objects.all()
    return render (request,"index.html",{'movie_list':obj})
def detail(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie})
def add_movie(request):
    if request.method=="POST" :
        name = request.POST.get('name_h',)
        desc = request.POST.get('desc_h', )
        year = request.POST.get('year_h', )
        img = request.FILES['img_h']
        movie = Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,id):
    if request.method=='POST':
        movie= Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')


