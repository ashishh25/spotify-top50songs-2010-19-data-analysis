import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the csv file
df = pd.read_csv('top50MusicFrom2010-2019Spotify.csv')

# Display the dataframe
print(df.head(10))
print(df.describe())

# Get the mean, median, and standard deviation of the duration column
mean_length = df['Length'].mean()
median_length = df['Length'].median()
std_length = df['Length'].std()

# Print the basic statistics of the duration column
print('Basic statistics of the duration column:')
print(f'Mean: {mean_length:.2f} s')
print(f'Median: {median_length:.2f} s')
print(f'Standard deviation: {std_length:.2f} s')

# Get the number of songs by genre
genre_counts = df['Genre'].value_counts()

# Print the count of songs by genre
print('\nCount of songs by genre:')
print(genre_counts)

# Group the DataFrame by year and get the top 1 song by popularity for each year
df_top1 = df.groupby('Year').apply(lambda x: x.nlargest(1, 'Popularity')).reset_index(drop=True)

# Display the title of the top 1 song by popularity from each year
print('Title of the top 1 song by popularity from each year:')
print(df_top1[['Year', 'Title', 'Artist']])

# Get the count of songs by genre and select the top 10 genres
genre_counts = df['Genre'].value_counts().head(8)

# Plot a pie chart to show the percentage of top 10 genres
plt.pie(genre_counts.values, labels=genre_counts.index, autopct='%1.1f%%', colors=('#ffff00', '#ffd400', '#ffa51c', '#ff724a', '#ff3b6f', '#ff0094', '#e102b5', '#9932cc'))
plt.title('Percentage of Top 10 Genres')
plt.show()

artist_counts = df['Artist'].value_counts().head(4)

colors = ['#EB5353', '#F9D923', '#36AE7C', '#187498']

plt.bar(artist_counts.index, artist_counts.values, color=colors)
plt.title('Top Four Artists')
plt.xlabel('Artist Name')
plt.ylabel('No of Songs')
plt.show()

# Create a dataframe for the songs of 2018
df_2018 = df[df['Year'] == 2018]

# Create a dataframe for the songs of 2019
df_2019 = df[df['Year'] == 2019]

# Get the count of songs by genre for 2018 and 2019
genre_counts_2018 = df_2018['Genre'].value_counts().head(8)
genre_counts_2019 = df_2019['Genre'].value_counts().head(8)

# Plot a bar graph to compare the top genres of 2018 and 2019
fig, ax = plt.subplots()
ax.bar(genre_counts_2018.index, genre_counts_2018.values, label='2018', color='darkorchid')
ax.bar(genre_counts_2019.index, genre_counts_2019.values, label='2019', color='orange')
ax.set_xlabel('Genre')
ax.set_ylabel('Number of Songs')
ax.set_title('Top Genres Comparison: 2018 vs 2019')
ax.legend()
plt.show()

# Get the mean danceability score for 2018 and 2019
danceability_mean_2018 = df_2018['Danceability'].mean()
danceability_mean_2019 = df_2019['Danceability'].mean()

# Plot a horizontal bar graph to compare the mean danceability score of 2018 and 2019
fig, ax = plt.subplots()
ax.barh(['2018', '2019'], [danceability_mean_2018, danceability_mean_2019], color=('#36AE7C', '#187498'))
ax.set_xlabel('Mean Danceability Score')
ax.set_title('Mean Danceability Score Comparison: 2018 vs 2019')
plt.show()



