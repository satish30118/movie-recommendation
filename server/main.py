import pandas as pd
import numpy as np
import tensorflow as tf
import text_normalizer as tn
import matplotlib.pyplot as plt
import seaborn as sns
import tokenizer_vectorizer as tkvc
import movie_recommender as mr
import posters as ps
import sys

import emotion_detector as ed


model=tf.keras.saving.load_model("text_based_emotion_classifier.h5")

text=str(sys.argv[1])
x=tn.normalize(text)
x=tkvc.tok_vectorizer(x)
a=model.predict(x)
mood=np.argmax(a[0],axis=0)
results=mr.recommend_movies(mood)
#print(results)

results1= results.reset_index(drop=True)
results1["title"][0]
posters=[]
for i in range(0,4):
    posters.append(ps.get_images(results1["title"][i]))
    print("Title:",results1['title'][i],)
    print("Rating:",results1['rating'][i])
    print("Release Year:",results1['releaseYear'][i])
    print("Description:",results1['description'][i])
    print("\n", "\n")

# audio section 
    
# mood1=ed.get_audio()

# if(mood1[0]==1):
#     mood1[0]=3
# if(mood1[0]==2):
#     mood1=4
# if(mood1[0]==3):
#     mood1[0]=1
# if(mood1[0]==4):
#     mood1[0]=0

# results11=mr.recommend_movies(mood1[0])
# results2=results11.reset_index(drop=True)

# posters=[]
# for i in range(0,4):
#     posters.append(ps.get_images(results2["title"][i]))
#     print("Title:",results2['title'][i])
#     print("Rating:",results2['rating'][i])
#     print("Release Year:",results2['releaseYear'][i])
#     print("Description:",results2['description'][i])