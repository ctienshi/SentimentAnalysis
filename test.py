import urllib2, base64
import webbrowser
from pycorenlp import StanfordCoreNLP
import json, requests
from requests.auth import HTTPBasicAuth
data = "hello"
#a = requests.get('http://localhost:9000', auth=HTTPBasicAuth('ching', 'testing123'))
nlp = StanfordCoreNLP('http://localhost:9000')
res = nlp.annotate(data,properties={'annotators': 'sentiment','outputFormat':'json','timeout': 100000})

print (res)