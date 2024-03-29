import json

FILE = open('config.json')
KEYS = json.load(FILE)

# back-end
CONSUMER_KEY = KEYS['CONSUMER_KEY']
CONSUMER_SECRET = KEYS['CONSUMER_SECRET']
ACCESS_TOKEN_1 = KEYS['ACCESS_TOKEN_1']
ACCESS_TOKEN_2 = KEYS['ACCESS_TOKEN_2']

# front-end
FLASK_SECRET = KEYS['FLASK_SECRET']
TWITCH_CLIENT_ID = KEYS['TWITCH_CLIENT_ID']
TWITCH_CLIENT_SECRET = KEYS['TWITCH_CLIENT_SECRET']
TWITCH_ACCESS_TOKEN = KEYS['TWITCH_ACCESS_TOKEN']

FILE.close()
