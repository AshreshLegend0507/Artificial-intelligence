import pandas as pd
from textblob import TextBlob
from colorama import Fore, Style, init

# Initialize colorama for colored text
init(autoreset=True)

# --- Step 1: Create a sample movie dataset ---
data = {
    "Title": ["Inception", "Titanic", "Avengers", "Interstellar", "Joker", "Frozen"],
    "Genre": ["Sci-Fi", "Romance", "Action", "Sci-Fi", "Drama", "Animation"],
    "Description": [
        "A mind-bending thriller about dream invasion.",
        "A love story set during the Titanic disaster.",
        "Superheroes team up to save the world.",
        "Exploration of space and time to save humanity.",
        "A dark story about society and mental health.",
        "A princess saves her kingdom with magical powers."
    ]
}

movies = pd.DataFrame(data)

# --- Step 2: Get user input ---
print(Fore.CYAN + " Welcome to the AI Movie Recommendation System!\n")

genre_input = input(Fore.YELLOW + "Enter a movie genre you like (e.g., Sci-Fi, Action, Drama): ").strip()
sentiment_input = input(Fore.YELLOW + "Describe the kind of movie you want (e.g., thrilling, romantic, funny): ").strip()

# --- Step 3: Sentiment Analysis ---
sentiment_score = TextBlob(sentiment_input).sentiment.polarity
if sentiment_score > 0:
    mood = "positive"
elif sentiment_score < 0:
    mood = "dark"
else:
    mood = "neutral"

print(Fore.GREEN + f"\nAnalyzing your mood... It seems you want a {mood} movie!\n")

# --- Step 4: Filter and Recommend ---
recommendations = movies[movies["Genre"].str.lower() == genre_input.lower()]

if not recommendations.empty:
    print(Fore.MAGENTA + f"Here are some {genre_input} movies for you:\n")
    for i, row in recommendations.iterrows():
        print(Fore.CYAN + f"- {row['Title']} ({row['Genre']}) → {row['Description']}")
else:
    print(Fore.RED + "Sorry, no movies found in that genre.")

print(Style.BRIGHT + Fore.GREEN + "\n Enjoy your movie time!")
