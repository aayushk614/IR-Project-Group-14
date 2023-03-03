from django.shortcuts import render
import csv
from django.http import JsonResponse

def query_csv(request):
    
    query = request.GET.get('query', None)
    
    #print("the query received" + query)
    if query:
        flag = 0
        matched_tweets = []
        with open('core/Dummy_Tweets.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if query in row:
                    flag = 1
                    #response_data = {'result': row}
                    matched_tweets.append(row)
            if matched_tweets:
                response_data = {'result': matched_tweets}
    else:
        response_data = {'result': 'errorintesting'}

    if flag == 0 :
        response_data = {'result': 'Not Found'}
    
    return JsonResponse(response_data)


# Create your views here.


