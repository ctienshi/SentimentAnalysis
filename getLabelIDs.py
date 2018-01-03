from apiclient import discovery
from apiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
import base64
from bs4 import BeautifulSoup
import re
import time
import dateutil.parser as parser
from datetime import datetime
import datetime
import csv
from Sentiment import calEmotionalLevel

results = GMAIL.users().labels().list(userId='me').execute()
labels = results.get('labels', [])

if not labels:
    print('No labels found.')
else:
    print('Labels:')
    for label in labels:
        print(label['name']+ " "+label['id'])