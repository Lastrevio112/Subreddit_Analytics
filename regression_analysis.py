import functions as fun
import pandas as pd
import statsmodels.api as sm
from matplotlib import pyplot as plt
import numpy as np

#Reading data from excel file:
subreddit = "Romania" #this is the input that should be changed accordingly
df = fun.read_data(subreddit)

#Cleaning the data
df = fun.convertColumnsOf_DF_to_Int(df, ['Karma', 'Number_of_comments'])

#Storing the independent variable in a list
lengthsOfEachPost = list()
for title in df['Post_title']:
    lengthsOfEachPost.append(len(title))

# defining the variables
x = lengthsOfEachPost
y = df['Karma'].tolist()

# adding the constant term
x = sm.add_constant(x)

# performing the regression
# and fitting the model
result = sm.OLS(y, x).fit()

# printing the summary table
print(result.summary())

#Plotting the scatter plot and regression line
plt.plot(lengthsOfEachPost, df['Karma'].tolist(), 'o')
#obtain m (slope) and b(intercept) of linear regression line
m, b = np.polyfit(lengthsOfEachPost, df['Karma'].tolist(), 1)
#add linear regression line to scatterplot
plt.plot(x, m*x+b)
plt.xlabel("Length of title of post")
plt.ylabel("Karma of the post")
plt.show()