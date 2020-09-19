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
def get_WTI():
    collection_WTI = db['OIL_WTI'].find({})

    df_WTI = pd.DataFrame(list(collection_WTI))
    del df_WTI['_id']

    # df_WTI.info()
    df_WTI.set_index(['Date'],inplace=True)

    df_WTI.index = pd.to_datetime(df_WTI.index)
    df_WTI = df_WTI.resample('D').asfreq()

    df_WTI.fillna(method='ffill',inplace=True)

    df_WTI.sort_values(by=['Date'],ascending=False,inplace=True)

    # df_WTI.head()

    return df_WTI