import sys
import json

sent_file = 0
tweet_file = 0
scores = 0
unknown = 0

def hw():
    afinnfile = sent_file
    global scores
    global unknown
    scores = {} # initialize an empty dictionary for known words
    unknown = {} # initialize a dictionary for new words
    for line in afinnfile:
      term, score  = line.split("\t")  
      scores[term] = int(score)
    #print scores.items() 
    
    for tweet in tweet_file:
      dic = json.loads(tweet)
      coef = calculate_sentiment(tweet)
      if 'text' in dic.keys():
        textp = dic['text']
        sentence = textp.split(" ")
 	for word in sentence:
       	  word = word.lower()
       	  if word not in scores: 
	    unknown[word] = unknown.get(word, 0) + coef

    for key, value in unknown.items():
      if isinstance(value, int):
        print key, value


def lines(fp):
    print str(len(fp.readlines()))

#method to calculate sentiment of a tweet
def calculate_sentiment(tweet):
    dic = json.loads(tweet)
    coef = 0
    if 'text' in dic.keys():
      textp = dic['text']
      sentence = textp.split(" ")
      for word in sentence:
	word = word.lower()
	if word in scores: 
	  coef = coef + scores.get(word, 0)
    return coef


def main():
    global sent_file
    global tweet_file
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
