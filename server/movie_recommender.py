# -*- coding: utf-8 -*-
"""Movie_Recommender.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HksYvh5s4GBT5DjLUTQpLKz7UYLzsS1i
"""

import pandas as pd
import numpy as np
import sys

df0=pd.read_csv("df0.csv")
df1=pd.read_csv("df1.csv")
df2=pd.read_csv("df2.csv")
df3=pd.read_csv("df3.csv")
df4=pd.read_csv("df4.csv")
df5=pd.read_csv("df5.csv")

def recommend_movies(value):
    # Define mini-datasets based on genres
    print("What do you want to see: Movie or TV series?")
    x = str(sys.argv[2])

    mini_datasets = {
        0: df0,
        1: df1,
        2: df2,
        3: df3,
        4: df4,
        5: df5
    }

    # Check if the provided value is valid
    if value not in mini_datasets:
        return "Invalid input. Please provide a value between 0 and 5."

    selected_df = mini_datasets[value]

    if x == "Movie":
        selected_df = selected_df[selected_df["contentType"] == "movie"]
        # Recommend the top 10 movies based on IMDb ratings for the corresponding mini-dataset
        top_movies = selected_df.nlargest(10, 'rating')[['title', 'rating', 'description', 'releaseYear']]
        return top_movies
    elif x == "TV series":
        selected_df = selected_df[selected_df["contentType"] == "tvSeries"]
        # Recommend the top 10 TV series based on IMDb ratings for the corresponding mini-dataset
        top_series = selected_df.nlargest(10, 'rating')[['title', 'rating', 'description', 'releaseYear']]
        return top_series
    else:
        return "Enter either 'Movie' or 'TV series' keyword!"