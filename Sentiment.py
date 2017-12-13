from pycorenlp import StanfordCoreNLP
import math
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#from test import  authenticate

#Afinn method--------------------------------------------------------------------------
#authenticate()
afinnText = open('afinn.txt')
afinn = dict(map(lambda (w, s): (w, int(s)), [ws.strip().split('\t') for ws in afinnText ]))
pattern_split = re.compile(r"\W+")

def sentimentAfinn(text):

    words = pattern_split.split(text.lower())
    sentiments = map(lambda word: afinn.get(word, 0), words)
    if sentiments:
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))

    else:
        sentiment = 0


    return sentiment

#StanfordNLP method---------------------------------------------------------------------
def calSentimentLevel(sentimentRate):
    slevel = 0
    if sentimentRate >= 5:
        slevel = 2
    elif sentimentRate >= 1 and sentimentRate < 5:
        slevel = 1
    elif sentimentRate == 0:
        slevel = 0
    elif sentimentRate <= -5:
        slevel = -2
    elif sentimentRate <= -1 and sentimentRate > -5:
        slevel = -1
    return slevel



def stanfordNLP(data):
    sentimentLevel = 0

    nlp = StanfordCoreNLP('http://localhost:9000')
    res = nlp.annotate(data,properties={'annotators': 'sentiment','outputFormat':'json','timeout': 100000})
    #print (res)
    for i in res["sentences"]:
        val = int(i["sentimentValue"])
        if i["sentiment"] == "Verypositive":
            sentimentLevel = sentimentLevel + val + 5

        elif i["sentiment"] == "Positive":
            sentimentLevel = sentimentLevel + val + 1

        elif i["sentiment"] == "Neutral":
            sentimentLevel = 0

        elif i["sentiment"] == "Negative":
            sentimentLevel = sentimentLevel - val - 1

        elif i["sentiment"] == "Verynegative":
            sentimentLevel = sentimentLevel - val - 5

    stanfordLevel = calSentimentLevel(sentimentLevel)
    return stanfordLevel


#Bag of words method-----------------------------------------------------------------------
def bagofwords(email):
    email = email.replace(".", " ")
    email = email.replace("?", " ")
    email = email.replace("!", " ")

    count = 0
    sentiBOW = 0
    for word in email.split():
        x = ','+word+','
        if x in open('positivewords.txt').read():
            count = count + 1

        if x in open('negativewords.txt').read():
            count = count - 1

    if count <= -20:
        sentiBOW = -2
    elif count < 0:
        sentiBOW = -1
    elif count == 0:
        sentiBOW = 0
    elif count >= 20:
        sentiBOW = 2
    elif count > 0:
        sentiBOW = 1

    return sentiBOW
#------------------------------------------------------------------------------------------

def calEmotionalLevel(email):
    emotionalLevel = ""
    tmp = 0
    sentiAF = sentimentAfinn(email)
    sentiBOW = bagofwords(email)
    sentiSNLP = stanfordNLP(email)

    Slvl = sentiAF + sentiBOW + sentiSNLP

    if Slvl >= 3:
        emotionalLevel = "very positive"
        tmp = 2
    elif Slvl >= 1.5 and Slvl < 3:
        emotionalLevel = "positive"
        tmp = 1
    elif Slvl >= -1.5 and Slvl < 1.5:
        emotionalLevel = "neutral"
        tmp = 0
    elif Slvl <= -1.5 and Slvl > -3:
        emotionalLevel = "negative"
        tmp = -1
    elif Slvl <= -3:
        emotionalLevel = "very negative"
        tmp = -2

    #print (email)
    #print ("afinn "+ str(sentiAF))
    #print ("bow "+ str(sentiBOW))
    #print ("NLP "+ str(sentiSNLP))
    print ("the slvl is: " + str(Slvl))
    #print ("The Average Sentiment Level is: " + str(emotionalLevel))
    #print ('\n')
    #return emotionalLevel
    return tmp

def tes(email):
    sentiAF = sentimentAfinn(email)
    sentiBOW = bagofwords(email)
    sentiSNLP = stanfordNLP(email)
    Slvl = sentiAF + sentiBOW + sentiSNLP
    return  Slvl
