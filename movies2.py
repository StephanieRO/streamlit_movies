import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("movies.csv")

# Clean genre Column and split the genres.  Important step.
df['genres'] = df['genres'].str.split('|')
df_exploded = df.explode('genres') # Create a new row for each genre

# Streamlit app
st.title("Movie Genre Explorer")

# Genre selection
all_genres = df_exploded['genres'].unique()
selected_genre = st.selectbox("Select a Genre", all_genres)

# Filter movies by genre
genre_movies = df_exploded[df_exploded["genres"] == selected_genre]

# Display movies table
st.subheader(f"Movies in {selected_genre} Genre")
st.dataframe(genre_movies)

# Plot genre distribution
st.subheader("Distribution of Genres")
genre_counts = df_exploded['genres'].value_counts()  # Use the exploded DataFrame
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_counts.index, y=genre_counts.values)
plt.xticks(rotation=45, ha="right")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
st.pyplot(plt)
