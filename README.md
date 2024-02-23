# Subreddit_Analytics
A web scraper developed in Python that showcases analytics about subreddits from Reddit.

# HOW TO USE:

1. Run scraper.py and enter the name of a subreddit of choice. This script will create an Excel file with information about the last 500 posts of that subreddit (title of the post, karma, number of comments, day of the week it was posted, the hour it was posted and the timezone of that hour).

2. Run engagementDaysOfWeek.py and enter the name of a scraped subreddit. This will output a bar chart with the average karma and number of comments of a post for each day of the week.

3. Run engagementHourPosted.py and enter the name of a scraped subreddit. This will output a bar chart with the average karma and number of comments of a post for each hour of the day.

4. Run regression_analysis.py and enter the name of a scraped subreddit. This will output a scatter plot with a simple linear regression line where the independent (predictor) variable is the length of the title of a post and the dependent (predicted) variable is the karma of that post.

5. Run keywordFrequency.py and enter the name of a scraped subreddit. This will output all words found in the titles of all posts in the respective file ordered by the frequency in which they appear as well as the frequency itself.
