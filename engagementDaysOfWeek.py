import functions as fun
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#Reading the data:
subreddit = input("Please enter a subreddit to analyze (that was already scraped): ")
df = fun.read_data(subreddit)

#Data cleaning:
df = fun.convertColumnsOf_DF_to_Int(df, ['Karma', 'Number_of_comments'])

#Grouping the data:
DAYS_OF_WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

df_daysOfWeek = df.groupby("Day_of_week")[['Karma', 'Number_of_comments']].mean()
df_daysOfWeek = df_daysOfWeek.reindex(DAYS_OF_WEEK)
print(df_daysOfWeek)

#Plotting the data:
BAR_WIDTH = 0.3

x = np.arange(len(DAYS_OF_WEEK)) #Creating an array with numbers from 0 to 6
plt.bar(x - BAR_WIDTH/2, df_daysOfWeek['Karma'], width = BAR_WIDTH,  label = "Karma", color="r")
plt.bar(x + BAR_WIDTH/2, df_daysOfWeek['Number_of_comments'], width = BAR_WIDTH,  label = "No. of comments", color="b")

plt.ylabel("Engagement") #Setting label on y axis
plt.xticks(x, DAYS_OF_WEEK) #Setting label on x axis
plt.title("Average karma and number of comments of a post on r/" + subreddit + " on each day of the week.")
plt.legend()
plt.show()