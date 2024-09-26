# -*- coding: utf-8 -*-
"""04. Recommendation Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d0_BQXdMUHpgnPxXUuZ5IXarqmBpfbyP
"""

import numpy as np
import pandas as pd
import ast
import re

movies = pd.read_csv('25k IMDb movie Dataset.csv')

movies.shape

movies.head(1)

movies.head(1)['Generes'].values

movies.head(1)['Plot Kyeword'].values

movies.head(1)['Overview'].values

movies.info()

movies.isnull().sum()

# drop missing data column
movies.fillna('', inplace=True)

movies.isnull().sum()

movies.duplicated().sum()

movies.iloc[0].Generes

movies['Generes'] = movies['Generes'].apply(lambda x: ast.literal_eval(x))
movies.iloc[0].Generes

movies.iloc[0].Overview

movies['Overview'] = movies['Overview'].str.split()
movies.iloc[0].Overview

movies.iloc[0]['Plot Kyeword']

movies['Plot Kyeword'] = movies['Plot Kyeword'].apply(lambda x: ast.literal_eval(x))

movies.iloc[0]['Plot Kyeword']

movies.iloc[0]['Top 5 Casts']

movies['Top 5 Casts'] = movies['Top 5 Casts'].apply(lambda x: ast.literal_eval(x))
movies.iloc[0]['Top 5 Casts']

movies.iloc[0]['Director']

movies['Director'] = movies['Director'].apply(lambda x: [x])
movies.iloc[0]['Director']

movies.iloc[0]['Writer']

movies['Writer'] = movies['Writer'].apply(lambda x: [x])
movies.iloc[0]['Writer']

movies.iloc[0]['year']

# define a regular expression pattern to extract the year from the "year" column
year_pattern = r'\d{4}'

# define a function to extract the year from a value in the "year" column
def extract_year(year_value):
    year_match = re.search(year_pattern, str(year_value))
    if year_match:
        return [year_match.group()]
    else:
        return []

# apply the "extract_year" function to the "year" column and create a new column "Year_List"
movies['year'] = movies['year'].apply(extract_year)


movies.iloc[0]['year']

movies.iloc[1000]['year']



# define a regular expression pattern to extract the numbers from the "User Rating" column
num_pattern = r'\d+\.?\d*'

# define a function to extract the number from a value in the "User Rating" column
def extract_number(rating_value):
    num_match = re.search(num_pattern, str(rating_value))
    if num_match:
        return float(num_match.group().replace(',', '')) * 1000 if 'K' in rating_value else int(float(num_match.group().replace(',', '')) * 1000000) if 'M' in rating_value else int(num_match.group())
    else:
        return None

# apply the "extract_number" function to the "User Rating" column and create a new column "User_Rating_Int"
movies['User Rating'] = movies['User Rating'].apply(extract_number)

movies.iloc[0]['User Rating']

# create a new column "User_Rating_Quantile" containing the quantile values for each row
movies['User Rating'] = pd.qcut(movies['User Rating'], 100, labels=False, duplicates='drop')

# print the minimum and maximum quantile values
print('Minimum quantile value:', movies['User Rating'].min())
print('Maximum quantile value:', movies['User Rating'].max())

movies.iloc[0]['User Rating']

movies['User Rating']

movies['User Rating'] = [f"[{int(x)} quantile value]" for x in movies['User Rating']]

movies.iloc[0]['User Rating']

movies.head()

# replace 'no-rating' values with NaN
movies['Rating'].replace('no-rating', np.nan, inplace=True)

# convert 'Rating' column to float type
movies['Rating'] = movies['Rating'].astype(float)

# calculate the mean value of 'Rating' column and replace NaN with the mean value
mean_rating = movies['Rating'].mean()
movies['Rating'].fillna(mean_rating, inplace=True)

movies['Rating']

bin_edges = np.linspace(0, 10, 31)
bin_labels = [f"{bin_edges[i]:.4f}-{bin_edges[i+1]:.4f}" for i in range(30)]

# Create a new column with the bin labels for each movie rating
movies['Rating_bin'] = pd.cut(movies['Rating'], bins=bin_edges, labels=bin_labels)

# Format the bin labels to display up to 4 decimal places
movies['Rating_bin'] = movies['Rating_bin'].apply(lambda x: x.replace('(', '').replace(']', '').replace(',', '-'))

# print the first 10 movies with their rating and rating bin
movies[['movie title', 'Rating', 'Rating_bin']].head(10)

movies['Rating_bin'].nunique()

movies = movies.drop(['Run Time', 'Rating'], axis=1)

movies.head(1)

movies.head()

# define lambda function to convert string to list and extract first element
def convert_to_str(s):
    str = None
    if isinstance(s, list):
        str =  re.findall('\d+', s[0])[0]
    else:
        str = s.strip().split()[0]

    str = str[1:] + ' quantile value'
    return [str]

# apply lambda function to each value in 'User Rating' column
movies['User Rating'] = movies['User Rating'].apply(convert_to_str)

movies.head()

movies['Rating_bin'] = movies['Rating_bin'].astype(str).apply(lambda x: x.split("-"))

# define a function to join the words in each list and remove spaces
def clean(genres_list):
    return [genre.replace(' ', '') for genre in genres_list]

# apply the clean_genres function to the Generes column
movies['Generes'] = movies['Generes'].apply(clean)
movies['Plot Kyeword'] = movies['Plot Kyeword'].apply(clean)
movies['Director'] = movies['Director'].apply(clean)
movies['Top 5 Casts'] = movies['Top 5 Casts'].apply(clean)
movies['Writer'] = movies['Writer'].apply(clean)
movies['User Rating'] = movies['User Rating'].apply(clean)
movies['Rating_bin'] = movies['Rating_bin'].apply(clean)

movies.head(1)

# create new column names tags and concatinate these column
movies['tags'] = movies['User Rating'] + movies['Generes'] + movies['Overview'] + movies['Plot Kyeword'] + movies['Director'] + movies['Top 5 Casts'] + movies['Writer'] + movies['year'] + movies['Rating_bin']

movies['tags'] = movies['tags'].apply(lambda x: ' '.join(x))

movies['tags'] = movies['tags'].apply(lambda x: x.lower())

movies.head(1)

new_df = movies[['path','movie title','tags']]
new_df.head()

new_df['tags'][0]

new_df['tags'][1]

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))

    return ' '.join(y)

new_df['tags'] = new_df['tags'].apply(stem)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 5000, stop_words='english')

vectors = cv.fit_transform(new_df['tags']).toarray()

vectors[0]

features = cv.get_feature_names_out()

len(features)

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)

similarity.shape

def recommend(movie):
    movie_index = new_df[new_df['movie title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    return movies_list

movie_names = ['Batman Begins','Top Gun: Maverick','Iron Man',"The King's Man"]
for name in movie_names:
    recommend(name)
    print(f'================{name}====================')
    for i in movie_list:
        print(new_df.iloc[i[0]]['movie title'])

import pickle

pickle.dump(new_df,open('movies.pkl','wb'))

new_df.to_dict()

pickle.dump(new_df.to_dict(),open('movies_dict.pkl','wb'))

pickle.dump(similarity,open('similarity.pkl','wb'))
























