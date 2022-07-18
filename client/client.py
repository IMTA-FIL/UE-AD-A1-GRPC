import grpc

import movie_pb2
import movie_pb2_grpc

import showtime_pb2
import showtime_pb2_grpc

import booking_pb2
import booking_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:3001') as channel1:
        stub1 = movie_pb2_grpc.MovieStub(channel1)

        print("-------------- GetMovieByID --------------")
        movieid = movie_pb2.MovieID(id = "a8034f44-aee4-44cf-b32c-74cf452aaaae")
        get_movie_by_id(stub1, movieid)

        print("-------------- DeleteMovieByID --------------")
        del_movie_by_id(stub1, movieid)

        print("-------------- UpdateMovieByID --------------")
        moviedata = movie_pb2.MovieData(title="Victor Frankenstein", rating=7.8, director="Paul McGuigan", id = "7daf7208-be4d-4944-a3ae-c1c2f516f3e6")
        up_movie_by_id(stub1, moviedata)

        print("-------------- GetMovieByTitle --------------")
        movietitle = movie_pb2.MovieTitle(title = "The Danish Girl")
        get_movie_by_title(stub1, movietitle)

        print("-------------- GetListMovies --------------")
        get_list_movies(stub1)

    channel1.close()

if __name__ == '__main__':
    run()
