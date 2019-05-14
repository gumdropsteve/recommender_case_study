# Movie Recommender Case Study

The Team's presentation slides can be found [here](https://docs.google.com/presentation/d/1qLeFmX4WpmIp0jjdLYf1quI9ddmVFXcTK2hRC8i4BQU/edit?usp=sharing)

### Intro 
Today you are going to have a little friendly competition with your classmates.

You are going to building a recommendation system based off data from the [MovieLens](https://grouplens.org/datasets/movielens/) dataset. It includes movie information, user information, and the users' ratings. Your goal is to build a recommendation system and to suggest movies to users!

The movies data and user data are in data/movies.dat and data/users.dat.

The ratings data can be found in data/training.csv. The users' ratings have been broken into a training and test set for you (to obtain the testing set, we have split the 20% of the most recent ratings).

### The Team's Matrix Decomposition Model
- Assume “latent features” in our movies and users
  - Use Alternating Least Squares (ALS) to predict latent features
    - Guess avg. rating per movie if confronted with new user
    - Thumbs Method
      - Converted ratings to binary system of approval and disapproval based on ratings above and below 4
    - Thumbs method takes user bias into account and it is intuitive
  - Pros
    - Identifies Hidden Connections Organically
    - Calculates all known user-movie combos
  - Areas for Improvement
    - Fits poorly on “sparse” data
    - Does not solve the “cold start” problem
- Reflection
  - What went well?
    - Good ideation
      - Feature Engineering
      - “Thumbs” method
      - EDA
    - The real 5-star rating is the friends you make along the way :)
  - Potential Future Work
    - Adjust predicted ratings based on
      - Average Movie Rating
      - User Genre Profile (cosine similarity)
      - Movie similarity to highly rated movies
    - Compare models
      - Adjust hyperparameters
      - Try linear regression



Movie Recommender Case Study (Galvanize g88 - Spring 2019)
