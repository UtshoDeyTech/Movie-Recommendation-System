# Movie Data Scraping Project

In this project, I used Python and the Beautiful Soup module to scrape data from IMDb.com for approximately 25,000 movies. The following information was collected for each movie:

- Movie title
- Total run time
- Movie rating
- User rating
- Genres
- Overview
- Movie's plot keywords
- Director name
- Top 5 cast's name
- Writer name
- Releasing year
- IMDb movie URL path

## Data Scraping Process

To scrape the data, I used Python's requests module to retrieve the HTML code for each movie page on IMDb.com. I then used Beautiful Soup to parse the HTML and extract the desired data.

## Data Cleaning and Formatting

After scraping the data, I cleaned and formatted it to ensure consistency and accuracy. For example, I removed any extraneous whitespace and converted data types as necessary.

## Movie Recommendation System

Using the scraped movie data, I built a small recommendation system using machine learning techniques. Specifically, I trained a model to identify the similarities between movies based on their genres, plot keywords, director, writer, and top cast members. The model was trained using a variety of techniques, including natural language processing and clustering algorithms.

To test the model, I built a small web app that takes a movie name from the dataset as input and returns the closest 5 movie recommendations. The app uses the trained model to find movies that are most similar to the input movie based on their features.

## Conclusion

Overall, this project demonstrates the power of web scraping, data analysis, and machine learning in building a movie recommendation system. The scraped movie data can be used for various purposes, such as analyzing trends in the movie industry, while the recommendation system can help users discover new movies based on their preferences.
