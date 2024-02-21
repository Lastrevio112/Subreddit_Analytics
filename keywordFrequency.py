import functions as fun

subreddit = "zizek"
df = fun.read_data(subreddit)

dict_frequencies = {}

for title in df['Post_title']:
    for word in title.split():
        if word.lower() in dict_frequencies:
            dict_frequencies[word.lower()] += 1
        else:
            dict_frequencies[word.lower()] = 1

for word in sorted(dict_frequencies, key=dict_frequencies.get, reverse=True):
    print(word, dict_frequencies[word])