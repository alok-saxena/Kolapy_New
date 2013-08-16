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
    df = pd.DataFrame(list(collection.find({'Symbol' : ticker})))
    df.index = pd.to_datetime(df['Date'])
    return df

# get full name of company from ticker
def name(ticker):
    global db
    collection = db.tickernames
    return str(collection.find_one({'Symbol' : ticker})['Name'])

# get typeahead options from term
def typeahead(term):
    global db
    collection = db.tickernames
    regx = '^' + term + '.*'
    regx = re.compile(regx, re.IGNORECASE)
    data = list(collection.find({'Symbol': regx}, {'_id': False}))
    return data

def csv(series, json):
    if json:
        output = StringIO.StringIO()
        series.to_csv(output, sep=',');
        val = output.getvalue()
        output.close()
        return val
    var_list = []
    for i in xrange(len(series)):
        var_list.append(series.index[i].strftime('%Y-%m-%d') + ',' + str(series[i]) + '\\n')
    return 'Date,Price' + '\\n' + ''.join(var_list)