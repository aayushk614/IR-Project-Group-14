from django.test import TestCase
from .similarity import find_similarity, cosine_similarity_new, find_similarity_vec
from .views import query_csv
import numpy as np
from django.http import HttpRequest

class SimilarityTests(TestCase):
    def test_find_similarity(self):
        tweet_list = [
            "The quick brown fox jumps over the lazy dog",
            "The lazy dog is jumped over by a quick brown fox",
            "I like to eat pizza",
            "Pizza is my favorite food",
            "The quick brown fox ate pizza"
        ]
        expected_result = np.array([
            [1.0, 0.7627700713964739, 0.0, 0.0, 0.6154574548966638],
            [0.7627700713964739, 1.0, 0.0, 0.1414213562373095, 0.5163977794943223],
            [0.0, 0.0, 1.0, 0.22360679774997896, 0.20412414523193154],
            [0.0, 0.1414213562373095, 0.22360679774997896, 1.0, 0.18257418583505539],
            [0.6154574548966638, 0.5163977794943223, 0.20412414523193154, 0.18257418583505539, 1.0]
        ])
        result = find_similarity(tweet_list)
        np.testing.assert_almost_equal(result, expected_result, decimal=5)

    def test_cosine_similarity_new(self):
        vec1 = np.array([1, 2, 3])
        vec2 = np.array([4, 5, 6])
        expected_result = 0.9746318461970762
        result = cosine_similarity_new(vec1, vec2)
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_find_similarity_vec(self):
        tweet_list = [
            "The quick brown fox jumps over the lazy dog",
            "The lazy dog is jumped over by a quick brown fox",
            "I like to eat pizza",
            "Pizza is my favorite food",
            "The quick brown fox ate pizza"
        ]
        expected_result = np.array([
            [1.0, 0.7627700713964739, 0.0, 0.0, 0.6154574548966638],
            [0.7627700713964739, 1.0, 0.0, 0.1414213562373095, 0.5163977794943223],
            [0.0, 0.0, 1.0, 0.22360679774997896, 0.20412414523193154],
            [0.0, 0.1414213562373095, 0.22360679774997896, 1.0, 0.18257418583505539],
            [0.6154574548966638, 0.5163977794943223, 0.20412414523193154, 0.18257418583505539, 1.0]
        ])
        result = find_similarity_vec(tweet_list)
        np.testing.assert_almost_equal(result, expected_result, decimal=5)

class ViewsTests(TestCase):
    def test_query_csv(self):
        request = HttpRequest()
        request.method = 'GET'
        request.GET['query'] = '1'
        response = query_csv(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json())
