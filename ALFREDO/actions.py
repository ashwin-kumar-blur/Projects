
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals


from rasa_core_sdk import Action
from rasa_core_sdk import events


class Inform_Action(Action):
	def name(self):
		return 'action_inform'

	def run(self, dispatcher, tracker, domain):
		import requests

		url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
		loc = tracker.get_slot('location')

		querystring = {"country":loc}

		headers = {
    	'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    	'x-rapidapi-key': "d3e268aac3msh391d58982488c27p1f0052jsnff3a0fc6e47c"
    		}

		response = requests.request("GET", url, headers=headers, params=querystring)
		stat_dict = response.json()
		stat_dict = stat_dict['data']
		deaths = sum([i['deaths'] for i in stat_dict['covid19Stats']])
		recovered = sum([i['recovered'] for i in stat_dict['covid19Stats']])
		total_case = sum([i['confirmed'] for i in stat_dict['covid19Stats']])
		Details = ("The death count is {} and the count for recovered cases is {} while there are {} total number of "
		      		"reported cases".format(deaths,recovered,total_case))
		dispatcher.utter_message(Details)
		return(events.Slotset('location',loc))