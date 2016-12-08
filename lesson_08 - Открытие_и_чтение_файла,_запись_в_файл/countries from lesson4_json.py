countries = {
	'Thailand': {'sea': True,
				'schengen': False,
				'average_temperature': 30,
				'currency_rate': 1.8,
				'cost_per_day': 60},
	'Hungary': {'sea': False,
				'schengen': True,
				'average_temperature': 10,
				'currency_rate': 0.3,
				'cost_per_day': 50},
	'Germany': {'sea': True,
				'schengen': True,
				'average_temperature': 10,
				'currency_rate': 80,
				'cost_per_day': 80},
	'Japan': {'sea': True,
				'schengen': False,
				'average_temperature': 15,
				'currency_rate': 0.61,
				'cost_per_day': 70},
	'Ukraine': {'sea': True,
				'schengen': False,
				'average_temperature': 23,
				'currency_rate': 4,
				'cost_per_day': 2000},
	'Russia': {'sea': True,
				'schengen': False,
				'average_temperature': 21,
				'currency_rate': 1,
				'cost_per_day': 5000},
	'Italy': {'sea': True,
				'schengen': True,
				'average_temperature': 25,
				'currency_rate': 60,
				'cost_per_day': 80},
	'Australia': {'sea': True,
				'schengen': False,
				'average_temperature': 23,
				'currency_rate': 90,
				'cost_per_day': 100},
	'USA': {'sea': True,
				'schengen': False,
				'average_temperature': 21,
				'currency_rate': 80,
				'cost_per_day': 90}
}

import json
from pprint import pprint

with open('countries_SM.json', 'w') as file:
	json.dump(countries, file)

with open('countries_SM.json') as file:
    country = json.load(file)
    pprint(country)

