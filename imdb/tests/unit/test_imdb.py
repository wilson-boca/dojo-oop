# -*- coding: utf-8 -*-

import unittest, os
from mock import mock

import imdb_domain

os.environ.update({
    'APP_SETTINGS': 'app.config.TestingConfig',
    'DATABASE_URL': 'postgresql+psycopg2://testeunitario:testeunitario@localhost/testeunitario-test',
    'API_TOKEN': 'AGRIMENSOR-API-TOKEN'
})


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

