from django.shortcuts import render
import csv
from django.http import JsonResponse
from .similarity import *
import numpy as np 


def query_csv(request):
    
    query = request.GET.get('query', None)
    matched_tweets = []
    each_tweet = []
    tweets_list = []
    column_name = 'Id'
    
    array = [[1.65,2,3,4],[1,3,4,5],[2,4,5,6]]
    if query:
        filename = 'core/Final_Tweet_Dataset.csv'
        with open(filename, 'r') as csvfile:
            #reader = csv.reader(csvfile)
            reader = csv.DictReader(csvfile)
            flag = 0
            for row in reader:
                #if query in row:
                if row[column_name] == query:
                    flag = 1
                    for key in row:
                        #print(key)
                        each_tweet.append(row.get(key))
                    matched_tweets.append(each_tweet)
                    tweets_list.append(row.get('Tweet'))
                each_tweet = []

            
            # replacing the empty entries with N/A

            for i in range(0 , len(matched_tweets)) :
                for j in range(0 , len(matched_tweets[i])):
                    #print(len(ans[i][j]))
                    if len(matched_tweets[i][j]) == 0 :
                        matched_tweets[i][j] = 'N/A'
            
            #Finding similarity (pass tweet_list variable)
            similarity_matrice = find_similarity(tweet_list= tweets_list)
            import numpy as np

            similarity_matrice_rounded = np.round(similarity_matrice, 3)

            idx_col = np.arange(similarity_matrice_rounded.shape[0]).reshape(-1, 1)
            new_similarity_matrice = np.hstack([idx_col+1, similarity_matrice_rounded])
            arr1 = new_similarity_matrice.tolist()
            

            matched_tweets.append(arr1)
            

            if flag == 1 and len(matched_tweets) > 0:
                response_data = {'result': matched_tweets}
            else:
                response_data = {'result': 'Not Found'}

        return JsonResponse(response_data)
    else:
        response_data = {'result': tweets_list}
        return JsonResponse(response_data)






# Create your views here.


