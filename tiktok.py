# Importing the python SDK
from TikTokApi import TikTokApi as tiktok
# Import json for the export of data
import json
# Import data processing helper
from helpers import process_results
# import pandas to create dataframe
import pandas as pd
# Import sys dependency to extract command line arguments
import sys


def get_data(hashtag):
    # Get Cookie data - INCOMPLETE
    verifyFP = "verify_kx5hcndm_Y1XGuNJz_Cw74_4lWy_B8Oe_AWRuZJ1WS73J"
    # Setup an instance
    api = tiktok.get_instance(custom_verifyFP = verifyFP, use_test_endpoints=True)

    # Get data by hashtags
    trending = api.by_hashtag(hashtag)

    flattened_data = process_results(trending)

    # Export data to json
    #with open('export.json', 'w') as f:
    #   json.dump(flattened_data, f)


    # Convert the preprocessed data to dataframe
    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    df.to_csv('tiktokdata.csv')

if __name__=='__main__':
    get_data(sys.argv[1])
