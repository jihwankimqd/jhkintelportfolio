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
def get_IR():
    # collection_KR_IR = db['KR_IR'].find({})

    # df_IR = pd.DataFrame(list(collection_KR_IR))
    # del df_IR['_id']
    
    # Didn't really need a database for KR_IR. But made one in the inital stage anyways.
    dates = pd.Index([pd.Timestamp('2015-03-12'), 
                    pd.Timestamp('2015-06-11'), 
                    pd.Timestamp('2016-06-09'), 
                    pd.Timestamp('2017-11-30'), 
                    pd.Timestamp('2018-11-30'), 
                    pd.Timestamp('2019-07-18'), 
                    pd.Timestamp('2019-10-16'), 
                    pd.Timestamp('2020-03-17'), 
                    pd.Timestamp('2020-05-28'), 
                    pd.Timestamp('2020-08-19')])
    df_IR = pd.DataFrame([1.75,1.50,1.25,1.50,1.75,1.50,1.25,0.75,0.50,0.50], dates)
    df_IR = df_IR.asfreq('D')
    df_IR.fillna(method='ffill',inplace=True)
    df_IR.reset_index(inplace=True)
    df_IR.columns = ['Date','IR']
    df_IR['Date'] = pd.to_datetime(df_IR['Date'])
    df_IR.sort_values(by=['Date'],ascending=False,inplace=True)
    df_IR.set_index(['Date'],inplace=True)
    # df_IR.head()
    return df_IR