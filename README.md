# Decentralized Movie Recommendation System

## Overview
This project implements a decentralized movie recommendation system that addresses privacy concerns, scalability issues, and fairness in content suggestions. By leveraging distributed computing principles and content-based recommendation algorithms, we aim to provide personalized movie recommendations while preserving user privacy and data security.

## Features
- Privacy-focused: User preferences processed locally
- Scalable architecture using distributed computing principles
- Fault-tolerant design
- Offline functionality
- Content-based recommendation algorithm
- Ethical considerations and FAIR principles implementation

## System Architecture
Our system comprises three main components, each running in separate Docker containers:
1. Scraping Server: Continuously scrapes new movie data from IMDb
2. Recommendation Server: Processes user queries and generates recommendations
3. Rebuild Server: Periodically rebuilds the recommendation model with new data

## Methodology
### Data Collection and Processing
- Custom web scraper using Python's BeautifulSoup library
- Dataset: 25,000 movies from IMDb
- Data preprocessing: text cleaning, categorical data conversion, numerical data handling, feature engineering

### Recommendation Algorithm
1. Text Vectorization using sklearn's CountVectorizer
2. Similarity Calculation using cosine similarity
3. Recommendation Generation based on highest similarity scores

### Decentralization Implementation
- Local data storage on each node
- Independent recommendation generation
- Periodic updates propagated to all nodes
- Peer-to-peer discovery mechanism using UDP broadcasts

## Results
### System Performance
- Near-linear scalability (see Table 1 in the paper)
- Fault tolerance: 5% increase in response time with 20% node failure

### Recommendation Quality
- Precision: 0.82
- Recall: 0.75
- NDCG: 0.79
- User study: 85% of users rated recommendations as "good" or "excellent"

### Data Analysis
- Genre distribution analysis
- Cast member popularity
- User rating distribution
- Temporal analysis of movies and ratings

## Conclusions
Our Decentralized Movie Recommendation System demonstrates:
1. Effective privacy preservation
2. Excellent scalability
3. Robust fault tolerance
4. Unique offline functionality
5. High-quality recommendations
6. Alignment with ethical data practices

## Installation and Usage
(Include steps for setting up and running the system, including any dependencies)

## Contributing
We welcome contributions to improve the recommendation algorithm, expand the movie database, or enhance the user interface. Please feel free to submit pull requests or open issues for bugs and feature requests.


## Authors
- Sakib Rokoni - 23273004
- Utsho Dey - 24366019
- Niloy Sarkar - 21201638

## Acknowledgments
We thank our advisor, Annajiat Alim Rasel, for guidance throughout this project.
