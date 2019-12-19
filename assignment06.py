## Name: Logan King
## File: assignment06.py (STAT 3250)
## Topic: Assignment 6
##

##  This assignment requires the data file 'movies.txt'.  This file
##  contains records for nearly 4000 movies, including a movie ID number, 
##  the title (with year of release, which is not part of the title), and a 
##  list of movie genre classifications (such as Romance, Comedy, etc). 
import numpy as np # load numpy as np
import pandas as pd # load pandas as pd
movies = pd.read_csv('C:/Users/Student/Downloads/movies.txt',sep='::',
                     header=None,names=['id','title','genre'])
##  Note: All questions on this assignment should be done without the explicit
##        use of loops in order to be eliglble for full credit.  

## 1.  Are there any repeated movies in the data set?  A movie is repeated 
##     if the title is exactly repeated and the year is the same.  List any 
##     movies that are repeated, along with the number of times repeated.

group1 = movies['title'].groupby(movies['title']).count() 
#group by title and display count
np.sum(group1>1)
#find how many are duplicates

'''
#1
0 no movies repeated
'''

## 2.  Determine the number of movies included in genre "Action", the number
##     in genre "Comedy", and the number in both "Children's" and "Animation".

len(movies[movies['genre'].str.contains('Action')])
#find if genre string contains Action, then find how many strings do
len(movies[movies['genre'].str.contains('Comedy')])
#find if genre string contains Comedy, then find how many strings do
len(movies[movies['genre'].str.contains("Children's")&movies['genre'].str.contains('Animation')])
#find if genre string contains Children's and Animation, then find how many strings do

'''
#2
503 movies included in genre Action
1200 movies included in genre Comedy
84 movies included in genre Children's and Animation
'''

## 3.  Among the movies in the genre "Horror", what percentage have the word
##     "massacre" in the title?  What percentage have 'Texas'? (Upper or lower
##     cases are allowed here.) 

mask3 = movies[movies['genre'].str.contains('Horror')]
#mask to only include horror movies
np.sum(mask3.title.str.lower().str.contains('massacre'))/len(mask3)*100
#make all titles lowercase and find how many contain massacre, display as percentage of mask3
np.sum(mask3.title.str.lower().str.contains('texas'))/len(mask3)*100
#make all titles lowercase and find how many contain texas, display as percentage of mask3

'''
#3
2.623906705539359 percentage of horror movies that contain massacre in title
1.1661807580174928 percentage that contain texas in the title
'''

## 4.  How many titles are exactly one word?

sum(movies['title'].str[:-6].str.split().apply(len)==1)
#remove year from movies, split each string on white space, find length of each,
#find number of titles with only one word

'''
#4
690 number of titles with exactly one word
'''

## 5.  Among the movies with exactly one genre, determine the top-3 genres in
##     terms of number of movies with that genre.
mask5 = movies[(movies['genre'].str.split('|').apply(len)==1)==True]
#mask to only include movies with one genre
mask5['genre'].groupby(mask5['genre']).count().sort_values(ascending=False).nlargest(3)
#group mask5 by genre, sort descending, display top 3 values

'''
#5
genre
Drama     843
Comedy    521
Horror    178
Name: genre, dtype: int64
Among movies with exactly one genre, top 3 genres in terms of number of movies with that genre
'''
## 6.  Determine the number of movies with 0 genres, with 1 genre, with 2 genres,
##     and so on.  List your results in a table, with the first column the number
##     of genres and the second column the number of movies with that many genres.
mask6 = movies['genre'].str.split('|').apply(len)
#create object with count of genres for each movie
df6 = pd.DataFrame(mask6)
#convert object to dataframe
df6['genre'].groupby(df6['genre']).count()
#group dataframe by genre, take count of each genre

'''
#6
genre
1    2025
2    1322
3     421
4     100
5      14
6       1
Name: genre, dtype: int64
table listing number of genres and number of movies with that many genres
'''

## 7.  How many remakes are in the data?  A movie is a remake if the title is
##     exactly the same but the year is different. (Count one per remake.  For
##     instance, 'Hamlet' appears 5 times in the data set -- count this as one
##     remake.)

df7 = pd.DataFrame(movies['title'].str[:-6])
#remove year from movie titles and convert to dataframe (df7)
np.sum(df7['title'].groupby(df7['title']).count()>1)
#group by title and take count, find how many titles appear more than once

'''
#7
38
Number of remakes in the data
'''

## 8.  List the top-5 most common genres in terms of percentage of movies in
##     the data set.  Give the genre and percentage, from highest to lowest.

list8 = list(movies['genre'].str.split('|'))
#split genre strings, coerce into a list of lists
df8 = pd.DataFrame([y for x in list8 for y in x])
#make the list of lists into one big list and convert into a dataframe
(df8[0].groupby(df8[0]).count()/len(movies)*100).sort_values(ascending=False).nlargest(5)
#group dataframe by genre, take count of each genre, 
#find percentage of genres in terms of all movies, sort descending, display top 5

'''
#8
0
Drama       41.282514
Comedy      30.903940
Action      12.953902
Thriller    12.670616
Romance     12.129797
Name: 0, dtype: float64
top 5 most common genres in terms of percentage of movies in the dataset
'''

## 9.  Besides 'and', 'the', 'of', and 'a', what are the 5 most common words  
##     in the titles of movies classified as 'Romance'? (Upper and lower cases
##     should be considered the same.)  Give the number of titles that include
##     each of the words.
import string 
#necessary to remve punctuation
mask9 = movies[movies['genre'].str.contains('Romance')]
#mask to only include romance movies
list9 = list((mask9['title'].str[:-6].str.lower()).str.split())
#remove year, make all lowercase, split string on white space, coerce to list of lists
series9 = pd.Series([y for x in list9 for y in x])
#make list of lists into a big list and coerce to a series
df9 = pd.DataFrame(series9.str.translate(str.maketrans(' ',' ',string.punctuation)))
#remove punctuation from series and convert to dataframe
drop9 = ['and','the','of','a']
#we will be fropping these words
df9[0].value_counts().drop(drop9).head(5) 
#take count of each word, and drop the soecified words, display top 5

'''
#10
in      27
love    25
to      14
you     13
on      10
Name: 0, dtype: int64
top 5 most common words other than those removed
number of titles that include each of wods
'''

## 10. It is thought that musicals have become less popular over time.  We 
##     judge that assertion here as follows: Compute the mean release years 
##     for all movies that have genre "Musical", and then do the same for all
##     the other movies.  Then repeat using the median in place of mean.
musical10 = movies[movies['genre'].str.contains('Musical')]
#mask to only include musicals
musical10['title'].str[-5:-1].astype(int).mean()
#only display year for movies, convert to int, take mean
musical10['title'].str[-5:-1].astype(int).median()
#only display year for movies, convert to int, take median
other10 = movies[movies['genre'].str.contains('Musical')==False]
#mask to exclude musicals
other10['title'].str[-5:-1].astype(int).mean()
#only display year for movies, convert to int, take mean
other10['title'].str[-5:-1].astype(int).median()
#only display year for movies, convert to int, take median

'''
#10
1968.7456140350878 mean year of Musicals
1986.5908729105863 mean year of other genres

1967.0 median year of musicals
1994.0 median year of other genres
'''