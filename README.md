# SentimentAnalysis
Sentiment analysis refers to the use of natural language processing and text analysis to identify, extract and study affective
states and subjective information. Sentiment analysis is applied to texts, such as online reviews and social media to identify the customers emotion.
Here the sentiment analysis is done via 3 methods.
	1. Afinn method
	2. Bag of words
	3. StanfordCoreNLP
All these 3 methods are combined together to obtain a higher accuracy result.

Getting Started

Download the StanfordCoreNLP server.
In order to use the StanfordCoreNLP method, the stanfordCoreNLP should be runnning.

Run the server from the following command.


java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000.


To access the gmail account the user should get the authentication by following the link


https://developers.google.com/gmail/api/quickstart/python


The downloaded client_secret.json should be saved in the same directory as the other files.


Next the labels should be manually created in the Gmail.
	1. Very_negative
	2. Negative
	3. Neutral
	4. Positive
	5. Very_positive

When creating these labels, each label is automatically assigned with a label ID.
This label ID should me manually gathered and edited in the code in order for the emails to be labeled accordingly.

<<<<<<< HEAD
By the running the piece of code which is commented in at the end of the gmailAPI.py file, the label IDs can be obtained.

While running the gmailAPI.py, it would access the gmail API and get the unread emails, call the funtion calemotionalLevel() in the sentiment.py and return an emotional level to a particular email.
=======
gmailAPI.py would call the funtion calemotionalLevel() in the sentiment.py and return an emotional level to a particular email.
>>>>>>> version5
