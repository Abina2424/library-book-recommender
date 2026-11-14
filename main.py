
from recommender.book_recommender import BookRecommender

def main():

    recommender = BookRecommender("data/books.csv")

    print("Recommendations for genre='Fantasy':")
    print(recommender.recommend(genre='Fantasy'))

if __name__ == "__main__":
    main()
