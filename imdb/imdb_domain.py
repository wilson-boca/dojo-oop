class Movie(object):

    @classmethod
    def create_movie_with_dict(cls, movie_dict):
        movie = cls()
        movie._year = movie_dict.get('year')
        movie._genres = movie_dict.get('genres')
        movie._name = movie_dict.get('name')
        movie._stars = movie_dict.get('stars')
        movie._writers = movie_dict.get('writers')
        movie._cast = movie_dict.get('cast')
        return movie

    def __init__(self):
        self._year = None
        self._genres = []
        self._name = None
        self._stars = []
        self._writers = []
        self._cast = []

    @property
    def year(self):
        return self._year

    @property
    def name(self):
        return self._name

    @property
    def genres(self):
        return self._genres

    @property
    def stars(self):
        return self._stars

    @property
    def writers(self):
        return self._writers

    @property
    def cast(self):
        return self._cast

