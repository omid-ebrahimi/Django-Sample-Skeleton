from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from BooksApp.models import Book
from BooksApp.forms import bookForms

def search(request):
    if request.method == 'POST':
        form = bookForms.SearchForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            books = Book.objects.filter(title__icontains=cd['title'])
            return render_to_response('book/search_results.html', {'books': books, 'query': cd['title']})
        else:
            return render_to_response('book/search.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = bookForms.SearchForm()
        return render_to_response('book/search.html', {'form': form}, context_instance=RequestContext(request))
