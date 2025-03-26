import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("movies.csv")

# Clean genre Column
# df['genre'] = df['genre'].str.split(',').str[0]
df['genre'] = df['genre'].str.split(',')

# Clean gender column
df['gender'] = df['gender'].str.capitalize()  # Standardize capitalization

# Streamlit app
st.title("Movie Gender Explorer")

# Gender selection
genders = df["gender"].unique()
selected_gender = st.selectbox("Select a Gender", genders)

# Filter movies by gender
gender_movies = df[df["gender"] == selected_gender]

# Display movies table
st.subheader(f"Movies with {selected_gender} Main Character(s)")
st.dataframe(gender_movies)

# Plot movie ratings
st.subheader(f"Ratings of Movies with {selected_gender} Main Character(s)")
plt.figure(figsize=(10, 6))
sns.barplot(x="title", y="rating", data=gender_movies)
plt.xticks(rotation=90)
st.pyplot(plt)

# Plot release year vs rating
st.subheader(f"Release Year vs Rating of Movies with {selected_gender} Main Character(s)")
plt.figure(figsize=(10, 6))
sns.scatterplot(x="release_year", y="rating", data=gender_movies)
st.pyplot(plt)

# Plot genre distribution
st.subheader(f"Genre Distribution of Movies with {selected_gender} Main Character(s)")
genre_counts = gender_movies['genre'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_counts.index, y=genre_counts.values)
plt.xticks(rotation=45, ha="right")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
st.pyplot(plt)
