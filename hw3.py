## Name: Logan King
## File: assignment03.py (STAT 3250)
## Topic: Assignment 3
##
import numpy as np
import pandas as pd
##  The questions in this assignment refer to the data in the
##  file 'absent.csv'.  The data contains 740 records from an
##  employer, with 21 columns of data for each record.  (There
##  are a few missing values indicated by zeros where zeros 
##  are clearly not appropriate.)  The file 'absent.pdf' has
##  a summary of the meanings for the variables.

##  Questions 1 and 2 can be completed without loops.  You should
##  try to do them this way, grading will take this into account.

## 1.  All questions refer to the data set 'absent.csv'.
absent = pd.read_csv('C:/Users/Student/Downloads/absent.csv') #read absent csv
## 1(a) Find the mean absent time among all records.
np.mean(absent)['Absenteeism time in hours'] #take mean of column in dataframe
'''
#1a
6.924324324324324 mean absent time
'''
## 1(b) Determine the number of records corresponding to
##      being absent on a Thursday.
day_group = absent['Day of the week'].groupby(absent['Day of the week']) 
#group the column by itself (unique values)
day_group.count().loc[5]
#take count of Thursdays
'''
#1b
125 number of records corresponding to being absent on a friday
'''
## 1(c) Find the number of different employees represented in 
##      this data.
absent['ID'].nunique() #find number of unique employee ID's

'''
#1c
36 number of different employees
'''

## 1(d) Find the transportation expense for the employee with
##      ID = 34.
transexp_group = absent['Transportation expense'].groupby(absent['ID']) 
#group transportation expense by ID
transexp_group.mean().loc[34]
#take mean of index 34, this works assuming transportation expense is a total 
#value for the employee (since it is the same for each absence)
'''
#1d
118 transportation expense
'''
## 1(e) Find the mean number of hours absent for the records
##      for employee ID = 11.
abshrs_group = absent['Absenteeism time in hours'].groupby(absent['ID'])
#group absent hours by ID
abshrs_group.mean().loc[11]
#take mean of hours for employee 11
'''
#1e
11.25 mean hours absent
'''
## 1(f) Find the mean number of hours absent for the records of those who 
##      have no pets, then do the same for those who have more than one pet.
abshrspets_group = absent['Absenteeism time in hours'].groupby(absent['Pet'])
#group absent hours by number of pets
nopets = abshrspets_group.mean().loc[0]
#take mean hours absent of owners of no pets
morethanone_pets = np.sum(abshrspets_group.sum().loc[2:8])/np.sum(abshrspets_group.count().loc[2:8])
#take mean absent hours of owners of more than one pet 
#(note actually divide sum of hours by sum of counts so it isn;t taking mean 
#of means for each owner)
nopets #print no pets
morethanone_pets #print more than one pet

'''
#1f
6.828260869565217 no pets
5.21830985915493 more than one pet
'''
## 1(g) Find the percentage of smokers among the records for absences that
##      exceeded 8 hours, then do the same for absences of no more then 4 hours.
hrs_group = absent['Absenteeism time in hours'].groupby(absent['Absenteeism time in hours'])
#group by absent hours
smokers_group = absent['Social smoker'].groupby(absent['Absenteeism time in hours'])
#group smokers by absent hours
eight_plus = np.sum(smokers_group.sum().loc[16:120])/np.sum(hrs_group.count().loc[16:120]) * 100
#take sum of sum of smokers for each hour represented over 8, divided by total over 8, 
#multply by 100 to get percent, save value
four_less = np.sum(smokers_group.sum().loc[0:4])/np.sum(hrs_group.count().loc[0:4]) * 100
#take sum of sum of smokers for each hour represented up to 4 divided by total under 4 hours,
#multply by 100 to get percent, save value
eight_plus
#print 8
four_less
#print 4
'''
#1g
6.349206349206349 exceed 8 hours
6.29067245119306 nor more than four hours
'''
## 1(h) Repeat 1(g), this time for social drinkers in place of smokers.
hrs_group = absent['Absenteeism time in hours'].groupby(absent['Absenteeism time in hours'])
#group by absent hours
drinkers_group = absent['Social drinker'].groupby(absent['Absenteeism time in hours'])
#group drinkers by absent hours
eight_plus = np.sum(drinkers_group.sum().loc[16:120])/np.sum(hrs_group.count().loc[16:120]) * 100
#take sum of sum of drinkers for each hour represented over 8, divided by total over 8 hours,
#multply by 100 to get percent, save value
four_less = np.sum(drinkers_group.sum().loc[0:4])/np.sum(hrs_group.count().loc[0:4]) * 100
#take sum of sum of drinkers for each hour represented up to 4 divided by total under 4 hours,
#multply by 100 to get percent, save value
eight_plus
#print 8
four_less
#print 4
'''
#1h
73.01587301587301 exceed 8 hours
53.36225596529284 no more than four hours
'''
## 2.  All questions refer to the data set 'absent.csv'.

## 2(a) Find the top-5 employee IDs in terms of total hours absent.  List
##      the IDs and corresponding total hours absent.
mosthrs_group = absent['Absenteeism time in hours'].groupby(absent['ID'])
#group absent hours by ID
mosthrs_group.sum().sort_values(ascending=False)[0:5,]
#take sum of hours for each ID, sort greatest to least, display top 5
'''
#2a
ID
3     482
14    476
11    450
28    347
34    344
Name: Absenteeism time in hours, dtype: int64
top 5 employee id's in terms of total hours absent
'''
## 2(b) Find the average hours absent per record for each day of the week.
##      Print out the day number and average.
dayhrs_group = absent['Absenteeism time in hours'].groupby(absent['Day of the week'])
#group absent hours by day of the week
dayhrs_group.mean()
#take mean hours for each day
'''
#2b
Day of the week
2    9.248447
3    7.980519
4    7.147436
5    4.424000
6    5.125000
Name: Absenteeism time in hours, dtype: float64
avg hours absent for each day of the week
'''
## 2(c) Repeat 2(b) replacing day of the week with month.
monthhrs_group = absent['Absenteeism time in hours'].groupby(absent['Month of absence'])
#group absent hours by month of the year
monthhrs_group.mean().drop([0,])
#take mean hours for each month, delete month 0
'''
#2c
Month of absence
1      4.440000
2      4.083333
3      8.793103
4      9.094340
5      6.250000
6      7.611111
7     10.955224
8      5.333333
9      5.509434
10     4.915493
11     7.507937
12     8.448980
Name: Absenteeism time in hours, dtype: float64
repeat 2b with month
'''
## 2(d) Find the top 3 most common reasons for absence for the social smokers,  
##      then do the same for the non-smokers. (If there is a tie for 3rd place,
##      include all that tied for that position.)
smokers = absent.loc[absent['Social smoker'] == 1]
#find every occurrence of social smokers, save as new df
abssmoke_group = smokers['Reason for absence'].groupby(smokers['Reason for absence'])
#group by reason for absence for smokers
smoker_reasons = abssmoke_group.count().sort_values(ascending=False).drop([0,]).nlargest(6)
#take count of each smokers reasons, sort descending,drop reason 0, and find 3 largest values
#enter 6 since 4 is repeated five times

nonsmokers = absent.loc[absent['Social smoker'] == 0]
#find every occurrence of nonsmokers, save as new df
absnonsmoke_group = nonsmokers['Reason for absence'].groupby(nonsmokers['Reason for absence'])
#group by reason of absence for nonsmokers
nonsmoker_reasons = absnonsmoke_group.count().sort_values(ascending=False).nlargest(3)
#take count of each nonsmokers reasons, sort descending, and find 3 largest values
#enter 3 since three highest values not repeated

smoker_reasons
#print top smoker reasons
nonsmoker_reasons
#print top nonsmoker reasons

'''
#2d
Reason for absence
25    7
19    4
18    4
28    4
22    4
23    4
Name: Reason for absence, dtype: int64
top smoker reasons

Reason for absence
23    145
28    108
27     69
Name: Reason for absence, dtype: int64
top nonsmoker reasons
'''

## 2(e) Suppose that we consider our data set as a sample from a much
##      larger population.  Find a 95% confidence interval for the 
##      proportion of the records that are from social drinkers.  Use
##      the formula 
##
##  [phat - 1.96*sqrt(phat*(1-phat)/n), phat + 1.96*sqrt(phat*(1-phat)/n)]
##
## where "phat" is the sample proportion and "n" is the sample size.
ctdrink_group = absent['Social drinker'].groupby(absent['Social drinker'])
#group by social drinker
n = np.sum(ctdrink_group.count())
#n is total count of drinkers and nondrinkers
phat = ctdrink_group.count().loc[1]/n
#phat is count of drinkers divided by total count
ci_low = phat - 1.96*np.sqrt(phat*(1-phat)/n)
#plug variables into formula for lower bound of ci
ci_high = phat + 1.96*np.sqrt(phat*(1-phat)/n)
#plug variables into formula for upper bound of ci
ci = [ci_low*100, ci_high*100]
#save ci
ci
#print ci
'''
#2e
[53.187250676078314, 60.326262837435195]
confidence interval
'''
## 3.  For this problem we return to simulations one more time.  Our
##     topic is "bias" of estimators, more specifically the "percentage
##     relative bias" (PRB) which we take to be
##
##        100*((mean of estimated values) - (exact value))/(exact value)
##
##     For instance, to approximate the bias of the sample mean in 
##     estimating the population mean, we would computer
##
##        100*((mean of sample means) - (population mean))/(population mean)
##
##     For estimators that are "unbiased" we expect that the average
##     value of all the estimates will be close to the value of the
##     quantity being estimated.  In these problems we will approximate
##     the degree of bias (or lack of) by simulating.  In all parts we
##     will be sampling from a population of 10,000,000 values randomly
##     generated from an exponential distribution with scale = 10 using
##     the code below.

pop = np.random.exponential(scale = 10, size = 10000000)

## 3(a) Compute and report the mean for all of "pop".  Simulate 100,000
##      samples of size 10, compute the sample mean for each of the samples,
##      compute the mean of the sample means, and then compute the PRB.
pop_mean = np.mean(pop) #take mean of pop
samp_means = np.zeros(100000) #initialize list of 100000 zeros
for i in range(100000): #run loop 100000 times
    samp = np.random.choice(pop, size=10) #take sample of size 10
    samp_means[i] = np.mean(samp) #take mean of sample and save as ith place
m_o_m = np.mean(samp_means) #take mean of sample means
PRB = 100*(m_o_m - pop_mean)/pop_mean #run prb formula
PRB #print prb
'''
#3a
-0.05005772360641138 PRB
'''
## 3(b) Compute and report the variance for all of "pop" using "np.var(pop)".  
##      Simulate 100,000 samples of size 10, then compute the sample variance 
##      for each sample using "np.var(samp)" (where "samp" = sample).  Compute 
##      the mean of the sample variances, and then compute the PRB.
##      Note: Here we are using the population variance formula on the samples
##      in order to estimate the population variance.  This should produce
##      bias, so expect something nonzero for the PRB.
pop_var = np.var(pop) #take var of pop
samp_var = np.zeros(100000)#initialize list of 100000 zeros
for i in range(100000): #run loop 100000 times
    samp = np.random.choice(pop, size=10)#take sample of size 10
    samp_var[i] = np.var(samp)#take var of sample and save as ith place
m_o_v = np.mean(samp_var)#take mean of sample vars
PRB = 100*(m_o_v - pop_var)/pop_var#run prb formula
PRB#print prb
'''
#3b
-10.31991312541339 PRB
'''
## 3(c) Repeat 3(b), but this time use "np.var(samp, ddof=1)" to compute the
##      sample variances.  (Don't change "np.var(pop)" when computing the
##      population variance.)
pop_var = np.var(pop)#take var of pop
samp_var = np.zeros(100000)#initialize list of 100000 zeros
for i in range(100000): #run loop 100000 times
    samp = np.random.choice(pop, size=10)#take sample of size 10
    samp_var[i] = np.var(samp, ddof=1)#take var of sample (ddof=1) and save as ith place
m_o_v = np.mean(samp_var)#take mean of sample vars
PRB = 100*(m_o_v - pop_var)/pop_var#run prb formula
PRB#print prb
'''
#3c
-0.3991900656137779 repeat 3b with changes
'''
## 3(d) Compute and report the median for all of "pop".  Simulate 100,000
##      samples of size 10, compute the sample median for each of the samples,
##      compute the mean of the sample medians, and then compute the PRB.
##      Note: For nonsymmetric distributions (such as the exponential) the
##      sample median is a biased estimator for the population median.  The
##      bias gets decreases with larger samples, but should be evident with 
##      samples of size 10.
pop_med = np.median(pop)#take median of pop
samp_meds = np.zeros(100000)#initialize list of 100000 zeros
for i in range(100000): #run loop 100000 times
    samp = np.random.choice(pop, size=10)#take sample of size 10
    samp_meds[i] = np.median(samp)#take median of sample and save as ith place
m_o_m = np.mean(samp_meds)#take mean of sample medians
PRB = 100*(m_o_m - pop_med)/pop_med#run prb formula
PRB#print prb
'''
#3d
7.442917121787653 PRB
'''