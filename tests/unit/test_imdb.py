# -*- coding: utf-8 -*-

import unittest, os, mock
from imdb import imdb_domain

os.environ.update({
    'APP_SETTINGS': 'app.config.TestingConfig',
    'DATABASE_URL': 'postgresql+psycopg2://testeunitario:testeunitario@localhost/testeunitario-test',
    'API_TOKEN': 'AGRIMENSOR-API-TOKEN'
})

# ASSERTS https://docs.python.org/2.7/library/unittest.html#unittest.TestCase.debug


class TestCase(unittest.TestCase):
    mock = mock


class TestMovie(TestCase):

    def test_create_movie_with_empty_dict(self):
        dict_movie = {}
        instance = imdb_domain.Movie.create_movie_with_dict(dict_movie)
        self.assertIsInstance(instance, imdb_domain.Movie)

    def test_create_movie_with_dict_assert_year(self):
        dict_movie = {
            'year': 1976
        }
        instance = imdb_domain.Movie.create_movie_with_dict(dict_movie)
        self.assertIsInstance(instance, imdb_domain.Movie)
        self.assertEqual(instance.year, dict_movie['year'])

    @TestCase.mock.patch('imdb.imdb_domain.requests.get')
    def test_availale_on_netflix_mocking_get(self, mocked_get):
        dict_movie = {
            'name': 'Wherever you want'
        }
        instance = imdb_domain.Movie.create_movie_with_dict(dict_movie)
        mocked_get.return_value.ok = True
        mocked_get.return_value.text = 'It Works Man'
        result = instance.is_available_on_netflix(instance.name)
        self.assertEqual(result, 'It Works Man')
        mocked_get.assert_called_with('http://www.google.com')
        mocked_get.assert_called()

    @TestCase.mock.patch('imdb.imdb_domain.Movie.http_call')
    def test_availale_on_netflix_mocking_http_call(self, mocked_http_call):
        dict_movie = {
            'name': 'Wherever you want'
        }
        instance = imdb_domain.Movie.create_movie_with_dict(dict_movie)
        mocked_http_call.return_value = 'It Works Man'
        result = instance.is_available_on_netflix(instance.name)
        self.assertEqual(result, 'It Works Man')
        mocked_http_call.assert_called()
