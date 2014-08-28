import sys
import json
import re

#sent_file = 0
tweet_file = 0
#scores = 0
unknown = 0
sum_words = 0

def hw():
    #afinnfile = sent_file
#    global scores
    global unknown
    global sum_words
#    scores = {} # initialize an empty dictionary for known words
    unknown = {} # initialize a dictionary for new words
    sum_words = 0
#    for line in afinnfile:
#      term, score  = line.split("\t")  
#      scores[term] = int(score)
    #print scores.items() 
    
    for tweet in tweet_file:
      dic = json.loads(tweet)
      #coef = calculate_sentiment(tweet)
      if 'text' in dic.keys() and dic['lang'] == 'en':
        textp = dic['text']
        sentence = textp.split(' ')
 	for word in sentence:
       	  word = word.lower()
	  word = re.sub('[^a-z]', "", word)	
          sum_words = sum_words + 1
       	  unknown[word] = unknown.get(word, 2000) + 1

    for key, value in unknown.items():
      if isinstance(value, int) and len(key) != 0 and key != "\n" and key != " " and value != None:
        print key.encode('utf8'), (value/(sum_words*(1.0)))
        #print "ababaX K".sub('[^a-z]', "X")
    #print unknown['you!']
    #print unknown['indirect']
    #print "Ahoj       ahoj".split(" ")

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
    #global sent_file
    global tweet_file
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
