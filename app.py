import flask
import tmdbsimple as tmdb
import urllib.request, json
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = flask.Flask(__name__, template_folder='templates')

df2 = pd.read_csv('./model/tmdb.csv')

tfidf = TfidfVectorizer(stop_words='english',analyzer='word')

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(df2['soup'])
print(tfidf_matrix.shape)

#construct cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print(cosine_sim.shape)

df2 = df2.reset_index()
indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()

# create array with all movie titles
all_titles = [df2['title'][i] for i in range(len(df2['title']))]

def get_recommendations(title):
    # Get the index of the movie that matches the title
    idx = indices[title]
    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]
    # print similarity scores
    print("\n Index      score")
    for i in sim_scores:
        print(i)

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # return ids of similar movies
    return  df2['id'].iloc[movie_indices]

# Set up the main route
@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))
            
    if flask.request.method == 'POST':
        m_name = flask.request.form['movie_name']
        m_name = m_name.title().strip()
        #  check = difflib.get_close_matches(m_name,all_titles,cutout=0.50,n=1)
        if m_name not in all_titles:
            return(flask.render_template('notFound.html',name=m_name))
        else:
            result_final = get_recommendations(m_name).to_numpy()
            movies =[]
            for i in range(len(result_final)):
                movies.append(tmdb.Movies(result_final[i]).info())
                
            return {"movies":movies}
            # return flask.render_template('found.html',movielist=movies,search_name=m_name)

@app.route("/movies")
def get_movies_list():
    movie = tmdb.Movies(1891)
    response = movie.info()
    return {"results": "https://image.tmdb.org/t/p/original"+movie.poster_path}
    # url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(os.environ.get("TMDB_API_KEY"))

    # response = urllib.request.urlopen(url)
    # movies = response.read()
    # dict = json.loads(movies)

    # movies = []

    # for movie in dict["results"]:
    #     movie = {
    #         "title": movie["title"],
    #         "overview": movie["overview"],
    #         # "director":movie["director"]
    #     }
        
    #     movies.append(movie)

    # return {"results": movies}

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
    #app.run()
