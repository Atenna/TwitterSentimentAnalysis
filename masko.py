import sys
import json
import re
import codecs

tweet_file = 0
unknown = 0
sum_wordsUK = 0
sum_wordsNY = 0
sum_tweetsUK = 0
sum_tweetsNY = 0
sum_words = 0
sum_tweets = 0

def hw():

    global unknown
    global sum_wordsUK
    global sum_wordsNY
    global sum_tweetsUK    
    global sum_tweetsNY
    global sum_words
    global sum_tweets

    for tweet in tweet_file:
      dic = json.loads(tweet) # naloaduju sa tweety v json formate do dictionary struktury
      if 'text' in dic.keys() and dic['lang'] == 'en': #ak obsahuju tweety text a su v anglictine (pravdepodobne)
        user = dic['user']
	sum_tweets = sum_tweets + 1
	textp = dic['text'] #v premennej textp je text tweetu
	sentence = textp.split(' ')
	sum_words = len(sentence)
	writing_len = sum_words * 0.125 #in minutes
	#print "tweet number " + str(sum_tweets) + " was writed " + str(writing_len) + " minutes."
	#print str(writing_len)
	print str(sum_words)
'''     loc = user['location'].encode('ascii', 'ignore').decode('ascii') #nech tam nie je nejaka azbuka ako vcera vecer
	if len(loc)> 4 and loc[-4:-2].encode("utf8") == ", ":
	  textp = dic['text'] #v premennej textp je text tweetu
	  #print loc
	  state = (str(loc[-2:]))
	  state = (str(loc[-2:])).encode('ascii', 'ignore').decode('ascii')
	  if state == "UK":
		  print user['location']
		  print str(sum_tweetsUK) + 'nth tweet from UK ----> '	
         	  	
		  #print textp
		  sentence = textp.split(' ')
		  print "number of words in this tweet: " + str(len(sentence))
		  sum_tweetsUK = sum_tweetsUK + 1; #pocet tweetov s ktorymi pracujeme
	 	  sum_wordsUK = sum_wordsUK + len(sentence) #spocitame vsetky slova v tweetoch
	  if state == "NY":
		  print user['location']
		  print str(sum_tweetsUK) + 'nth tweet from NY ----> '	
         	  	
		  #print textp
		  sentence = textp.split(' ')
		  print "number of words in this tweet: " + str(len(sentence))
		  sum_tweetsNY = sum_tweetsNY + 1;
	 	  sum_wordsNY = sum_wordsNY + len(sentence)
'''
    
'''
    print "pocet tweetov: "
    print sum_tweetsUK + sum_tweetsNY
    print "pocet slov spolu: "
    print sum_wordsUK + sum_wordsNY
    print "priemerny pocet slov = pocet slov spolu / pocet tweetov: "
    print ((sum_wordsUK + sum_wordsNY)*(1.0) / (sum_tweetsUK + sum_tweetsNY)*(1.0))
    print "priemerny pocet slov v UK"
    print ((sum_wordsUK)*(1.0) / (sum_tweetsUK)*(1.0))
    print "priemerny pocet slov v NY"
    print ((sum_wordsNY)*(1.0) / (sum_tweetsNY)*(1.0))
'''

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
