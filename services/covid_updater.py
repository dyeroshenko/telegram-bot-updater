import requests
from datetime import datetime, timedelta
import csv
import pandas
import numpy

from countries import countries

start_date = (datetime.now() - timedelta(days=2)).strftime('%m-%d-%Y')
end_date = (datetime.now() - timedelta(days=1)).strftime('%m-%d-%Y')

def extract_numbers_for_date(date): 

   URL = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv'
   
   dataframe = pandas.read_csv(URL)
   sum_of_cases_by_country = dataframe.groupby("Country_Region")["Confirmed"].sum()
   cases = []
 
   for country in countries.keys():
      cases.append(sum_of_cases_by_country[country])

   return cases


def calculate_cases_previous_date():
   cases_two_days_ago = extract_numbers_for_date(start_date)
   cases_one_day_ago = extract_numbers_for_date(end_date)

   result = numpy.subtract(cases_one_day_ago, cases_two_days_ago)
   return result


def construct_message():
   date = (datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y')

   result = calculate_cases_previous_date()
   emojies = [emoji for emoji in countries.values()]
   storage = dict(zip(emojies, result))

   strings = []

   for flag, numbers in storage.items():
      message = f'{flag} *{numbers}*\n'
      strings.append(message)
   message = ('').join(strings)
   
   base_message = f'Covid stats for {date}:\n{message}'
   return base_message