from django.shortcuts import render
import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup

# Create your views here.

CRAIGSLIST_URL = "https://delhi.craigslist.org/search/sss?query={}"
CRAIGSLIST_IMG_URL= "https://images.craigslist.org/{}_300x300.jpg"
def home(request):
    return render(request, 'base.html')

def search(request):
    final_url = CRAIGSLIST_URL.format(quote_plus(request.POST.get('search')))
    response = requests.get(final_url)
    soup = BeautifulSoup(response.text, features='html.parser')

    post_listings = soup.find_all('li',{'class':'result-row'})

    final_postings = []
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if (post.find(class_ = 'result-image').get('data-ids')):
            post_image = post.find(class_ = 'result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = CRAIGSLIST_IMG_URL.format(post_image)
        else:
            post_image_url = "https://craigslist.org/images/peace.jpg"    

        final_postings.append((post_title,post_url,post_image_url))

    item_values = {
        "search_content" : request.POST.get('search'),
        "final_postings" : final_postings,
    }

    return render(request, 'myapp/search.html', item_values)    
