# get post put delete
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid: int):
        return self.session.query(Movie).get(mid)

    def get_by_director(self, director_id):
        return self.session.query(Movie).filter_by(director_id=director_id).all()

    def get_by_genre(self, genre_id):
        return self.session.query(Movie).filter_by(genre_id=genre_id).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter_by(year=year).all()

    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()
