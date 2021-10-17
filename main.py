from flask import Flask,jsonify,request
from storage import all_movies,liked_movies,not_liked_movies,did_not_watch
from demographic_filtering import output
from content_filtering import get_recomendations
app=Flask(__name__)
@app.route("/get-movie")

def get_movie():

    })

@app.route("/liked-articles",methods=["POST"])
def liked_movie():
    article=all_[0]
    # all_movies=all_movies[1:]
    liked_movies.append(movie)
    all_movies.pop(0)
    return  jsonify({
        "status":"success"
    }),


@app.route("/unliked-movies",methods=["POST"])
def unliked_movie():
    movie=all_movies[0]
    # all_movies=all_movies[1:]
    not_liked_movies.append(movie)
    all_movies.pop(0)
    return  jsonify({
        "status":"success"
    }),


@app.route("/did-not-watch",methods=["POST"])
def did_not_watch_movie():

    movie=all_movies[0]
    # all_movies=all_movies[1:]
    did_not_watch.append(movie)
    all_movies.pop(0)
    return  jsonify({
        "status":"success"
    }),

@app.route("/popular-movies")

def popular_movies():
    movie_data=[]
    for movie in output:
        _d={
            "title":movie[0],
            "poster_link":movie[1],
            "release_date":movie[2],
            "duration":movie[3],
            "rating":movie[4],
            "overview":movie[5],
        }
        movie_data.append(_d)
    return jsonify({
        "data":movie_data,
        "status":"success"
    })

@app.route("/recomended-movies")

def recomended_movies():
    all_recomended=[]
    for liked_movie in liked_movies:
        output=get_recomendations(liked_movie[19])
        for data in output:
            all_recomended.append(data)
    import itertools
    all_recomended.sort()
    all_recomended=list(all_recomended for all_recomended,_ in itertools.groupby(all_recomended))

    movie_data=[]
    for recomended in output:
        _d={
            "title":recomended[0],
            "poster_link":recomended[1],
            "release_date":recomended[2],
            "duration":recomended[3],
            "rating":recomended[4],
            "overview":recomended[5],
        }
        movie_data.append(_d)
    return jsonify({
        "data":movie_data,
        "status":"success"
    })

if __name__=="__main__":
    app.run()