import re
import pandas as pd
import requests
# from bs4 import BeautifulSoup

import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://jihwan:1234@intelportfolio.kqupw.gcp.mongodb.net/test?retryWrites=true&w=majority')
db = cluster['test']

## BACKEND and ML

# DJI
def get_DJI():
    collection_DJI = db['DJI'].find({})

    df_DJI = pd.DataFrame(list(collection_DJI))
    del df_DJI['_id']

    df_DJI.info()
    df_DJI.set_index(['Date'],inplace=True)
    df_DJI.sort_values(by=['Date'],ascending=False,inplace=True)
    drop_cols = ['Open', 'High','Low', 'Adj Close', 'Volume']

    # Remove columns without relative significance.
    df_DJI = df_DJI.drop(drop_cols,axis=1)
    df_DJI.head()


    df_DJI.index = pd.to_datetime(df_DJI.index)

    df_DJI = df_DJI.resample('D').asfreq()
    df_DJI.sort_values(by=['Date'],ascending=False,inplace=True)
    df_DJI.fillna(method='ffill',inplace=True)
    return df_DJI