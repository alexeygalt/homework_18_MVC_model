from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, key):
        if len(key) == 0:
            return self.dao.get_all()
        elif key.get('genre_id'):
            return self.dao.get_by_genre(int(key.get('genre_id')))
        elif key.get('director_id'):
            return self.dao.get_by_director(int(key.get('director_id')))
        elif key.get('year'):
            return self.dao.get_by_year(int(key.get('year')))

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get('id')
        movie = self.get_one(mid)
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        self.dao.update(movie)
        return movie

    def update_partial(self, data):
        mid = data.get('id')
        movie = self.dao.get_one(mid)

        if "title" in data:
            movie.title = data.get('title')
        if "description" in data:
            movie.title = data.get('description')
        if "trailer" in data:
            movie.title = data.get('trailer')
        if "year" in data:
            movie.title = data.get('year')
        if "rating" in data:
            movie.title = data.get('rating')
        self.dao.update(movie)
        return movie

    def delete(self, mid):
        movie = self.dao.get_one(mid)
        if movie:
            self.dao.delete(movie)
            return movie
        return None


