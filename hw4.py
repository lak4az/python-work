## Name: Logan King
## File: assignment04.py (STAT 3250)
## Topic: Assignment 4
##
import numpy as np
import pandas as pd
import re
##  This assignment requires the data file 'airline_tweets.csv'.  This file
##  contains records of over 14000 tweets and associated information related
##  to a number of airlines.  You should be able to read this file in using
##  the usual pandas methods.
airline_tweets = pd.read_csv('C:/Users/Student/Downloads/airline_tweets.csv')
##  Note: Questions 1-9 should be done without the use of loops.  
##        Questions 10-13 can be done with loops.

## 1.  Determine the number of tweets for each airline, indicated by the
##     name in the 'airline' column of the data set.  Give the airline 
##     name and number of tweets in table form.

airline_group = airline_tweets['airline'].groupby(airline_tweets['airline'])
#group by airline
airline_group.count()
#give count of each airline
'''
#1 Determine the number of tweets for each airline, indicated by the
##     name in the 'airline' column of the data set
airline
American          2759
JetBlue           2222
Southwest         2420
US Airways        2913
United            3822
Virgin America     504
Name: airline, dtype: int64
'''

## 2.  For each airlines tweets, determine the percentage that are positive,
##     based on the classification in 'airline_sentiment'.  Give a table of
##     airline name and percentage, sorted from largest percentage to smallest.

pos_airline_tweets = airline_tweets[airline_tweets['airline_sentiment'] == 'positive']
#mask airline tweets to create dataframe with just positive tweets
pos_group = pos_airline_tweets['airline'].groupby(pos_airline_tweets['airline'])
#group positive df by airline
percent_pos = pos_group.count()/airline_group.count()*100
#find count of positive airline tweets divided by count of total airline tweets (from Q1)
#times 100 for percent
percent_pos.sort_values(ascending=False)
#sort values descending
'''
#2 table of
##     airline name and percentage, sorted from largest percentage to smallest
airline
Virgin America    30.158730
JetBlue           24.482448
Southwest         23.553719
United            12.872841
American          12.178325
US Airways         9.234466
Name: airline, dtype: float64
'''

## 3.  List all user names (in the 'name' column) with at least 20 tweets
##     along with the number of tweets for each.  Give the results in table
##     form sorted from most to least.

user_group = airline_tweets['name'].groupby(airline_tweets['name'])
#group by usernames
user_count = user_group.count()
#get count of each username and save
user_count[user_count >= 20].sort_values(ascending=False)
#mask user count to users with more than 20 tweets and sort descending
'''
#3 all user names (in the 'name' column) with at least 20 tweets
##     along with the number of tweets for each
name
JetBlueNews        63
kbosspotter        32
_mhertz            29
otisday            28
throthra           27
weezerandburnie    23
rossj987           23
MeeestarCoke       22
GREATNESSEOA       22
scoobydoo9749      21
jasemccarty        20
Name: name, dtype: int64
'''

## 4.  Determine the percentage of tweets from users who have more than one
##     tweet in this data set.

len(user_count[user_count > 1])/len(user_count)*100
#mask user count to only display those with more than one tweet, find length of table
#that gives us the number of users with more than one tweet. Then divide by the 
#lenth of total users to get proportion with more than one tweet. 
#multiply by 100 for percent
'''
#4 percentage of tweets from users who have more than one
##     tweet
38.955979742890534
'''

## 5.  Among the negative tweets, which five reasons are the most common?
##     Give the percentage of negative tweets with each of the five most 
##     common reasons.  Sort from most to least common.

neg_airline_tweets = airline_tweets[airline_tweets['airline_sentiment'] == 'negative']
#mask airline tweets to create df with only negative tweets
neg_group = neg_airline_tweets['negativereason'].groupby(neg_airline_tweets['negativereason'])
#group negative tweets by negative reason
neg_pcts = neg_group.count()/len(neg_airline_tweets)*100
#find the count of each negative reason and divide by total number of negative tweets
#multiply by 100 to get percent
neg_pcts.sort_values(ascending=False).nlargest(5)
#sort descending and show top 5
'''
#5 Give the percentage of negative tweets with each of the five most 
##     common reasons
negativereason
Customer Service Issue    31.706254
Late Flight               18.141207
Can't Tell                12.965788
Cancelled Flight           9.228590
Lost Luggage               7.888429
Name: negativereason, dtype: float64
'''

## 6.  How many of the tweets for each airline include the phrase "on fleek"?
np.sum(airline_tweets.text.str.contains('on fleek'))
#find the tweets that contain all fleek and take the sum
'''
#6 tweets for each airline include the phrase "on fleek"
146
'''

## 7.  What percentage of tweets included a hashtag?
np.sum(airline_tweets.text.str.contains('#'))/len(airline_tweets.text)*100
#find the sum of tweets that contain a hashtag, divide by total number of tweets
#multiply by 100
'''
#7 percentage of tweets included a hashtag
17.001366120218577
'''
                                        
## 8.  How many tweets include a link to a web site?
np.sum(airline_tweets.text.str.contains('http'))
#since links start with http or https, find sum of strings that contain each and add
'''
#8 tweets include a link to a web site
1173
'''

## 9.  How many of the tweets include an '@' for another user besides the
##     intended airline?
len(airline_tweets.text.str.count('@')[airline_tweets.text.str.count('@')>1])
#take count @ in each string
#mask that to only display those tweets with more than one @
#take length of that
'''
#9 tweets include an '@' for another user besides the
##     intended airline
1645
'''

## 10. Suppose that a score of 1 is assigned to each positive tweet, 0 to
##     each neutral tweet, and -1 to each negative tweet.  Determine the
##     mean score for each airline, and give the results in table form with
##     airlines and mean scores, sorted from highest to lowest.
sentiment_value = [] #create blank array for sentiment value
for i in range(len(airline_tweets.airline_sentiment)): 
    #loop for range of length of airline_sentiment array in dataframe
    if airline_tweets.airline_sentiment[i] == 'positive':
        sentiment_value.append(1)
        #append 1 to the array if positive sentiment
    if airline_tweets.airline_sentiment[i] == 'neutral':
        sentiment_value.append(0)
        #append 0 to array if neutral sentiment
    if airline_tweets.airline_sentiment[i] == 'negative':
        sentiment_value.append(-1)
        #append -1 to array if negative sentiment
airline_tweets['sentiment_value'] = sentiment_value
#append the array to airline tweets df
sent_group = airline_tweets['sentiment_value'].groupby(airline_tweets['airline'])
#group airline tweets by their sentiment value
sent_group.mean().sort_values(ascending=False)
#take mean of sentiment values for each airline and sort descending
'''
#10 Determine the
##     mean score for each airline, and give the results in table form with
##     airlines and mean scores, sorted from highest to lowest
airline
Virgin America   -0.057540
JetBlue          -0.184968
Southwest        -0.254545
United           -0.560178
American         -0.588619
US Airways       -0.684518
Name: sentiment_value, dtype: float64
'''

## 11. Among the tweets that "@" a user besides the indicated airline, 
##     what percentage include an "@" directed at the other airlines 
##     in this file? (Note: Twitterusernames are not case sensitive, 
##     so '@MyName' is the same as '@MYNAME' which is the same as '@myname'.)
airlines = ['@virginamerica','@united','@southwestair','@jetblue', '@usairways','@americanair']
#create list of airline twitter handles
def mult(text): #create function
    ct = 0 #set count to 0
    for i in airlines: #loop for each airline twitter handle
        if text.count(i) >=1: #if the airline appears once or more in string
            ct += 1 #add 1 to count
    if ct >= 2: #if count is greater than or equal to 2
        return True #return true
    else: #else
        return False #return false
over1 = airline_tweets[airline_tweets['text'].str.count('@')>1] 
#find number of tweets with more than one mention
ans11 = over1['text'].str.lower().apply(mult).sum()/len(over1)*100
#make text of tweets with more than one mention lowercase and apply the function, 
#take sum of output, divide by length of tweets with more than one mention
#multiply by 100 for percent
ans11 #print answer
'''
#11 percentage include an "@" directed at the other airlines
21.458966565349545
'''

## 12. Suppose the same user has two or more tweets in a row, based on how they 
##     appear in the file. For such tweet sequences, determine the percentage
##     for which the most recent tweet (which comes nearest the top of the
##     file) is a positive tweet.
prev = airline_tweets.iloc[0:-2,].reset_index() #all rows before last two rows
dur = airline_tweets.iloc[1:-1,].reset_index() #all rows except first and last rows
post = airline_tweets.iloc[2:,].reset_index() #all rows after first two rows
rate = dur['airline_sentiment'][(prev['name']!=dur['name'])&(dur['name']==post['name'])]
#rows with same user tweeting sight after they tweeted
np.mean(rate == 'positive')*100
#percentage of tweets that are positive
'''
#12 determine the percentage
##     for which the most recent tweet (which comes nearest the top of the
##     file) is a positive tweet
11.189634864546525
'''


## 13. Give a count for the top-10 hashtags (and ties) in terms of the number 
##     of times each appears.  Give the hashtags and counts in a table
##     sorted from most frequent to least frequent.  (Note: Twitter hashtags
##     are not case sensitive, so '#HashTag', '#HASHtag' and '#hashtag' are
##     all regarded as the same. Also ignore instances of hashtags that are
##     alone with no other characters.)
airline_tweets = pd.read_csv('C:/Users/Student/Downloads/airline_tweets.csv') 
#reinitialize dataframe
airline_tweets.text.str.lower().str.extractall(r'(\#\w+)')[0].value_counts().head(10)
#make all tweets lowercase, extract every hashtag in each string
#take counts of each, display top 10
'''
#13 Give the hashtags and counts in a table
##     sorted from most frequent to least frequent
#destinationdragons    81
#fail                  69
#jetblue               48
#unitedairlines        45
#customerservice       36
#usairways             30
#neveragain            27
#americanairlines      27
#united                26
#usairwaysfail         26
Name: 0, dtype: int64
'''






