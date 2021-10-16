from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests 



# Create your views here.
def HomeView(request):

    
        if 'search_input' in request.GET:
            search = request.GET.get('search_input')
        
            url = 'https://www.ask.com/web?q='+search 
            response = requests.get(url) 
            # convert text into editable format
            soup = bs(response.text, 'lxml')

            result_listings = soup.find_all('div', {'class': 'PartialSearchResults-item'})

            final_result = []

            for result in  result_listings:
                result_title = result.find(class_='PartialSearchResults-item-title').text
                result_url = result.find('a').get('href')
                result_description = result.find(class_='PartialSearchResults-item-abstract').text
                final_result.append((result_title,result_url,result_description))

            context = {'final_result':final_result,'search':search}
        
            return render(request,'results.html',context)
        else:
            return render(request,'index.html')


def ResultView(request):
    return render(request,'results.html')