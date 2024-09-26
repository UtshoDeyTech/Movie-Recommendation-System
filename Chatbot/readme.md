# Decentralized Movie Recommendation System

## Overview
This project implements a decentralized movie recommendation system using Streamlit. It offers personalized movie recommendations based on user input, prioritizing privacy and offline accessibility.

## Features
- Privacy-focused: User preferences are processed locally
- Personalized recommendations based on movie selection
- Offline access once initial data is downloaded
- Simple and intuitive user interface
- Diverse content recommendations, avoiding filter bubbles

## Requirements
- Python 3.7+
- Streamlit
- Pandas
- Scikit-learn

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/decentralized-movie-recommender.git
   cd decentralized-movie-recommender
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have the following files in your project directory:
   - `chatbot.py`
   - `movies_dict.pkl`
   - `similarity.pkl`

## Usage
1. Run the Streamlit app:
   ```
   streamlit run chatbot.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Select a movie from the dropdown menu or type in a movie title.

4. Click "Show Recommendation" to get personalized movie suggestions.

## How It Works
- The system uses a pre-computed similarity matrix to find movies similar to the user's selection.
- Recommendations are generated based on cosine similarity between movies.
- All processing occurs locally, ensuring user privacy.

## Advantages Over Centralized Systems
1. **Privacy**: Viewing history and preferences remain on the user's device.
2. **Personalization**: Recommendations are tailored to individual tastes without global trend influence.
3. **Offline Access**: Recommendations available without an internet connection after initial data download.
4. **Diverse Content**: Avoids echo chambers created by centralized algorithms.
5. **User Control**: Full control over data and transparent recommendation process.

## Contributing
Contributions to improve the recommendation algorithm, expand the movie database, or enhance the user interface are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.


## Contact
Utsho Dey - utshodey.tech@gmail.com

