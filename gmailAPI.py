'''
Before running this script, the user should get the authentication by following 
the link: https://developers.google.com/gmail/api/quickstart/python
Also, client_secret.json should be saved in the same directory as this file
'''

# Importing required libraries
from apiclient import discovery
<<<<<<< HEAD
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


# Creating a storage.JSON file with authentication details
SCOPES = 'https://www.googleapis.com/auth/gmail.modify' # we are using modify and not readonly, as we will be marking the messages Read
store = file.Storage('storage.json') 
creds = store.get()
=======
from httplib2 import Http
from oauth2client import file, client, tools
from bs4 import BeautifulSoup
from Sentiment import calEmotionalLevel
import dateutil.parser as parser
import base64

# Creating a storage.JSON file with authentication details
SCOPES = 'https://www.googleapis.com/auth/gmail.modify' # we are using modify and not readonly, as we will be marking the messages Read
store = file.Storage('storage.json')
creds = store.get()

>>>>>>> version5
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

user_id =  'me'
label_id_one = 'INBOX'
label_id_two = 'UNREAD'

# Getting all the unread messages from Inbox
<<<<<<< HEAD
# labelIds can be changed accordingly

#unread_msgs = GMAIL.users().messages().list(userId='me',labelIds=[label_id_one, label_id_two]).execute()
vpos = GMAIL.users().messages().list(userId='me',labelIds='Label_64').execute()
#print (vpos)
# We get a dictonary. Now reading values for the key 'messages'
mssg_list = vpos['messages']

print ("Total unread messages in inbox: ", str(len(mssg_list)))

=======

# We get a dictonary. Now reading values for the key 'messages'
vpos = GMAIL.users().messages().list(userId='me',labelIds='Label_63').execute()
mssg_list = vpos['messages']

>>>>>>> version5
final_list = [ ]
count = 0
email = ''
elevel = 0

lbl = ""

for mssg in mssg_list:
<<<<<<< HEAD
	temp_dict = { }
	m_id = mssg['id'] # get id of individual message
	message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute() # fetch the message using API
	payld = message['payload'] # get payload of the message 
	headr = payld['headers'] # get header of the payload


	for one in headr: # getting the Subject
		if one['name'] == 'Subject':
			msg_subject = one['value']
			temp_dict['Subject'] = msg_subject
		else:
			pass


	for two in headr: # getting the date
		if two['name'] == 'Date':
			msg_date = two['value']
			date_parse = (parser.parse(msg_date))
			m_date = (date_parse.date())
			temp_dict['Date'] = str(m_date)
		else:
			pass

	for three in headr: # getting the Sender
		if three['name'] == 'From':
			msg_from = three['value']
			temp_dict['Sender'] = msg_from
		else:
			pass

	temp_dict['Snippet'] = message['snippet'] # fetching message snippet
	
	try:
		
		# Fetching message body
		mssg_parts = payld['parts'] # fetching the message parts
		part_one  = mssg_parts[0] # fetching first element of the part 
		part_body = part_one['body'] # fetching body of the message
		part_data = part_body['data'] # fetching data from the body
		clean_one = part_data.replace("-","+") # decoding from Base64 to UTF-8
		clean_one = clean_one.replace("_","/") # decoding from Base64 to UTF-8
		clean_two = base64.b64decode (bytes(clean_one, 'UTF-8')) # decoding from Base64 to UTF-8
		soup = BeautifulSoup(clean_two , "lxml" )
		mssg_body = soup.body()
		temp_dict['Message_body'] = mssg_body
		
	except :
		pass

	final_list.append(temp_dict)
	# This will create a dictonary item in the final list
	# This will mark the messagea as read
	email = str(final_list[count])
	elevel = calEmotionalLevel(email)

	if elevel == 2:
		lbl = 'Label_77' #very positive
	elif elevel == 1:
		lbl = 'Label_76' #positive
	elif elevel == 0:
		lbl = 'Label_75' #neutral

	elif elevel == -1: #negative
		lbl = 'Label_74'
	elif elevel == -2: #very negative
		lbl = 'Label_73'
	print(email)
	print(elevel)
	
	# Updating the label according to the emotional level
	GMAIL.users().messages().modify(userId=user_id, id=m_id,body={ 'addLabelIds': ['UNREAD', lbl]}).execute() 

	count = count + 1
	if count == 100:
		break

print ("Total messaged retrived: ", str(len(final_list)))

=======
    temp_dict = { }
    m_id = mssg['id'] # get id of individual message
    message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute() # fetch the message using API
    payld = message['payload'] # get payload of the message
    headr = payld['headers'] # get header of the payload


    for one in headr: # getting the Subject
        if one['name'] == 'Subject':
            msg_subject = one['value']
            temp_dict['Subject'] = msg_subject
        else:
            pass


    for two in headr: # getting the date
        if two['name'] == 'Date':
            msg_date = two['value']
            date_parse = (parser.parse(msg_date))
            m_date = (date_parse.date())
            temp_dict['Date'] = str(m_date)
        else:
            pass

    for three in headr: # getting the Sender
        if three['name'] == 'From':
            msg_from = three['value']
            temp_dict['Sender'] = msg_from
        else:
            pass

    temp_dict['Snippet'] = message['snippet'] # fetching message snippet

    try:

        # Fetching message body
        mssg_parts = payld['parts'] # fetching the message parts
        part_one  = mssg_parts[0] # fetching first element of the part
        part_body = part_one['body'] # fetching body of the message
        part_data = part_body['data'] # fetching data from the body
        clean_one = part_data.replace("-","+") # decoding from Base64 to UTF-8
        clean_one = clean_one.replace("_","/") # decoding from Base64 to UTF-8
        clean_two = base64.b64decode (bytes(clean_one, 'UTF-8')) # decoding from Base64 to UTF-8
        soup = BeautifulSoup(clean_two , "lxml" )
        mssg_body = soup.body()
        temp_dict['Message_body'] = mssg_body

    except :
        pass

    final_list.append(temp_dict)
    # This will create a dictonary item in the final list
    # This will mark the messagea as read
    email = str(final_list[count])
    elevel = calEmotionalLevel(email)

    if elevel == 2:
        lbl = 'Label_77' #very positive
    elif elevel == 1:
        lbl = 'Label_76' #positive
    elif elevel == 0:
        lbl = 'Label_75' #neutral

    elif elevel == -1: #negative
        lbl = 'Label_74'
    elif elevel == -2: #very negative
        lbl = 'Label_73'

    # Updating the label according to the emotional level
    GMAIL.users().messages().modify(userId=user_id, id=m_id,body={ 'addLabelIds': ['UNREAD', lbl]}).execute()

    count = count + 1
    if count == 100:
        break

print ("Total messaged retrived: ", str(len(final_list)))

#The code to get the relevant label IDs
>>>>>>> version5
'''
results = GMAIL.users().labels().list(userId='me').execute()
labels = results.get('labels', [])

if not labels:
    print('No labels found.')
else:
  print('Labels:')
  for label in labels:
    print(label['name']+ " "+label['id'])
<<<<<<< HEAD

=======
'''
'''
>>>>>>> version5
#Negative Label_74
#VeryPositive Label_77
#Neutral Label_75
#Positive Label_76
#VeryNegative Label_73
Labels:
Mars-dev Label_48
Dev Label_41
Sales/Marktn/Bizdev/LatAm-Bizdev Label_28
CATEGORY_PERSONAL CATEGORY_PERSONAL
6. operations Label_57
2. vacation Label_65
Documentation Label_15
Partner-marketing Label_53
Neutral Label_75
Infra Label_47
CATEGORY_SOCIAL CATEGORY_SOCIAL
Sales/Marktn/Bizdev/EU-Bizdev Label_26
Sales/Marktn/Marketing Label_29
Pub-commits Label_50
Org List/Architecture Label_16
Operations/Com-Operations Label_35
Sales/Marktn/Partner Marktn Label_33
Sup-sales Label_51
testingForFun Label_72
Sales/Marktn/Bizdev/Canada Bizdev Label_38
Org List/Carbon Dev Label_17
Marketing Label_44
Sales/Marktn Label_36
Tech Content Label_39
Org List Label_19
Everyone/Team Group Label_11
PeopleHR/People Info Label_59
Everyone/News Label_10
1. Me/Graduate Study Programme Label_66
VeryPositive Label_77
Engineering Label_22
Everyone/Club Label_3
CATEGORY_FORUMS CATEGORY_FORUMS
Ballerina Label_68
PeopleHR Label_58
Training Label_42
Negative Label_74
Engineering/Support Dev Label_4
Eng Label_49
Sup-jira Label_52
Org List/Commits Label_18
Sales/Marktn/Bizdev Label_37
Sales/Marktn/Pre Sales Label_30
BizDev Label_69
Everyone/Training Label_2
Sales/Marktn/Bizdev/Gen Bizdev Label_27
Everyone/Extern Traing Label_34
Sup-dev Label_46
Vacation Label_13
IMPORTANT IMPORTANT
Archi Label_54
Sales/Marktn/Sales Group Label_31
Positive Label_76
WSO2 Con Label_12
Infastructure Label_6
1. Me/HR Team Label_62
VeryNegative Label_73
1. Me Label_56
Product Mangt Label_32
Sales Label_43
3. Jobs/Pacific Controls Label_60
Engineering/Support JIRA Label_5
Operations/LK-Operations Label_8
Engineering/Eng Group Label_21
Everyone Label_20
CATEGORY_UPDATES CATEGORY_UPDATES
4. Club Label_64
CHAT CHAT
SENT SENT
5. Team Label_63
Everyone/Strategy Label_1
INBOX INBOX
TRASH TRASH
CATEGORY_PROMOTIONS CATEGORY_PROMOTIONS
Operations Label_23
Sales/Marktn/Bizdev/MEAP-Bzdev Label_40
DRAFT DRAFT
SPAM SPAM
STARRED STARRED
UNREAD UNREAD
Sales/Marktn/Bizdev/Americas Bizdev Label_25
Stratergy Label_55
Sup-commit Label_45
Everyone/Library Label_7
Operations/US-Operations Label_9
3. Jobs/Careers-group Label_61
Sales/Marktn/Billing Label_24

'''