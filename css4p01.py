# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('C:/Users/mamel/project 1 css2024/movie_dataset.csv')
df_cleaned = df.dropna()
print(df)

# Question 1
highest_rated_movie = df.loc[df['Rating'].idxmax(), 'Title']
print("Highest rated movie:", highest_rated_movie)

# Question 2
average_revenue_all = df['Revenue (Millions)'].mean()
print("Average revenue of all movies:", average_revenue_all)

# Question 3
average_revenue_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]['Revenue (Millions)'].mean()
print("Average revenue of movies from 2015 to 2017:", average_revenue_2015_2017)

# Question 4
movies_2016 = df[df['Year'] == 2016].shape[0]
print("Number of movies released in 2016:", movies_2016)

# Question 5
movies_nolan = df[df['Director'] == 'Christopher Nolan'].shape[0]
print("Number of movies directed by Christopher Nolan:", movies_nolan)

# Question 6 
movies_high_rating = df[df['Rating'] >= 8.0].shape[0]
print("Number of movies with a rating of at least 8.0:", movies_high_rating)

# Question 7
median_rating_nolan = df[df['Director'] == 'Christopher Nolan']['Rating'].median()
print("Median rating of movies directed by Christopher Nolan:", median_rating_nolan)

# Question 8
highest_avg_rating_year = df.groupby('Year')['Rating'].mean().idxmax()
print("Year with the highest average rating:", highest_avg_rating_year)

# Question 9 
highest_avg_rating_year = df.groupby('Year')['Rating'].mean().idxmax()
print("Year with the highest average rating:", highest_avg_rating_year)

# Question 9 
movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print("Percentage increase in number of movies made between 2006 and 2016:", percentage_increase)

# Question 10
most_common_actor = df['Actors'].str.split(',').explode().str.strip().mode()[0]
print("Most common actor in all movies:", most_common_actor)

# Question 11
unique_genres = df['Genre'].str.split(',').explode().str.strip().nunique()
print("Number of unique genres in the dataset:", unique_genres)

# Question 12
correlation_matrix = df.corr()
print("Correlation matrix of numerical features:\n", correlation_matrix)

print("\nInsights:")

print("1. Positive correlation between X1 and X2 indicates...")

print("2. Negative correlation between X3 and X4 implies...")

print("3. Strong correlation between X5 and X6 suggests...")

print("4. Weak correlation between X7 and X8 indicates...")

print("\nAdvice for directors:")

print("- Focus on aspects with strong positive correlation for better movie success.")

print("- Pay attention to areas with negative correlation to avoid potential issues.")

print("- Consider factors with weak correlation to strike a balance in movie production.")

print("- Continuously analyze correlations to adapt to changing audience preferences.")
 
