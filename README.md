# Movie Recommender System

## Overview
This project is a **movie recommender system** that uses a hybrid approach to suggest movies based on user preferences. It leverages the MovieLens 32M dataset and combines collaborative filtering and content-based recommendation techniques. The system is built with Python and Flask, providing an interactive interface for users to explore movie recommendations.

## Features
- Hybrid recommendation combining collaborative filtering and content-based methods.
- Flask-based web application for user interaction.
- Efficient processing of large datasets (MovieLens 32M).

## Technologies Used
- **Python**: Core programming language.
- **Flask**: Web framework for the application.
- **Pandas, NumPy**: Data processing and analysis.
- **scikit-learn**: Machine learning implementation for recommendations.
- **MovieLens Dataset**: Data source for movies and user ratings.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd movie-recommender-system
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Access the app at `http://127.0.0.1:5000` in your browser.

## Future Improvements
- Implement user authentication for personalized recommendations.
- Deploy the application to a cloud platform (e.g., AWS, Heroku).
- Integrate real-time movie updates.
