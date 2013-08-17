from django.http import HttpResponse
from django.shortcuts import render
import json
import data_analysis as da


def home(request):
    return render(request, 'test.html')


def stocks(request, symbol):
    data = json.dumps(da.getSymbolData(symbol))
    return HttpResponse(data[1:-1], content_type='application/json')