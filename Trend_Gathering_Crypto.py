# BNY Crypto Trend App Code
import apikey
import re
import requests

# -------------INTRO-------------#
search_subject = input("enter search subject(s)")

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


# -------------INITIATE-------------#
if __name__ == '__main__':
    search_subject_call()
    # infile(file)
    # startapp(query)
