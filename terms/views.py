from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.http import JsonResponse
# Create your views here.
from .models import Keyword

class AllKeywordsListView(ListView):
    model = Keyword
    template_name ='terms/base.html'

class KeywordsListView(ListView):
    model = Keyword
    paginate_by = 5

def listing(request,page):
    keywords = Keyword.objects.all()
    paginator = Paginator(keywords, 10)
    keywords = paginator.get_page(page)
    context = {'keywords': keywords}
    return render(request,'terms/keyword_list.html',context)
    
def listing_api(request):
    page = request.GET.get('page',1)
    per_page = request.GET.get('per_page',4)
    start_with = request.GET.get('start_with',"")

    keywords = Keyword.objects.filter(name__startswith=start_with)

    paginator = Paginator(keywords, per_page)
    page_obj = paginator.get_page(page)
    payload = {
        "page":{
"current_page":page,
        "total": paginator.count,
        "has_next": page_obj.has_next(),
        "has_prev": page_obj.has_previous(),
        },
        "data": [{"name":keyword.name} for keyword in page_obj.object_list]
    }

    return JsonResponse(payload)