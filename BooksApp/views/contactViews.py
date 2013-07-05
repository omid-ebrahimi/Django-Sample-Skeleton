__author__ = 'OMID EBRAHIMI'

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from BooksApp.forms import contactForms
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = contactForms.SignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['ebrahimi.omid69@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = contactForms.SignupForm(
            initial={'subject': 'I love your site!'}
        )
    return render_to_response('contact/contactUs.html', {'form': form}, context_instance=RequestContext(request))

def registerThanks(request):
    render_to_response('contact/contactThanks.html')