from django.http import HttpResponse
from django.shortcuts import render
import json
import data_analysis as da


def home(request):
    return render(request, 'test.html')


def stocks(request):
    data = json.dumps(da.typeahead(''))
    return HttpResponse(data, content_type='application/json')