# Movie-recommendation-system

## About  
This Content Based Filtering Movie Recommender is built on a [flask app](https://flask.palletsprojects.com/en/2.0.x/) using Python programming language and JavaScript programming language. Two snippets of code were created using the concept of CB. The first one is in Python programming language using the package “scikit-learn” and the second snippet of code is in JavaScript programming language which uses no packages and operates based on logic. Here, feature extraction methods and distance metrics are utilised to generate recommendations. 

Dataset: TMDB 5000

## Content Based Filtering Methods

Feature extraction methods such as TF-IDF vectorises the text data and distance metrics such as Cosine Similarity computes the similarity between each item by calculating the distance between each vector.

### Feature Extraction Method
The feature extraction method used in this recommender is Term Frequency- Inverse Document Frequency (TF-IDF). TF-IDF works by converting textual information into a Vector Space Model (VSM). In the context of TF-IDF, VSM is an algebraic model that represents text documents as vectors, also known as index terms. The converted vectors can be seen as features extracted from the document. With CB filtering, a multi-dimension vector represents the preference of a user and the items available, in which each item is stored as a vector of its features. The angles between these vectors will be useful later on in calculating the similarity between each item.   
![image](https://user-images.githubusercontent.com/65379600/129465678-66d0773d-6faf-4759-8235-bf7d2e96aefa.png) ![image](https://user-images.githubusercontent.com/65379600/129465918-24743bfe-cc19-44aa-80bc-d8f85a75e6a2.png)  
### Distance metric
The distance metric used in this recommender is Cosine Similarity. Cosine Similarity computes the similarity of items by measuring the cosine of the angle between two vectors projected in a multidimensional vector space. With Cosine Similarity, non-binary vector values are taken into consideration during calculation as the values directly influence the position of the vector. Cosine Similarity focuses on the contents of the items and disregards the size of the items. Hence, Cosine Similarity is suitable for text documents with different word counts. 
![image](https://user-images.githubusercontent.com/65379600/129465404-790cbc28-ee78-4c2f-85c8-e40f82ac72d6.png)   ![image](https://user-images.githubusercontent.com/65379600/129466224-5b165535-f7be-4378-a8bb-0438d4e60574.png)


## Code Snippets

Two of the following snippets of code were written to demonstrate the use of TFIDF and Cosine SImilarity in generating recommendations.

### Python Code
The python code in app.py will generate a list of movie recommendations provided that the user entered a valid movie name. When the entered movie name matches with a movie name in the dataset, recommendations will be generated according to the soup column (all details concatenated into one string) of each movie. In this set of code, the TF-IDF Vectorizer and Cosine Similarity function is imported from the “scikit-learn” package.

scikit-learn documentation: [TF-IDF vectoriser](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html?highlight=tfidf#sklearn.feature_extraction.text.TfidfVectorizer) and [Cosine Similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#sklearn.metrics.pairwise.cosine_similarity)

### Javascript Code
The javascript code in notfound.html is executed when the user entered an invalid movie name. This set of code will return movie titles that are similar to the input that the user has entered, if applicable. The entered data will be checked against all existing movie names to find the most similar movie names. Since this snippet of code doesn't use any packages, a dictionary was created to store the terms for vectorising purposes and several functions were also created to compute the TF-IDF and Cosine Similarity values.


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

