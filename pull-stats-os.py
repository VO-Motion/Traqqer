from opensea import OpenseaAPI
import pandas as pd
import time

# OPENSEA API

api = OpenseaAPI(apikey='prive-api-key')
collection_database = pd.DataFrame
collection_data = {}

def fetch_collection_data(collection_slug):
    return api.collection(collection_slug)

def fetch_collection_stats(collection_slug):
    response = fetch_collection_data(collection_slug)
    stats = response['collection']['stats']
    name = response['collection']['name']
    return name, stats

def poll():
    collection_list = open("/traqqer/back-end/collection_list.txt").read().splitlines()

    for x in collection_list:
        temp_data = fetch_collection_stats(x)
        collection_data[temp_data[0]] = temp_data[1]
        
    collection_database = pd.DataFrame(collection_data).transpose()
    print(collection_database) # print if needed
