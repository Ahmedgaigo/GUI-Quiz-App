import requests

api = 'https://opentdb.com/api.php?amount=50&type=boolean'

response = requests.get(api)
question_data = response.json()['results']

