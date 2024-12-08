import pickle
import pandas as pd
from flask import Flask, render_template, request
from surprise import SVD
from surprise import Reader, Dataset

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained SVD model (collaborative filtering model)
with open('model/svd_model.pkl', 'rb') as file:
    svd_model = pickle.load(file)

# Load the content similarity matrix (optional if you use content-based filtering)
with open('model/content_similarity.pkl', 'rb') as file:
    content_similarity = pickle.load(file)

# Load movie data (small dataset)
movies = pd.read_csv('ml-dataset-small/movies.csv')

def get_recommendations(user_id, genres, movie_type):
    """
    Generate movie recommendations based on user input.
    - user_id: The ID of the user for collaborative filtering
    - genres: List of genres the user is interested in
    - movie_type: Type of movie the user enjoys most
    """
    # Filter movies by genres
    filtered_movies = movies[movies['genres'].str.contains('|'.join(genres), case=False, na=False)]

    # Use content-based recommendations to get similar movies based on genres
    recommendations = []
    for _, row in filtered_movies.iterrows():
        movie_id = row['movieId']  # Ensure this matches the column name in your dataset
        
        # Predict ratings using the collaborative filtering model (SVD)
        predicted_rating = svd_model.predict(str(user_id), str(movie_id)).est  # Use string IDs if needed
        recommendations.append((row['title'], predicted_rating))

    # Sort recommendations based on predicted rating
    recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)
    return [rec[0] for rec in recommendations[:10]]  # Return top 10 recommendations

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        genres = request.form.getlist('genres')  # This returns a list of selected genres
        movie_type = request.form['movie_type']  # This returns the selected movie type

        # Set a user_id for the example, you can use a dynamic ID based on the user
        user_id = 1  # Adjust as needed

        # Call get_recommendations function with the user inputs
        recommendations = get_recommendations(user_id, genres, movie_type)

        return render_template('index.html', recommendations=recommendations)

    return render_template('index.html', recommendations=[])

if __name__ == '__main__':
    app.run(debug=True)
