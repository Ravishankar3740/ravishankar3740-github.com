from django.shortcuts import render,get_object_or_404
from .models import *
from .forms import *
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here@login_required(login_url='/accounts/login')
@login_required(login_url='/jobs/login')
def allblogs(request):
    blogs = Blog.objects
    return render(request,'blog/allblogs.html', {"blogs":blogs} )
    
@login_required(login_url='/jobs/login')
def detail(request,blog_id):
    blogdetail =get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html', {'blog':blogdetail} )

@login_required(login_url='/jobs/login')
def enquiry(request):
    return render(request,'blog/enquiry.html')

@login_required(login_url='/jobs/login')
@csrf_exempt
def inquiry(request):
    if request.method == 'POST':
        form=Detail(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/blog/Twitter/")
    else:
        form=Data()
    return render(request,'blog/data.html',{'form':form})
