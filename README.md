# Movie-recommendation-system

A Content Based Filtering Movie Recommendation Flask app that uses Tf-Idf and Cosine Similarity.

Dataset: TMDB 5000

## Setup
activate environment and install requirements (windows):
``python
python -m venv venv <br/>
.\venv\scripts\activate <br/>
python -m pip install -r requirements.txt <br/>
``

run flask app:
``python
set FLASK_APP=app.py<br/>
set FLASK_ENV=development<br/>
flask run<br/>
``

## Files
### index.html
Home page where user can input a movie name to search for similar movie recommendations

### found.html
Page to display all movie recommendations similar to the input.

### notfound.html
Error page that shows when the initial movie input is not a valid movie in the dataset.
TFIDF and Cosine Similarity functions and algorithms were developed to suggest a valid input

### app.py
Python Flask app, processes all the routing and app logic when user has entered a valid movie input.
TFIDF and Cosine Similarity functions from the sklearn package was used to generate movie recommendations.
