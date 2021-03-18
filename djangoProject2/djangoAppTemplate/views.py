from django.shortcuts import render
from django.http import HttpResponse
from djangoAppTemplate.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request, 'djangoAppTemplate/index.html', context=date_dict)

def help(request):
    help_dict = {'help_insert':'Now I am coming from djangoAppTemplate/help.html!'}
    return render(request, 'djangoAppTemplate/help.html', context=help_dict)