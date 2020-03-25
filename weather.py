import requests
import config
import os

# prompt user for zip code they want to get weather information from
zip = input('Please enter the zip code: ') 
APIKEY = config.API_KEY

# link to send a request to the API
url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip},us&appid={APIKEY}' #url contains the zip code (US BASED) and developer API key
data = requests.get(url).json() # get the response from server --- convert in json file
print(data) # print the json object which contains the data

#extract from the json file to get the information and then print it out
print('City: {}'.format(data['name']))
print('Temperature: {}'.format(data['main']['temp']))
print('Country: {}'.format(data['sys']['country']))
print('Description: {}'.format(data['weather'][0]['description']))

