## Name: Logan King
## File: assignment09.py (STAT 3250)
## Topic: Assignment 9 
##

##  This assignment requires data from the file 
##
##      'ncaa.csv':  NCAA Men's Tournament Scores, 1985-2019
##
##  The organization of the file is fairly clear.  Each record has information
##  about one game, including the year, the teams, the final score, and each 
##  team's tournament seed.  All questions refer only to the data in this
##  file, not to earlier tournaments.

##  Note: The data set is from Data.World, with the addition of the 2019
##  tournament provided by your dedicated instructor.
import numpy as np
import pandas as pd

ncaa = pd.read_csv('C:/Users/Student/Downloads/ncaa.csv')

## 1.  Find all schools that have won the championship, and make a table that
##     incluldes the school and number of championships, sorted from most to
##     least.

mask1 = ncaa[ncaa['Round']==6]
#mask to only include championship rounds
mask1['champs']=''
#create empty column for champions
for i in range(len(mask1)): #loop for all rows
    if mask1.iloc[i,5]>mask1.iloc[i,8]: #if score > score.1
        mask1.iloc[i,10] = mask1.iloc[i,6] #set champs as team
    else: #else
        mask1.iloc[i,10] = mask1.iloc[i,7] #set champs as team.1
mask1['champs'].value_counts() #find how many times each champ appears

'''
#1
Duke              5
Connecticut       4
North Carolina    4
Kentucky          3
Villanova         3
Florida           2
Kansas            2
Louisville        2
UCLA              1
Virginia          1
Arkansas          1
UNLV              1
Michigan St       1
Maryland          1
Indiana           1
Michigan          1
Syracuse          1
Arizona           1
Name: champs, dtype: int64
#all schools that have won the championship, and how many times they have won
'''

## 2.  Find the top-10 schools based on number of tournament appearances.
##     Make a table that incldes the school name and number of appearances,
##     sorted from most to least.  Include all that tie for 10th position
##     if necessary.

mask2 = ncaa[ncaa['Round']==1]
#mask to only include first round
(mask2['Team'].append(mask2['Team.1'])).value_counts().nlargest(11)
#append team columns, take value counts, display top 11 since there is a tie

'''
#2
Kansas            34
Duke              34
North Carolina    32
Arizona           32
Kentucky          30
Michigan St       29
Syracuse          28
Louisville        26
Oklahoma          26
Texas             26
Purdue            26
dtype: int64
#top-10 schools based on number of tournament appearances
#top 11 displayed due to a tie
'''

## 3.  Determine the average tournament seed for each school, then make a
##     table with the 10 schools that have the lowest average (hence the
##     best teams). Sort the table from smallest to largest, and include
##     all that tie for 10th position if necessary.

mask3 = ncaa[ncaa['Round']==1]
#mask to only include opening round
mask3a = mask3[['Seed','Team']]
#mask to only include seed and team
mask3b = mask3[['Seed.1','Team.1']]
#mask to only include seed.1 and team.1
mask3b.columns = ['Seed','Team']
#change column names so appending works
all3 = mask3a.append(mask3b)
#append into one dataframe
all3['Seed'].groupby(all3['Team']).mean().nsmallest(10)
#take mean of seed grouped by team and display smallest 10

'''
#3
Team
Duke               2.176471
Kansas             2.500000
North Carolina     2.718750
Kentucky           3.566667
Connecticut        3.950000
Loyola Illinois    4.000000
Massachusetts      4.375000
Syracuse           4.428571
Arizona            4.437500
Ohio St            4.450000
Name: Seed, dtype: float64
#the 10 schools that have the lowest average seed
'''

## 4.  Give a table of the average margin of victory by round, sorted by
##     round in order 1, 2, ....

df4 = ncaa
#create df for this problem
df4['mov']=np.abs(df4['Score']-df4['Score.1'])
#create column for margin of victory
df4['mov'].groupby(df4['Round']).mean()
#take mean of margin of victory, grouped by round

'''
#4
Round
1    12.956250
2    11.275000
3     9.917857
4     9.707143
5     9.485714
6     8.257143
Name: mov, dtype: float64
#table of the average margin of victory by round
'''

## 5.  Give a table of the percentage of wins by the higher seed by round,
##     sorted by round in order 1, 2, 3, ...

df5 = ncaa
#create df for this problem
df5['highw']=''
#create column for higher seed win
for i in range(len(df5)): #loop for each row
    if ((df5.iloc[i,4] < df5.iloc[i,9] and df5.iloc[i,5]>df5.iloc[i,8]) or
        #if team is better seed and has higher score, or
        (df5.iloc[i,9] < df5.iloc[i,4] and df5.iloc[i,8]>df5.iloc[i,5])):
        #team.1 is better seed and has higher score
        df5.iloc[i,10] = 1 #set high win column as 1
    else: #else
        df5.iloc[i,10] = 0 #set high win column as zero
df5['highw'].groupby(df5['Round']).sum()/df5['Round'].value_counts()*100
#find amount of better seed wins, grouped by round
#divide by total games per round, multiply by 100 for percent

'''
#5
Round
1    74.285714
2    71.250000
3    71.428571
4    55.000000
5    48.571429
6    57.142857
dtype: float64
#table of the percentage of wins by the higher seed by round
'''

## 6.  Determine the average seed for all teams in the Final Four for each
##     year.  Give a table of the top-5 in terms of the lowest average seed
##     (hence teams thought to be better) that includes the year and the
##     average, sorted from smallest to largest.

mask6 = ncaa[ncaa['Round']==5]
#mask to only include opening round
mask6a = mask6[['Year','Seed']]
#mask to only include seed and team
mask6b = mask6[['Year','Seed.1']]
#mask to only include seed.1 and team.1
mask6b.columns = ['Year','Seed']
#change column names so appending works
all6 = mask6a.append(mask6b)
#append into one dataframe
all6['Seed'].groupby(all6['Year']).mean().nsmallest(8)
#average of seed grouped by year, display top 8 (since there is a tie)

'''
Year
2008    1.00
1993    1.25
2007    1.50
1991    1.75
1997    1.75
1999    1.75
2001    1.75
2009    1.75
Name: Seed, dtype: float64
#table of the top-5 years in terms of the lowest average seed
#top 8 displayed due to a tie
'''

## 7.  For the first round, determine the percentage of wins by the higher
##     seed for the 1-16 games, for the 2-15 games, ..., for the 8-9 games.
##     Give a table of the above groupings and the percentage, sorted
##     in the order given.

mask7 = ncaa[ncaa['Round']==1]
#mask to only include the first round
mask7['highw'] = ''
#create empty column for higher seed win
mask7['matchup'] = mask7['Seed'].apply(str) +'-'+ mask7['Seed.1'].apply(str)
#create column for each seed matchup
for i in range(len(mask7)): #loop for each row
    if ((mask7.iloc[i,4]<mask7.iloc[i,9] and mask7.iloc[i,5]>mask7.iloc[i,8]) or
        #if team is better seed and has higher score, or
        (mask7.iloc[i,9]<mask7.iloc[i,4] and mask7.iloc[i,8]>mask7.iloc[i,5])):
        #team.1 is better seed and has higher score
        mask7.iloc[i,10] = 1 #set high win column as 1
    else: #else
        mask7.iloc[i,10] = 0 #set high win column as zero
mask7['highw'].groupby(mask7['matchup']).sum()/mask7['matchup'].value_counts()*100
#find amount of better seed wins, grouped by matchup
#divide by total games per matchup, multiply by 100 for percent

'''
#7
1-16    99.285714
2-15    94.285714
3-14    85.000000
4-13    79.285714
5-12    64.285714
6-11    62.857143
7-10    60.714286
8-9     48.571429
dtype: float64
#percentage of wins by the higher seed for each seed matchup
'''

## 8.  For each champion, determine the average margin of victory in all
##     games played by that team.  Make a table to the top-10 in terms of
##     average margin, sorted from highest to lowest.  Include all that tie
##     for 10th position if necessary.

df8 = ncaa
#create df for this problem
df8['Win'] = np.where(df8['Score']>df8['Score.1'],df8['Team'],df8['Team.1'])
#create column with winning team
df8['mov'] = abs(df8['Score']-df8['Score.1'])
#create column for margin of victory
champs8 = df8[df8['Round']==6][['Year','Win']]
#mask to only include championship round and winners from each year, save as df
df8c = champs8.merge(df8, on = ['Year','Win'])
#merge champs to df to get each champs game
df8c['mov'].groupby([df8c['Year'],df8c['Win']]).mean().nlargest(10)
#take mean of margin of victory for each champ and year, find 10 largest

'''
#8
Year  Win           
1996  Kentucky          21.500000
2016  Villanova         20.666667
2009  North Carolina    20.166667
1990  UNLV              18.666667
2018  Villanova         17.666667
2001  Duke              16.666667
2013  Louisville        16.166667
2006  Florida           16.000000
1993  North Carolina    15.666667
2015  Duke              15.500000
Name: mov, dtype: float64
#average margin of victory in all games played by each champion
'''

## 9.  For each champion, determine the average seed of all opponents of that
##     team.  Make a table of top-10 in terms of average seed, sorted from 
##     highest to lowest.  Include all that tie for 10th position if necessary.
##     Then make a table of the bottom-10, sorted from lowest to highest.
##     Again include all that tie for 10th position if necessary. 

df9 = ncaa
#create df for this problem
df9['Win'] = np.where(df9['Score']>df9['Score.1'],df9['Team'],df9['Team.1'])
#create column with winning team
df9['ls'] = np.where(df9['Score']>df9['Score.1'],df9['Seed.1'],df9['Seed'])
#create column for losing team's seed for each game
champs9 = df9[df9['Round']==6][['Year','Win']]
#mask to only include championship round and winners from each year, save as df
df9c = champs9.merge(df9, on = ['Year','Win'])
#merge champs to df to get each champs game
group9 = df9c['ls'].groupby([df9c['Year'],df9c['Win']]).mean()
#take mean of losing seed for each champ and year
group9.nlargest(11)
#find 10 highest avg seeds faced (weakest team)
group9.nsmallest(11)
#find 10 lowest avg seeds faced (weakest team)

'''
#9
Year  Win           
1990  UNLV              9.000000
2013  Louisville        8.500000
2008  Kansas            8.000000
2019  Virginia          8.000000
2006  Florida           7.666667
1986  Louisville        7.500000
1999  Connecticut       7.500000
1994  Arkansas          7.333333
2000  Michigan St       7.166667
1987  Indiana           7.000000
2005  North Carolina    7.000000
Name: ls, dtype: float64
#top-10 highest in terms of average seed, 11 shown due to tie 

Year  Win           
1985  Villanova         3.333333
2014  Connecticut       4.666667
2016  Villanova         4.833333
1993  North Carolina    5.500000
2003  Syracuse          5.666667
2017  North Carolina    5.666667
2009  North Carolina    5.833333
1989  Michigan          6.000000
1996  Kentucky          6.000000
2002  Maryland          6.000000
2007  Florida           6.000000
Name: ls, dtype: float64
#top-10 lowest in terms of average seed, 11 shown due to tie 
'''

## 10. Determine the 2019 champion.

mask10 = ncaa[(ncaa['Year']==2019)&(ncaa['Round']==6)]
#mask to only include this year's championship
np.where(mask10['Score']>mask10['Score.1'],mask10['Team'],mask10['Team.1'])
#print winner

'''
#10
array(['Virginia'], dtype=object)
#the 2019 champion
'''