# Movie Recommender Case Study

### Intro 
Today you are going to have a little friendly competition with your classmates.

You are going to building a recommendation system based off data from the MovieLens dataset. It includes movie information, user information, and the users' ratings. Your goal is to build a recommendation system and to suggest movies to users!

The movies data and user data are in data/movies.dat and data/users.dat.

The ratings data can be found in data/training.csv. The users' ratings have been broken into a training and test set for you (to obtain the testing set, we have split the 20% of the most recent ratings).

### The Team's Matrix Decomposition Model
- Assume “latent features” in our movies and users
  - Use Alternating Least Squares (ALS) to predict latent features
    - Guess avg. rating per movie if confronted with new user
    - Thumbs Method - converted ratings to binary system of approval and disapproval based on ratings above and below 4
    - Thumbs method takes user bias into account and it is intuitive
  - Pros
    - Identifies Hidden Connections Organically
    - Calculates all known user-movie combos
  - Areas for Improvement
    - Fits poorly on “sparse” data
    - Does not solve the “cold start” problem


Movie Recommender Case Study (Galvanize g88 - Spring 2019)
