import pandas as pd 
import numpy as np 
df=pd.read_csv("articles.csv")
C=df["vote_average"].mean()
m=df["vote_count"].quantile(0.9)
q_movies=df.copy().loc[df["vote_count"]>=m]
def weighted_rating(x,m=m,C=C):
    v=x["vote_count"]
    R=x["vote_average"]
    return (v / (v + m)) *R + (m / (v + m)) *C  
q_movies["score"]=q_movies.apply(weighted_rating,axis=1)
q_movies=q_movies.sort_values("score",ascending=False)
output=q_movies[["timestamp","eventType","contentId","personId","sessionId","userAgent","userRegion","userCountry"]].head(10).values.tolist()
