import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

def load_data(path="imdb_top_1000.csv"):
    try:
        df = pd.read_csv(path)
        df["combined_features"] = (
            df["Genre"].fillna("") + " " + df["Overview"].fillna("")
        )
        return df
    except FileNotFoundError:
        print(Fore.RED + "Dataset not found. Make sure imdb_top_1000.csv exists.")
        exit()

movies_df = load_data()

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies_df["combined_features"])
cosine_sim = cosine_similarity(tfidf_matrix)

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return polarity, "Positive"
    elif polarity < -0.1:
        return polarity, "Negative"
    return polarity, "Neutral"

def get_genres(df):
    genres = set()
    for g in df["Genre"].dropna():
        for item in g.split(","):
            genres.add(item.strip())
    return sorted(genres)

genres = get_genres(movies_df)

def recommend_random(genre=None, rating=None, n=5):
    df = movies_df.copy()

    if genre:
        df = df[df["Genre"].str.contains(genre, case=False, na=False)]
    if rating:
        df = df[df["IMDB_Rating"] >= rating]

    df = df.sample(min(n, len(df)))

    results = []
    for _, row in df.iterrows():
        polarity, sentiment = get_sentiment(row["Overview"])
        results.append({
            "Title": row["Series_Title"],
            "Genre": row["Genre"],
            "IMDB": row["IMDB_Rating"],
            "Sentiment": sentiment,
            "Polarity": polarity
        })
    return results

def recommend_ai(movie_title, n=5):
    if movie_title not in movies_df["Series_Title"].values:
        return None

    idx = movies_df[movies_df["Series_Title"] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]

    results = []
    for i, _ in sim_scores:
        row = movies_df.iloc[i]
        polarity, sentiment = get_sentiment(row["Overview"])
        results.append({
            "Title": row["Series_Title"],
            "Genre": row["Genre"],
            "IMDB": row["IMDB_Rating"],
            "Sentiment": sentiment,
            "Polarity": polarity
        })
    return results

def display_movies(movies):
    print(Fore.YELLOW + "\n🎬 Movie Recommendations:\n")
    for i, m in enumerate(movies, 1):
        print(Fore.CYAN + f"{i}. {m['Title']}")
        print(f"   Genre: {m['Genre']}")
        print(f"   IMDb Rating: {m['IMDB']}")
        print(f"   Sentiment: {m['Sentiment']} ({m['Polarity']:.2f})\n")

def main():
    print(Fore.BLUE + "🎥 Movie Recommendation System\n")

    print("1. AI-Based Recommendation")
    print("2. Random Recommendation")
    choice = input("\nChoose an option (1/2): ").strip()

    print("\nAvailable Genres:")
    for i, g in enumerate(genres, 1):
        print(f"{i}. {g}")

    genre_choice = input("\nEnter genre name or 'skip': ").strip()
    genre = None if genre_choice.lower() == "skip" else genre_choice

    rating_input = input("Minimum IMDb rating or 'skip': ").strip()
    rating = None if rating_input.lower() == "skip" else float(rating_input)

    if choice == "1":
        movie_title = input("\nEnter a movie you like: ").strip()
        results = recommend_ai(movie_title)
        if results:
            display_movies(results)
        else:
            print(Fore.RED + "Movie not found in dataset.")

    elif choice == "2":
        results = recommend_random(genre, rating)
        display_movies(results)

    else:
        print(Fore.RED + "Invalid choice.")

if __name__ == "__main__":
    main()
