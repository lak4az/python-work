## Name: Logan King
## File: exam-solns.py (STAT 3250)
## Topic: Exam 3 Solutions
##

##  Exam 3 consists of three sections.  All code should be submitted as a single 
##  Python file.  Section 3 is on creating plots.  The plots will be submitted 
##  in a separate PDF document.

#import relevant packages
import numpy as np
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import json

####
####  Section A
####

##  For this portion of Exam 3 you will be working with Twitter data related
##  to the season opening of Game of Thrones on April 14.  You will use a set
##  of 10,790 tweets for this purpose.  The data is in the file 'GoTtweets.txt'.  
##  The code below can be used to import the data into a list, with each
##  list element a dict of the tweet object.

# Read in the tweets and append them to 'tweetlist'
tweetlist = []
for line in open('C:/Users/Student/Downloads/GoTtweets.txt', 'r'): # Open the file of tweets
    tweetlist.append(json.loads(line))  # Add to 'tweetlist' after converting

## A1. The tweets were downloaded in several groups at about the same time.
##     Are there any that appear in the file more than once?  List the tweet 
##     ID for any repeated tweets, along with the number of times each is
##     repeated.
    
t_id = [] #create empty list for tweet id
for t in tweetlist: #loop over tweetlist
    t_id.append(t['id']) #take id from each tweet and append to t_id
group_a1 = pd.Series(t_id).value_counts() 
#convert to series and find value counts
group_a1[group_a1>1] #find which tweets appeared more than once

'''
#A1
1117608744639025152    2
1117608741099069440    2
1117619562588057600    2
1117619559043948544    2
dtype: int64
#ID for any repeated tweets, along with the number of times each is repeated
'''

## Note: For the remaining questions in this section, do not worry about 
##       the duplicate tweets.  Just answer the questions based on the 
##       existing data set.
    
## A2. Some tweeters like to tweet a lot.  Find the screen name for all 
##     tweeters with at least 5 tweets in the data.  Give the screen name
##     and the number of tweets.  

s_n = [] #create empty list for screen name
for t in tweetlist: #loop over tweetlist
    s_n.append(t['user']['screen_name']) 
    #take each screen name nested in user and append to screen name
group_a2 = pd.Series(s_n).value_counts()
#convert to series and find value counts
group_a2[group_a2>=5]
#find which tweeted at least 5 times

'''
#A2
Eleo_Ellis         6
taehyungiebtsdm    6
Czo18              5
caioomartinez      5
_sherycee          5
dtype: int64
#tweeters with at least 5 tweets in the data
'''

## A3. Determine the number of tweets that include the hashtag '#GoT', then
##     repeat for '#GameofThrones'.
##     Note: Hashtags are not case sensitive, so any of '#GOT', '#got', 'GOt' 
##     etc are all considered matches.  Each tweet object has a list of
##     hashtag objects -- use those for this problem, not the text of the
##     tweet.

ht = [] #create empty list for hashtag
for t in tweetlist: #loop over tweetlist
    hts=t['entities']['hashtags'] #save hashtags of t
    for h in hts: #for each hashtag
        ts = h['text'].lower() #make lowercase
        ht.append(ts) #append to hashtag list
pd.Series(ht).value_counts().nlargest(2) 
#convert ht to series,take value counts,
#top two happen to be what we're looking for

'''
#A3
gameofthrones    8364
got              1032
dtype: int64
#number of tweets that include the hashtag '#GoT', then
#repeat for '#GameofThrones'
'''

## A4. Among the screen names with 4 or more tweets, find the 
##     'followers_count' for each and then give a table of the top-5 
##     (plus ties) in terms of number of followers. Include the screen 
##     name and number of followers.  (If the number of followers changes
##     for a given screen name, then report the average number of followers 
##     among all of the tweeter's tweets.) 

s_n = [] #create empty list for screen name
for t in tweetlist: #loop over tweetlist
    s_n.append(t['user']['screen_name']) #append screen name
group_a4 = pd.Series(s_n).value_counts() 
#convert s_n to series, take value counts
list_a4 = list(group_a4[group_a4>=4].index) 
#subset to only those with 4 or more tweets, take index (screen names),
#convert to list
s_n2 = [] #make new empty list for screen names
foll = [] #make empty list for follower count
for t in tweetlist: #loop over tweetlist
    if t['user']['screen_name'] in list_a4: #if screen name is in select list
        s_n2.append(t['user']['screen_name'])
        #append screen name to new screen name list
        foll.append(t['user']['followers_count'])
        #append follower count to follower count list
df_a4 = pd.concat([pd.DataFrame(s_n2),pd.DataFrame(foll)],axis=1)
#convertnew screen name list and follower list to dataframes, concatenate
df_a4.columns = ['screen_name','followers_count']
#change column names
df_a4['followers_count'].groupby(df_a4['screen_name']).mean().nlargest(5)
#take mean of follower count, group by screen name, display 5 largest

'''
#A4
screen_name
bbystark          9313.00
Gamoraavengxr     3842.00
Eleo_Ellis        2948.00
HellblazerArts    2506.00
Dahoralu          1901.25
Name: followers_count, dtype: float64
#Among the screen names with 4 or more tweets, find the 'followers_count' 
#for each and then give a table of the top-5 (plus ties) in terms of number 
#of followers
'''

## A5. Find the mean number of hashtags included in the tweets. 

ht = [] #create empty list for hashtag
for t in tweetlist: #loop over tweetlist
    hts=t['entities']['hashtags'] #save hashtags of t
    for h in hts: #for each hashtag
        ts = h['text'].lower() #make lowercase
        ht.append(ts) #append to hashtag list
pd.Series(ht).value_counts().sum()/len(tweetlist)
#convert ht to series, take sum of value counts
#divide by total number of tweets to get mean hashtags per tweet

'''
#A5
1.0022242817423541
#mean number of hashtags included in the tweets
'''

## A6. Give a table of hashtag counts: How many tweets with 0, 1, 2, ...
##     hashtags?

htc = [] #create empty list for hashtag count
for t in tweetlist: #loop over tweetlist
    hts = t['entities']['hashtags'] #save hashtags of t
    htc.append(len(hts)) #append number of hashtags per tweet in htc
pd.Series(htc).value_counts().sort_index() 
#convert htc to series, take value counts
#sort the index to display no hashtag to most hashtag counts

'''
#A6
0     1575
1     8111
2      768
3      242
4       55
5       24
6       10
7        2
8        1
9        1
10       1
dtype: int64
#table of hashtag counts
'''

## A7. Determine the number of tweets that include 'Daenerys' (any combination
##     of upper and lower case) in the text of the tweet.  Then do the same 
##     for 'dragon'.

daenerys = 0 #set daenerys counter to 0
dragon = 0 #set dragon counter to 0
for t in tweetlist: #loop over tweetlist
    t['text'] = t['text'].lower() #change text to lower
    if 'daenerys' in t['text']: #if text contains daenerys
        daenerys += 1 #add one to daenerys count
    if 'dragon' in t['text']: #if text contains dragon
        dragon += 1 #add one to dragon
daenerys #print daenerys count
dragon #print dragon count

'''
#A7
735 #number of tweets that include daenerys
385 #number of tweets that include dragon
'''

## A8.  Determine the 5 most frequent hashtags, and the number of tweets that
##      each appears in.  As usual, give a table.

ht = [] #create empty list for hashtag
for t in tweetlist: #loop over tweetlist
    hts=t['entities']['hashtags'] #save hashtags of t
    for h in hts: #for each hashtag
        ts = h['text'].lower() #make lowercase
        ht.append(ts) #append to hashtag list
pd.Series(ht).value_counts().nlargest(5) 
#convert ht to series,take value counts, display top 5

'''
#A8
gameofthrones           8364
got                     1032
forthethrone             219
gameofthronesseason8     124
demthrones               110
dtype: int64
#the 5 most frequent hashtags, and the number of tweets that each appears in
'''

## A9.  Determine the 5 most frequent 'user_mentions', and the number of tweets 
##      that each appears in.  Give a table.

u_m = [] #create empty list for user mentions
for t in tweetlist: #loop over tweetlist
    ms = t['entities']['user_mentions'] #save user mentions of t
    for m in ms: #for each mention
        ums = m['screen_name'].lower() #record the screen name, make lowercase
        u_m.append(ums) #append to user mention list
pd.Series(u_m).value_counts().nlargest(5)
#convert to series, take value counts, display top 5 mention counts

'''
#A9
gameofthrones    502
ygorfremo         82
gotthings_        79
complex           75
tpain             60
dtype: int64
#the 5 most frequent 'user_mentions', and the number of tweets that each 
#appears in
'''

####
####  Section B
####

##  We will use the 'Stocks' data sets from Assignment 8 in this section.
##  You can see some information about the data in the assignment description.

##  The time interval covered varies from stock to stock. There are some 
##  missing records, so the data is incomplete. Note that some dates are not 
##  present because the exchange is closed on weekends and holidays. Those 
##  are not missing records. Dates outside the range reported for a given 
##  stock are also not missing records, these are just considered to be 
##  unavailable. Answer the questions below based on the data available in 
##  the files.

os.chdir('C:/Users/Student/Downloads/Stocks') #set working directory
filelist = glob.glob('*.csv')
#'*.csv' selects files ending in '.csv','glob.glob' is the directory search

# We can concatenate the dataframes into one large dataframe, 
#adding column with the stock name
B_df = pd.DataFrame()
for f in filelist:
    df = pd.read_csv(f)
    df['name']=f[:-4] #drop .csv from stock name
    B_df = pd.concat([B_df,df])

B_df['Date'] = pd.to_datetime(B_df['Date'])

## B1.  Use the collective data to determine when the market was open from 
##      January 1, 2008 to December 31, 2015. (Do not use external data for 
##      this question.) Report the number of days the market was open for 
##      each year in 2008-2015. Include the year and the number of days in 
##      table form.

B_df['Date'].dt.date.groupby(B_df['Date'].dt.year).unique().str.len()[8:16]
#take the length of unique values of date, grouped by year
#index 8:16 to obtain relevant years

'''
#B1
Date
2008    253
2009    252
2010    252
2011    252
2012    250
2013    252
2014    252
2015    252
Name: Date, dtype: int64
#the number of days the market was open for each year in 2008-2015
'''

## B2.  Determine the total number of missing records for all stocks for the 
##      period 2008-2015.

stock = np.unique(B_df['name'])
#find unique stocks
dates = pd.Series(np.unique(B_df['Date']))
#create a series of unique dates
rel_dates = dates[(dates.dt.year>=2008)&(dates.dt.year<=2015)]
#subset to only dates relevant to the problem
missing_timestamps = []
#create empty list for missing timestamps for each stock
#(will be useful later on)
ct = 0
#set counter variable to 0
for s in stock: #loop for each unique stock
    s_dat = B_df.loc[B_df['name']==s] 
    #locate where name included in stock
    s_dat_min = min(s_dat['Date'])
    #find earliest date for s
    s_dat_max = max(s_dat['Date'])
    #find latest date for s
    s_rel_dates = rel_dates[(rel_dates>=s_dat_min)&(rel_dates<=s_dat_max)]
    #subset to only include relevant dates for s
    s_missing = len(s_rel_dates[~s_rel_dates.isin(s_dat['Date'])])
    #find how many relevant dates don't have entries for s
    ct += s_missing
    #add missing dates to count
    miss_dat = s_rel_dates[~s_rel_dates.isin(s_dat['Date'])]
    #find which relevant dates don't have entries for s
    missing_timestamps.append(miss_dat.tolist())
    #append those dates to create list of timestamps
print(ct)   
#print count

'''
#B2
7168
#total number of missing records for all stocks for the period 2008-2015
'''
    
## B3.  For the period 2008-2015, find the 10 stocks (plus ties) that had the 
##      most missing records, and the 10 stocks (plus ties) with the fewest 
##      missing records. (For the latter, don't include stocks that have no 
##      records for 2008-2015.) Report the stocks and the number of missing 
##      records for each.

stock = list(stock) #turn stock from B2 into a list
b3_list = list(zip(stock,missing_timestamps)) 
#gives each list in missing_timestamps name of associated stock
b3_series = pd.Series(b3_list) #convert b3_list to series
miss_rec = [] #create empty list for miss_rec
for b in b3_series: #for each element of series
    miss_rec.append(len(b[1])) 
    #find number of missing dates and append to miss_rec
miss_rec=pd.DataFrame(miss_rec) #convert miss rec to dataframe
b3_df = pd.concat([pd.DataFrame(stock),miss_rec],axis=1)
#convert stock to dataframe and concatenate with miss_rec
b3_df.columns = ['Stock','Miss_Rec']
#rename columns
b3_df['Miss_Rec'].groupby(b3_df['Stock']).sum().nlargest(12)
#find stocks (included in this time period) with most missing records,
#display top 12 because of a tie
b3_df['Miss_Rec'].groupby(b3_df['Stock']).sum().nsmallest(10)
#find stocks (included in this time period) with least missing records,
#display top 10

'''
#B3
Stock
NBL     44
HBAN    37
RF      37
BBT     36
LB      36
PDCO    36
WAT     36
SEE     35
VRSN    35
GAS     34
HOT     34
RCL     34
Name: Miss_Rec, dtype: int64
#find stocks (included in this time period) with most missing records,
#display top 12 because of a tie

Stock
ADT     0
FB      0
GM      0
LYB     0
NAVI    0
NLSN    0
NWSA    0
TRIP    0
XYL     0
ZTS     0
Name: Miss_Rec, dtype: int64
#find stocks (included in this time period) with least missing records,
#display top 10
'''
## B4.  Identify the top-10 dates (plus ties) in 2008-2015 that are missing 
##      from the most stocks.  Provide a table with dates and counts.

missing_dates = [] #create empty list for missing dates
for m in missing_timestamps: #loop over all lists of missing timestamps
    for t in m:#loop over all timestamps in each list
        missing_dates.append(t) #append to missing dates
group_b4 = pd.Series(missing_dates).value_counts() 
#convert missing dates to series, take value counts
group_b4[group_b4>8] 
#display all counts greater than 8, there is a tie for 10th place

'''
#B4
2012-04-23    11
2011-03-08    10
2013-09-23    10
2013-01-30    10
2012-06-25     9
2009-08-05     9
2009-06-11     9
2013-04-30     9
2013-08-29     9
2009-12-24     9
2008-06-10     9
2009-04-06     9
2013-11-05     9
2008-04-03     9
2009-04-27     9
2013-07-22     9
2010-07-21     9
2009-03-16     9
2008-04-01     9
2009-08-13     9
2012-04-24     9
2011-08-01     9
2012-08-10     9
dtype: int64
#the top-10 dates (plus ties) in 2008-2015 that are missing from the most stocks
'''

##  Questions B5 and B6: For each stock, impute (fill in) the missing records 
##  using linear interpolation. For instance, suppose d1 < d2 < d3 are dates,  
##  and P1 and P3 are known Open prices on dates d1 and d3, respectively, with
##  P2 missing.  Then we estimate P2 (the Open price on date d2) with
##
##       P2 = ((d3 - d2)*P1 + (d2 - d1)*P2)/(d3 - d1)
##
##  The same formula is used for the other missing values of High, Low, Close, 
##  and Volume.  Once you have added the missing records into your data, then
##  use the new data (including the imputed records) to calculate the Python 
##  Index for each date in 2008-2015 (see Assignment 8 for the formula). 
##  Remember that weekends and holidays are not missing records, so don't 
##  impute those.  Once you're done with that, then you can answer B5 and B6.

b3_df = pd.DataFrame(b3_list)
b3_df.columns = ['name','miss_dt']
b3_df = b3_df[b3_df.miss_dt.apply(len)!=0]
s = b3_df.apply(lambda x: pd.Series(x['miss_dt']), axis=1).stack().reset_index(level=1, drop=True)
s.name = 'miss_dt'
b3_df2 = b3_df.drop('miss_dt', axis=1).join(s)
b3_df2['miss_dt'] = pd.Series(b3_df2['miss_dt'], dtype=object)
b3_df2['miss_dt'] = pd.to_datetime(b3_df2['miss_dt'])
b3_df2.columns = ['name','Date']
b3_df2 = b3_df2.reindex(columns=list(['name','Date','Open','High','Low','Close',
                                      'Volume','Adj Close']))
b3_df2 = b3_df2[['Date','Open','High','Low','Close','Volume','Adj Close','name']]
b56_df = B_df.append(pd.DataFrame(data = b3_df2), ignore_index=True)
b56_df = b56_df.sort_values(by=['name','Date'])
b56_df = b56_df[(b56_df['Date'].dt.year>=2008)&(b56_df['Date'].dt.year<=2015)]
b56_df = b56_df.reset_index(drop=True)

coli = ['Open','High','Low','Close','Volume','Adj Close']
for c in coli:
    for b in b56_df[coli]:
        i = b56_df[coli].index(b)
        if b.notnull():
            continue
        else:
            b = b56_df[coli][i-1] + b56_df[coli][i+1]/2
            b56_df[coli][i]=b

            
## B5.  Find the Open, High, Low, and Close for the imputed Python Index for 
##      each day the market was open in January 2013. Give a table the includes 
##      the Date, Open, High, Low, and Close, with one date per row.

b56_df['Open_Index'] = b56_df['Open'] * b56_df['Volume']
b56_df['High_Index'] = b56_df['High'] * b56_df['Volume']
b56_df['Low_Index'] = b56_df['Low'] * b56_df['Volume']
b56_df['Close_Index'] = b56_df['Close'] * b56_df['Volume']

j13 = b56_df[b56_df['Date'].str.contains('2013-01')]

open_ = j13.groupby('Date')['Open_Index'].sum() / j13.groupby('Date')['Volume'].sum()
high = j13.groupby('Date')['High_Index'].sum() / j13.groupby('Date')['Volume'].sum()
low = j13.groupby('Date')['Low_Index'].sum() / j13.groupby('Date')['Volume'].sum()
close = j13.groupby('Date')['Close_Index'].sum() / j13.groupby('Date')['Volume'].sum()

py_index = pd.concat([open_, high, low, close], axis=1)
py_index.columns = ['Open', 'High', 'Low', 'Close']
py_index

'''
#B5
Open       High        Low      Close
Date                                                  
2013-01-02  37.054761  37.505297  36.638862  37.228915
2013-01-03  37.032179  37.523912  36.657750  37.081912
2013-01-04  37.404633  37.863218  37.142403  37.636333
2013-01-07  39.467304  39.985991  39.121514  39.630800
2013-01-08  39.403554  39.748143  38.922081  39.354890
2013-01-09  35.024724  35.401727  34.640686  35.003027
2013-01-10  37.033616  37.421070  36.654474  37.189733
2013-01-11  38.191304  38.514559  37.833823  38.247111
2013-01-14  38.484674  38.900076  38.112640  38.526461
2013-01-15  38.200333  38.754825  37.881484  38.366129
2013-01-16  39.376960  39.755706  38.911310  39.371881
2013-01-17  35.979870  36.329769  35.648391  35.974307
2013-01-18  40.134305  40.504265  39.723440  40.230839
2013-01-22  40.567323  41.068261  40.241281  40.851074
2013-01-23  44.641020  45.344795  44.288949  44.994229
2013-01-24  48.921170  49.827586  48.346726  49.279962
2013-01-25  55.089956  58.565085  54.817362  57.965279
2013-01-28  50.963814  51.568084  49.721003  50.138855
2013-01-29  42.852754  43.719166  42.382627  43.346702
2013-01-30  45.365733  45.742741  44.516468  44.955761
2013-01-31  43.908594  44.645015  43.391417  44.108205
#Open, High, Low, and Close for the imputed Python Index for 
#each day the market was open in January 2013
'''

## B6.  Determine the mean Open, High, Low, and Close imputed Python index 
##      for each year in 2008-2015, and report that in a table that includes 
##      the year together with the corresponding Open, High, Low, and Close.

open2= b56_df.groupby('Date')['Open_Index'].sum() / b56_df.groupby('Date')['Volume'].sum()
high2 = b56_df.groupby('Date')['High_Index'].sum() / b56_df.groupby('Date')['Volume'].sum()
low2 = b56_df.groupby('Date')['Low_Index'].sum() / b56_df.groupby('Date')['Volume'].sum()
close2 = b56_df.groupby('Date')['Close_Index'].sum() / b56_df.groupby('Date')['Volume'].sum()

py_index = pd.concat([open2, high2, low2, close2], axis=1).reset_index()
py_index.columns = ['Date', 'Open', 'High', 'Low', 'Close']
py_index['Year'] = py_index['Date'].str[:4]
py_index.groupby('Year').mean()

'''
#B6
Open       High        Low      Close
Year                                            
2008  39.380067  40.282598  38.369949  39.316860
2009  27.203915  27.762914  26.660808  27.236140
2010  35.487994  35.966539  34.998897  35.505608
2011  38.709006  39.251518  38.116169  38.681309
2012  37.258081  37.740394  36.806378  37.295120
2013  47.072033  47.616081  46.539772  47.096413
2014  58.266215  58.897633  57.604711  58.269364
2015  54.358924  54.988411  53.707369  54.354561
#mean Open, High, Low, and Close imputed Python index for each year in 2008-2015
'''

####
####  Section C
####

##  This section requires the creation of a number of graphs. In addition to 
##  the code in your Python file, you will also upload a PDF document (not Word!)
##  containing your graphs (be sure they are labeled clearly).  The data file 
##  you will use is 'samplegrades.csv'.

samp_grades = pd.read_csv('C:/Users/Student/Downloads/samplegrades.csv')
#read csv and save

## C1.  Make a scatter plot of the 'Math' SAT scores (x-axis) against the 
##      'Read' SAT scores (y-axis). Label the plot 'Math vs Read' and label
##      the axes 'Math' and 'Read'.

x=samp_grades['Math']
#set x as math scores
y=samp_grades['Read']
#set y as read scores
plt.scatter(x,y)
#scatter plot with x axis as math scores, y axis as read scores
plt.title('Math vs Read') #add a title to the plot
plt.xlabel('Math') #add x-axis title
plt.ylabel('Read') #add y-axis title
#run all at once to create plot


## C2.  Make the same scatter plot as the previous problem, but this time 
##      color-code the points to indicate the 'Sect' and choose different 
##      shapes to indicate the value of 'Prev'.

#create a list of colors based on the section
colors = pd.Series(len(samp_grades)*['green'])
colors[samp_grades['Sect']=='TR930'] = 'red'
colors[samp_grades['Sect']=='TR1230'] = 'blue'
#create categories for markers
c1 = colors[samp_grades['Prev']=='Y']
c2 = colors[samp_grades['Prev']=='N']
#make graph for each level
x1 = x[samp_grades['Prev']=='Y']
x2 = x[samp_grades['Prev']=='N']
y1 = y[samp_grades['Prev']=='Y']
y2 = y[samp_grades['Prev']=='N']
#plot each
plt.scatter(x1,y1,marker='^',c=c1)
plt.scatter(x2,y2,marker='o',c=c2)
#add titles and legend
plt.title('Math vs Read, Colored by Section, Shaped by Previous') 
plt.xlabel('Math') #add x-axis title
plt.ylabel('Read') #add y-axis title
#run all at once to create plot

## C3.  Make a histogram of the values of 'CourseAve'. Label the graph 
##      'Course Averages'.

x = samp_grades['CourseAve'] #set x as course averages
plt.hist(x) #plot histogram of x
plt.title('Course Averages') #add title to plot
#run all together to create plot

## C4.  Make a histogram of the values of 'Final' with color-coded portions 
##      indicating whether they scored at least 75 on the Midterm. Give 
##      the graph appropriate labels.

x = samp_grades['Final']
#set x as final grades
x1 = x[samp_grades['Midterm']>=75]
#create category for midterm >=75
x2 = x[samp_grades['Midterm']<75]
#create category for midterm <75
plt.hist([x1,x2], color=['blue','orange'])
#plot histogram
#add axis titles, legend, and plot title
plt.xlabel("Final Score")
plt.ylabel("Frequency")
plt.legend(['Midterm Score >= 75', 'Midterm Score < 75'])
plt.title('Histogram of Final Scores, coded by Midterm Score')
#run all at once to create plot

## C5.  Make a bar chart of the counts for the different values of Year. 
##      Give the graph appropriate labels.
counts = samp_grades['Year'].value_counts() #count for each year
years = counts.index  #list of year, in order of 'counts'
plt.bar(years,counts) #plot bar graph
plt.xticks(years) #remove irrelevant tick marks
#add titles
plt.xlabel("Year")
plt.ylabel("Count")
plt.title('Count of Each Year')
#run together to create plot

## C6.  Make side-by-side box-and-whisker plots for the 'CourseAve' for each 
##      distinct 'Sect'. Give the graph appropriate labels.

#create different categories for each section
data1 = samp_grades.loc[samp_grades['Sect']=='MW200','CourseAve']
data2 = samp_grades.loc[samp_grades['Sect']=='TR930','CourseAve']
data3 = samp_grades.loc[samp_grades['Sect']=='TR1230','CourseAve']
#bring together each section
data = [data1,data2,data3]
#create a boxplot for the data
plt.boxplot(data)
#set ticks as each section
plt.xticks([1, 2, 3], ['MW200', 'TR930', 'TR1230'])
#add titles
plt.xlabel("Section")
plt.ylabel("Course Average")
plt.title("Course Average by Section Boxplot")
#run together to create plot
