#pip install textblob
#Usage: getsentiment()
#input: "text"
#output: "positive/negative"
#Polarity :float ,range of [-1,1]
#Subjectivity:float ,range of [0,1]
from textblob import TextBlob

def getsentiment():
    text = input("Enter text to get its sentiment")
    blob = TextBlob(text)
    sentiment_value =blob.sentiment
    polarity_score,subjectivity_score=sentiment_value[0],sentiment_value[1]
    if polarity_score>=0 :
        return "Its Positive"
    else:
        return "Its Negative"

print(getsentiment())
