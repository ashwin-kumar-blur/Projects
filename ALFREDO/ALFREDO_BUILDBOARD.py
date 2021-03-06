from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/current/nlu")

message = "tell me the deaths for covid19 in India"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))




import requests

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

querystring = {"country":"Italy"}

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "d3e268aac3msh391d58982488c27p1f0052jsnff3a0fc6e47c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
import re
stat_dict = response.json()

if bool(re.match("Country not found.",message['message'])) == True:

    stat_dict = stat_dict['data']
    deaths = sum([i['deaths'] for i in stat_dict['covid19Stats']])
    recovered = sum([i['recovered'] for i in stat_dict['covid19Stats']])
    total_case = sum([i['confirmed'] for i in stat_dict['covid19Stats']])
    print("The death count world wide is {} and the count for recovered cases is {} while there are {} total number of "
      "reported cases. location unidentified try USA for usa or France for france".format(deaths,recovered,total_case))

else:

    stat_dict = stat_dict['data']
    deaths = sum([i['deaths'] for i in stat_dict['covid19Stats']])
    recovered = sum([i['recovered'] for i in stat_dict['covid19Stats']])
    total_case = sum([i['confirmed'] for i in stat_dict['covid19Stats']])
    print("The death count  for is {} and the count for recovered cases is {} while there are {} total number of "
      "reported cases.".format(deaths,recovered,total_case))
