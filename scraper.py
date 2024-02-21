import pandas as pd
from bs4 import BeautifulSoup
import requests


subreddit = "AskReddit" #variable to be inputted later
URL = r"https://old.reddit.com/r/" + subreddit + '/new/'
firstPage = requests.get(URL, headers = {'User-agent': 'your bot 0.1'})
soup1 = BeautifulSoup(firstPage.text, 'html.parser')

first_20_pages = []
first_20_pages.append(soup1)

#scraping the first 20 pages starting from the newest post, will give 500 posts in total
for i in range(0, 19):
    next_page_link = list(first_20_pages[i].find("span", class_="next-button").children)[0]
    href = next_page_link.attrs['href']
    newPage = requests.get(str(href), headers = {'User-agent': 'your bot 0.1'})
    newSoup = BeautifulSoup(newPage.text, 'html.parser')
    first_20_pages.append(newSoup)

    print("Link to page " + str(i+1) + ": " + href)


#inputting each post into a dataframe
df = pd.DataFrame(data=None, columns=['Post_title', 'Karma', 'Number_of_comments', 'Day_of_week', 'Hour'])

i = 0
for page in first_20_pages:
    i += 1
    print("\n\n----------------------------------------" + "PAGE " + str(i) + " ----------------------------------------\n")
    for post in page.find_all('div', class_='thing'):
        title = post.find('a', class_="title").get_text()

        karma = post.find('div', class_="score unvoted").get_text()
        #in case karma is not shown on that subreddit, it will enter a dot
        if not karma.isnumeric():
            karma = 0

        nrOfComments = post.find('li', class_="first").get_text()[
                       : post.find('li', class_="first").get_text().find("c")]
        if nrOfComments == "":
            nrOfComments = '0'

        timePosted = post.find('time').attrs['title']
        dayPosted = timePosted[0:3].strip()
        hourPosted = timePosted[11:16].strip(":")

        new_df_row = {'Post_title': title,
                      'Karma': karma,
                      'Number_of_comments': nrOfComments,
                      'Day_of_week': dayPosted,
                      'Hour': hourPosted
                      }

        df = df._append(new_df_row, ignore_index=True)

        print("POST TITLE:", title)
        print("KARMA:", karma)
        print("DAY OF WEEK:", dayPosted)
        print("HOUR:", hourPosted)
        print("NUMBER OF COMMENTS:", nrOfComments)
        print()

#Outputting dataframe to Excel file
new_excel = subreddit + ".xlsx"
df.to_excel("ExcelFiles/" + new_excel)
print("Data written to Excel file successfuly.")


