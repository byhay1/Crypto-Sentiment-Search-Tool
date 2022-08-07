# B N Y Crypto Trend App Code
import apikey
import re
import requests
import pandas as pd
from datetime import date

# -------------INTRO-------------#
search_subject = input("enter search subject(s)")
csvpath_location = input("enter path location you want to save csv")

keyapi = apikey.apikey
# auth = HTTPBasicAuth('apikey', '1234abcd')
url = 'https://api.social-searcher.com/v2/search'
headers = {'Accept': 'application/json'}
params = {'key': keyapi,
          'q': search_subject}


# -------------FUNCTIONS-------------#
def search_subject_call():
    global search_subject
    if re.search(" ", search_subject) or re.search(",", search_subject):
        q = re.sub("\s+", 'OR', search_subject)
        q = re.sub(',', 'OR', q)
        search_subject = q

    results = requests.get(url, headers=headers, params=params)
    printed_results = print(results.json())
    return printed_results

def to_csv(file):
    csvpath_file = f"{csvpath_location}\\{search_subject}_cryptonews_{date.today()}.csv"
    df = pd.read_json(file)
    df.to_csv(csvpath_file, index=None)

# -------------INITIATE-------------#
if __name__ == '__main__':
    search_results = search_subject_call()
    # clean_response(file=search_results)
    to_csv(file=search_results)
    # startapp(query)
