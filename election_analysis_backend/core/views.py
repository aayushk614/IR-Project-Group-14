from django.shortcuts import render
import csv
from django.http import JsonResponse

def query_csv(request):
    query = request.GET.get('query', None)
    #print("the query received" + query)
    if query:
        with open('Dummy_Tweets.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if query in row:
                    response_data = {'result': 'found'}
                    break
            else:
                response_data = {'result': 'not found'}
    else:
        response_data = {'result': 'errorintesting'}
    return JsonResponse(response_data)


# Create your views here.
