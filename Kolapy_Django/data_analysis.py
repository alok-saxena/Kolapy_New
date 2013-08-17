import pandas as pd
import numpy as np

from pymongo import MongoClient
client = MongoClient()
db = client.kolapy
import datetime as dt
import StringIO
import re


# get pandas dataframe from ticker
def dataframe(ticker):
    global db
    collection = db.daily
    cursor = collection.find({'Symbol': ticker})
    if not cursor.count():
        return None
    df = pd.DataFrame(list(cursor))
    df.index = pd.to_datetime(df['Date'])
    return df

# get full name of company from ticker
def name(ticker):
    global db
    collection = db.tickers
    return str(collection.find_one({'Symbol': ticker})['Name'])

# get typeahead options from term
def getSymbolData(symbol):
    global db
    collection = db.tickers
    data = list(collection.find({'Symbol': symbol}, {'_id': False}))
    return data

def csv(series):
    output = StringIO.StringIO()
    series.to_csv(output, sep=',');
    val = output.getvalue()
    output.close()
    return val