from django.shortcuts import render
import csv
from django.http import JsonResponse

from .similarity import *
import numpy as np 


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
    each_tweet = []
    tweets_list = []
    column_name = 'Id'
    
    array = [[1.65,2,3,4],[1,3,4,5],[2,4,5,6]]
    if query:
        filename = 'core/Dummy_Tweets_hashtags3.csv'
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
            
            #Finding similarity between fetched tweets (passing tweet_list variable)
            similarity_matrice = find_similarity_vec(tweet_list = tweets_list)

            #Rouding off decimal values to 3DP.
            similarity_matrice_rounded = np.round(similarity_matrice, 3)

            idx_col = np.arange(similarity_matrice_rounded.shape[0]).reshape(-1, 1)
            new_similarity_matrice = np.hstack([idx_col+1, similarity_matrice_rounded])
            new_sim_matrix_list = new_similarity_matrice.tolist()

            matched_tweets.append(new_sim_matrix_list)
            

            if flag == 1 and len(matched_tweets) > 0:
                response_data = {'result': matched_tweets}
            else:
                response_data = {'result': 'Not Found'}

        return JsonResponse(response_data)
    else:
        response_data = {'result': tweets_list}
        return JsonResponse(response_data)






