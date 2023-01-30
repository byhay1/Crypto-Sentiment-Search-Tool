# B N Y Crypto Trend App Code
# This Python file uses the following encoding: utf-8

import apikey
from tkinter import *
import re, requests, csv
import json
from datetime import date

# -------------GUI---------------#

main_window = Tk()


# Text Input
search_subject = StringVar()
csv_name = StringVar()

# API KEY
keyapi = apikey.apikey


# -------------FUNCTIONS-------------#
def search_subject_call():
    global search_subject, csv_name
    global keyapi
    search_subject = search_subject.get()
    csv_name = csv_name.get()

    if re.search(" ", search_subject) or re.search(",", search_subject):
        q = re.sub("\s+", 'OR', search_subject)
        q = re.sub(',', 'OR', q)
        search_subject = q

    list_of_results = []
    page_number = 0
    url = 'https://api.social-searcher.com/v2/search'
    headers = {'Accept': 'application/json'}
    params = {'key': keyapi,
              'q': search_subject,
              'limit': 100,
              'page': page_number}

    counter = 0
    while counter < 1:
        try:
            results = requests.get(url, headers=headers, params=params).json()
            list_of_results += results['posts']
            page_number += 1
            params['page'] = page_number
            counter = page_number
            # for testing print results
            #print(results)
        except:
            break

    file = list_of_results

    if re.search(" ", search_subject) or re.search(",", search_subject):
        q = re.sub("\s+", 'OR', search_subject)
        q = re.sub(',', 'OR', q)
        search_subject = q
    to_csv = file
    keys = list(to_csv[0].keys())
    keys += {"urls"}
    keys += {"tags"}
    keys += {'popularity'}
    keys += {'title'}
    keys += {'image'}

    with open(f"{csv_name}_searched-on-{search_subject}_{date.today()}.csv", 'w', encoding="utf-8", newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(to_csv)


def the_looping():
    search_subject_call()
    main_window.after(86400000, the_looping)

# Labels
sub_lab = Label(main_window, text="Enter search subject(s):")
csv_lab = Label(main_window, text="What would you like to name csv:")

# Entrys
search_subject_entry = Entry(main_window, textvariable=search_subject, width=50, borderwidth=5)
csv_name_entry = Entry(main_window, textvariable=csv_name, width=50, borderwidth=5)

# Buttons
search_bttn = Button(main_window, text="Search and Create .csv", command=search_subject_call)
run_bttn = Button(main_window, text="Run Daily", command=the_looping)

# Grid
sub_lab.grid(row=0, column=0)
csv_lab.grid(row=1, column=0)
search_subject_entry.grid(row=0, column=1)
csv_name_entry.grid(row=1, column=1)
search_bttn.grid(row=2, column=1)
run_bttn.grid(row=2, column=2)


main_window.mainloop()


# -------------INTRO-------------#
# search_subject = input("enter search subject(s): ")
# csv_name = input("what would you like to name csv: ")
# csvpath_location = input("enter path location you want to save csv")
#
# keyapi = apikey.apikey
# page_number = 0
# auth = HTTPBasicAuth('apikey', '1234abcd')
# url = 'https://api.social-searcher.com/v2/search'
# headers = {'Accept': 'application/json'}
# params = {'key': keyapi,
#           'q': search_subject,
#           'limit': 100,
#           'page': page_number}


# -------------FUNCTIONS-------------#
# def search_subject_call():
#     global search_subject
#     global keyapi
#     if re.search(" ", search_subject) or re.search(",", search_subject):
#         q = re.sub("\s+", 'OR', search_subject)
#         q = re.sub(',', 'OR', q)
#         search_subject = q
#
#     list_of_results = []
#     page_number = 0
#     url = 'https://api.social-searcher.com/v2/search'
#     headers = {'Accept': 'application/json'}
#     params = {'key': keyapi,
#               'q': search_subject,
#               'limit': 20,
#               'page': page_number}
#
#     counter = 0
#     while counter < 10:
#         try:
#             results = requests.get(url, headers=headers, params=params).json()
#             list_of_results += results['posts']
#             page_number += 1
#             params['page'] = page_number
#             counter = page_number
#             # for testing print results
#             print(results)
#         except:
#             break
#
#     # printed_results = print(results.json())
#     return list_of_results
#
# def to_csv(file):
#     global search_subject
#     if re.search(" ", search_subject) or re.search(",", search_subject):
#         q = re.sub("\s+", 'OR', search_subject)
#         q = re.sub(',', 'OR', q)
#         search_subject = q
#     to_csv = file
#     keys = list(to_csv[0].keys())
#     keys += {"urls"}
#     keys += {"tags"}
#
#     with open(f"{csv_name}_searched-on-{search_subject}_{date.today()}.csv", 'w', encoding="utf-8", newline='') as output_file:
#         dict_writer = csv.DictWriter(output_file, keys)
#         dict_writer.writeheader()
#         dict_writer.writerows(to_csv)


# -------------INITIATE-------------#
# if __name__ == '__main__':
    ###
    # search_results = search_subject_call()
    # clean_response(file=search_results)
    # to_csv(file=search_results)
    # startapp(query)
