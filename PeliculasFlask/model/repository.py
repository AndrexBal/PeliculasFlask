from model.entity import Movie, Review
from model.db import execute, commit


class MovieRepository:
    def insert(movie: Movie) -> None:
        sql = f"""
                INSERT INTO Movie (code, name, image_url, year)
                VALUES ('{movie.code}', '{movie.name}', '{movie.image_url}', {movie.year});
               """
        cursor = execute(sql)
        cursor.close()
        commit()

    def findByCode(code: str) -> Movie:
        sql = f"""
                SELECT code, name, image_url, year
                FROM Movie
                WHERE code = '{code}';
               """
        cursor = execute(sql)
        result = cursor.fetchone()  # ('a1','Matrix','htt...',2000)
        cursor.close()

        return Movie(
            code=result[0],
            name=result[1],
            image_url=result[2],
            year=result[3])

    def findAll() -> list:
        sql = """
                SELECT code, name, image_url, year
                FROM Movie
                ORDER BY name
              """
        cursor = execute(sql)
        # [('a1','Matrix','htt...',2000),('b2','El resplandor','http....',2005),()]
        result = cursor.fetchall()
        cursor.close()

        response = list()
        for data in result:
            response.append(Movie(
                code=data[0],
                name=data[1],
                image_url=data[2],
                year=data[3]))

        return response


class ReviewRepository:
    def insert(review: Review) -> None:
        sql = f"""
                INSERT INTO Review (name, email, description, rating, code)
                VALUES ('{review.name}', '{review.email}', '{review.description}', {review.rating}, '{review.code}');
               """
        cursor = execute(sql)
        cursor.close()
        commit()

    def findById(id: int) -> Review:
        sql = f"""
                SELECT id, name, email, description, rating, code
                FROM Review
                WHERE id = {id};
               """
        cursor = execute(sql)
        result = cursor.fetchone()
        cursor.close()

        return Review(
            id=result[0],
            name=result[1],
            email=result[2],
            description=result[3],
            rating=result[4],
            movie_code=result[5])

    def findByMovieCode(movie_code: str) -> list:
        sql = f"""
               SELECT id, name, email, description, rating, code
                FROM Review
                WHERE code = '{movie_code}';
              """
        cursor = execute(sql)
        result = cursor.fetchall()
        cursor.close()

        response = list()
        for data in result:
            response.append(Review(
                id=data[0],
                name=data[1],
                email=data[2],
                description=data[3],
                rating=data[4],
                movie_code=data[5]))

        return response

    def update(review: Review) -> None:
        sql = f"""
                UPDATE Review
                SET name = '{review.name}',
                    email = '{review.email}',
                    description = '{review.description}',
                    rating = {review.rating},
                    code = '{review.code}'
                WHERE id = {review.id};
               """
        cursor = execute(sql)
        cursor.close()
        commit()

    def delete(id: int) -> None:
        sql = f"""
                DELETE
                FROM Review
                WHERE id = {id};
               """
        cursor = execute(sql)
        cursor.close()
        commit()
