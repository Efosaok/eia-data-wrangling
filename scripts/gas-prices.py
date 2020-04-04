import requests
import os
import pandas as pd

api_key = os.getenv('API_KEY')
daily_price_url = 'http://api.eia.gov/series/?api_key=' + api_key + '&series_id=NG.RNGWHHD.D'
monthly_price_url = 'http://api.eia.gov/series/?api_key=' + api_key + '&series_id=NG.RNGWHHD.M'

try:
  print('fetching data ...')
  daily_price_response = requests.get(daily_price_url)
  monthly_price_response = requests.get(monthly_price_url)

  daily_price_data = daily_price_response.json()['series'][0]['data']
  monthly_price_data = monthly_price_response.json()['series'][0]['data']

  print('processing data...')
  daily_prices = pd.DataFrame(
    {
      'Date': [i[0][0 : 4] + '-' + i[0][4 : 6] + '-' + i[0][6 : 8] for i in daily_price_data],
      'Price (Dollars per Million Btu)': [i[1] for i in daily_price_data],
    }
  )

  monthly_prices = pd.DataFrame(
    {
      'Date': [i[0][0 : 4] + '-' + i[0][4 : 6] + '-' + '01' for i in monthly_price_data],
      'Price (Dollars per Million Btu)': [i[1] for i in monthly_price_data],
    }
  )

  daily_prices.to_csv('data/henry_hub_natural_gas_prices_daily.csv')
  monthly_prices.to_csv('data/henry_hub_natural_gas_prices_monthly.csv')
except:
  print('An error occurred, please try again')
else:
  print('csv files successfully updated with new data')
