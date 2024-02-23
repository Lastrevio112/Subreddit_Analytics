import functions as fun
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime

#Reading the data:
subreddit = input("Please enter a subreddit to analyze (that was already scraped): ")
df = fun.read_data(subreddit)

#Data cleaning:
df = fun.convertColumnsOf_DF_to_Int(df, ['Karma', 'Number_of_comments'])

newHours = []
for hour in df['Hour']:
    newHours.append(int(hour[:2].strip(":")))
df['Hour'] = pd.Series(newHours)

#Aggregating the data:
df_Hour = df.groupby("Hour")[['Karma', 'Number_of_comments']].mean()
print(df_Hour)

#Plotting the data
BAR_WIDTH = 0.3
NR_OF_HOURS_IN_A_DAY = 24

x = np.arange(NR_OF_HOURS_IN_A_DAY) #Creating an array with numbers from 0 to 23
plt.bar(x - BAR_WIDTH/2, df_Hour['Karma'], width = BAR_WIDTH,  label = "Karma", color="r")
plt.bar(x + BAR_WIDTH/2, df_Hour['Number_of_comments'], width = BAR_WIDTH,  label = "No. of comments", color="b")

plt.ylabel("Engagement") #Setting label on y axis
plt.xticks(x, x) #Setting label on x axis
plt.title("Average karma and number of comments of a post on r/" + subreddit + " on each hour of the day.")
plt.legend()
plt.show()