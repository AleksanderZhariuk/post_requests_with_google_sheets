import requests
import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
TOKEN = os.environ.get('TOKEN')
URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_URL = os.environ.get('SHEETY_URL')

user_text = input('What are u doing today? ')
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}
config = {
    'query': user_text
}
response = requests.post(url=URL, headers=headers, json=config).json()

new_row_auth = {
    "Authorization": f"Bearer {TOKEN}"
}

for user_input in response['exercises']:
    new_row_config = {
        'workout': {
            'date': datetime.datetime.now().strftime('%d/%m/%Y'),
            'time': datetime.datetime.now().strftime('%H:%M:%S'),
            'exercise': user_input['user_input'].title(),
            'duration': user_input['duration_min'],
            'calories': user_input['nf_calories']
        }
    }
    new_row = requests.post(url=SHEETY_URL, headers=new_row_auth, json=new_row_config)
