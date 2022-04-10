from opensea import OpenseaAPI

# OPENSEA API

api = OpenseaAPI(apikey='{Private API Key}')

def fetch_raw_collection(collection_slug):
    return api.collection(collection_slug)

def fetch_collection(collection_slug):
    response = fetch_raw_collection(collection_slug)
    data = response['collection']['stats']
    print(data)

fetch_collection('pudgypenguins') # Example to pull statistics for Pudgy Penguins
