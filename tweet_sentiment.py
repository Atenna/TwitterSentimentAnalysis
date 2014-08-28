import sys
import json


tweet_file = 0
sent_file = 0

def hw():
    afinnfile = sent_file
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  
      scores[term] = int(score)
    coef = 0
    for tweet in tweet_file:
      dic = json.loads(tweet)
      if 'text' in dic.keys():
	textp = dic['text']
        sentence = textp.split(" ")
        for word in sentence:
	  word = word.lower()
	  coef = coef + scores.get(word, 0)
	print coef
	coef = 0

    #for tweet in tweet_file:
    #  print tweet
    #  print "\n"

    # Print every (term, score) pair in the dictionary
    # print scores.items() 
    # print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    global tweet_file
    global sent_file
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
