
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.shortcuts import render
from . models import Page
from .contact import ContactForm

def index(request, pagename=''):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'page_list': Page.objects.all()
    }
    return render(request, 'pages/pages.html', context)

def contact(request):
	submitted = False
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'b.walkowiak2@mail.dcu.ie'),
				['b.walkowiak2@mail.dcu.ie'], # change this
				connection=con
			)
			return HttpResponseRedirect('/contact?submitted=True')
	else:
		form = ContactForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form': form,
		'page_list': Page.objects.all(),
		'submitted': submitted
	}
	return render(request, 'pages/contact.html', context)

def home(request):
	context = {
		'page_list': Page.objects.all()
	}
	return render(request, 'pages/home.html', context)
