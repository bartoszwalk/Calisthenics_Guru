from django.shortcuts import render
from youtubers.models import Youtuber
from pages.models import Page
from .forms import YoutuberForm
from django.http import HttpResponseRedirect

# Create your views here.

def youtuber_expanded(request, pk):
    youtuber = Youtuber.objects.get(pk=pk)
    page_list = Page.objects.all()
    context = {
        'youtuber': youtuber,
        'name': youtuber.title,
        'link': youtuber.link,
        'description': youtuber.description,
        'subscribers': youtuber.subscribers,
        'image': youtuber.image,
        'page_list': page_list,
    }
    return render(request, 'youtubers/youtuber_expanded.html', context)

def youtuber_basic(request):
    youtubers = Youtuber.objects.all()
    page_list = Page.objects.all()
    context = {
        'youtubers': youtubers,
        'page_list': page_list,
    }
    return render(request, 'youtubers/youtubers_index.html', context)

def add_youtuber(request):
    submitted = False
    page_list = Page.objects.all()
    if request.method == "POST":
        form = YoutuberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/youtubers/add_youtuber?submitted=True')

    else:
        form = YoutuberForm
        if 'submitted' in request.GET:
            submitted=True

    context = {
        'page_list': page_list,
        'form': form,
        'submitted':submitted
    }

    return render(request, 'youtubers/add_youtuber.html', context)



