from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

def search(request):
    item_values = {
        "search_content" : request.POST.get('search')
    }
    return render(request, 'myapp/search.html', item_values)    
