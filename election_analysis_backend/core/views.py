from django.shortcuts import render
import csv
from django.http import JsonResponse

'''def query_csv(request):
    
    query = request.GET.get('query', None)
    flag = 0
    matched_tweets = []
    #print("the query received" + query)
    if query: 
        filename = 'core/Dummy_Tweets.csv'
        #with open('core/Dummy_Tweets.csv', newline='') as csvfile:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if query in row:
                    flag = 1
                    #response_data = {'result': row}
                    matched_tweets.append(row)
            if flag == 1 :
                response_data = {'result': matched_tweets}
        if flag == 0 :
            response_data = {'result': 'Not Found'}
    else:
        response_data = {'result': 'errorintesting'}

    
    
    return JsonResponse(response_data)'''

def query_csv(request):
    query = request.GET.get('query', None)
    matched_tweets = []
    if query:
        filename = 'core/Dummy_Tweets_2.csv'
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            flag = 0
            for row in reader:
                if query in row:
                    flag = 1
                    matched_tweets.append(row)

            if flag == 1 and len(matched_tweets) > 0:
                response_data = {'result': matched_tweets}
            else:
                response_data = {'result': 'Not Found'}
        return JsonResponse(response_data)
    else:
        response_data = {'result': 'error'}
        return JsonResponse(response_data)






# Create your views here.


