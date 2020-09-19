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
def get_XR():
    collection_XR = db['USD_KRW_XR'].find({})

    df_XR = pd.DataFrame(list(collection_XR))
    del df_XR['_id']

    # df_XR.info()
    # df_XR.head()

    drop_cols = ['오픈','고가','저가']
    df_XR.drop(drop_cols,axis=1,inplace=True)

    col_rename = ['Date','XR','Pct_Change']
    df_XR.columns = col_rename


    df_XR = df_XR.replace('년','-', regex=True)
    df_XR = df_XR.replace('월','-', regex=True)
    df_XR = df_XR.replace('일','', regex=True)
    df_XR = df_XR.replace('\,','', regex=True)
    df_XR = df_XR.replace('\%','', regex=True)
    df_XR = df_XR.replace(' ','', regex=True)

    # df_XR.head()

    df_XR['Date'] = pd.to_datetime(df_XR['Date'])
    df_XR = df_XR.set_index('Date')

    df_XR = df_XR.resample('D').asfreq()
    df_XR.fillna(method='ffill',inplace=True)

    df_XR.sort_values(by=['Date'],ascending=False,inplace=True)

    # df_XR.head()
    return df_XR