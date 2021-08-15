# Movie-recommendation-system

This Content Based Filtering Movie Recommender is built on a flask app using Python programming language and JavaScript programming language. Two snippets of code were created using the concept of CB. The first one is in Python programming language using the package “scikit-learn” and the second snippet of code is in JavaScript programming language which uses no packages and operates based on logic. Here, feature extraction methods and distamce metrics are utilised to generate recommendations. 

Dataset: TMDB 5000


## Content Based Filtering Methods

Feature extraction methods such as TF-IDF vectorises the text data and distance metrics such as Cosine Similarity computes the similarity between each item by calculating the distance between each vector.

### Feature Extraction Method
The feature extraction method used in this recommender is Term Frequency- Inverse Document Frequency (TF-IDF). TF-IDF works by converting textual information into a Vector Space Model (VSM). In the context of TF-IDF, VSM is an algebraic model that represents text documents as vectors, also known as index terms. The converted vectors can be seen as features extracted from the document. With CB filtering, a multi-dimension vector represents the preference of a user and the items available, in which each item is stored as a vector of its features. The angles between these vectors will be useful later on in calculating the similarity between each item.   
![image](https://user-images.githubusercontent.com/65379600/129465678-66d0773d-6faf-4759-8235-bf7d2e96aefa.png) ![image](https://user-images.githubusercontent.com/65379600/129465752-2119f556-8edf-428f-8b85-3972121e413d.png)
### Distance metric
The distance metric used in this recommender is Cosine Similarity. Cosine Similarity computes the similarity of items by measuring the cosine of the angle between two vectors projected in a multidimensional vector space. With Cosine Similarity, non-binary vector values are taken into consideration during calculation as the values directly influence the position of the vector. Cosine Similarity focuses on the contents of the items and disregards the size of the items. Hence, Cosine Similarity is suitable for text documents with different word counts. 
![image](https://user-images.githubusercontent.com/65379600/129465404-790cbc28-ee78-4c2f-85c8-e40f82ac72d6.png)   
![image](https://user-images.githubusercontent.com/65379600/129465856-d995cf37-72d5-4036-9197-c8abd592f43a.png)  


## Code Snippets

Two of the following snippets of code were developped to demonstrate the use of TFIDF and Cosine SImilarity in generating recommendations.

### Python Code
The python code in app.py will generate a list of movie recommendations provided that the user entered a valid movie name. In this set of code, the TF-IDF Vectorizer and Cosine Similarity function is imported from the “scikit-learn” package.

Documentation: [TF-IDF vectoriser](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html?highlight=tfidf#sklearn.feature_extraction.text.TfidfVectorizer) and [Cosine Similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#sklearn.metrics.pairwise.cosine_similarity)

### Javascript Code
The javascript code in notfound.html is executed when the user entered an invalid movie name. This set of code will return movie titles that are similar to the input that the user has entered, if applicable. Since this set of code doesn't use any packages, a dictionary was created to store the terms in the text and several functions were created to compute the TF-IDF and Cosine Similarity values.


## Setup
activate environment and install requirements (windows):
```
python -m venv venv
.\venv\scripts\activate
python -m pip install -r requirements.txt 
```

run flask app:
```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```


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
TFIDF and Cosine Similarity functions from the scikit-learn package was used to generate movie recommendations.
