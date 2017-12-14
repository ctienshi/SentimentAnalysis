from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from extractImportant import ListThreadsWithLabels
from extractImportant import get_mail_threads
from extractImportant import find_between

SCOPES = 'https://www.googleapis.com/auth/gmail.modify' # we are using modify and not readonly, as we will be marking the messages Read
store = file.Storage('storage.json')
creds = store.get()

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

user_id =  'me'

#Getting the threadID list for a particular label
threadids = []
r = ListThreadsWithLabels(GMAIL,'me','Label_64')
#print (len(r))
for i in range(len(r)):
    threadid = find_between(str(r[i]))
    threadids.append(threadid)
print (threadids)
print (len(threadids))

get_mail_threads(GMAIL,threadids)