import logging
import numpy as np
import pandas as pd
from scipy import stats as scs
from importlib import reload
import pyspark as ps
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
spark = SparkSession.builder.getOrCreate()

class MovieRecommender():
    """Template class for a Movie Recommender system."""

    def __init__(self):
        """Constructs a MovieRecommender"""
        self.logger = logging.getLogger('reco-cs')
        # ...


    def fit(self, ratings):
        """
        Trains the recommender on a given set of ratings.

        Parameters
        ----------
        ratings : pandas dataframe, shape = (n_ratings, 4)
                  with columns 'user', 'movie', 'rating', 'timestamp'

        Returns
        -------
        self : object
            Returns self.
        """
        self.logger.debug("starting fit")

        ratings['thumbs'] = (ratings['rating'] > 4).astype(int)
        spark_df = spark.createDataFrame(ratings) 
        
        ratings_df = spark_df.drop('timestamp')

        als_model = ALS(
            itemCol='movie',
            userCol='user',
            ratingCol='thumbs',
            nonnegative=True,    
            regParam=0.1,
            rank=18)

        self.average_movie_ratings = ratings.groupby('movie').mean()['rating']

        self.recommender = als_model.fit(ratings_df)
        self.logger.debug("finishing fit")
        return(self)


    def transform(self, requests):
        """
        Predicts the ratings for a given set of requests.

        Parameters
        ----------
        requests : pandas dataframe, shape = (n_ratings, 2)
                  with columns 'user', 'movie'

        Returns
        -------
        dataframe : a pandas dataframe with columns 'user', 'movie', 'rating'
                    column 'rating' containing the predicted rating
        """
        self.logger.debug("starting predict")
        self.logger.debug("request count: {}".format(requests.shape[0]))

        #requests['rating'] = np.random.choice(range(1, 5), requests.shape[0])

        #Change requests pandas data frame to spark to run through spark ALS model
        request_results = spark.createDataFrame(requests) 
        
        #Transform requests with recommender model
        request_pred = self.recommender.transform(request_results)
        request_pred_df = request_pred.toPandas()
        
        requests['rating']=request_pred_df['prediction']
        requests['rating'].fillna(requests['rating'].mean(), inplace=True)
        # requests['rating'].fillna(self.average_movie_ratings[requests['movie']], inplace=True)
        # requests.rename(columns={'prediction': 'rating'})
        #Change spark df back to pandas df and return 
        self.logger.debug("finishing predict")
        return(requests)


if __name__ == "__main__":
    logger = logging.getLogger('reco-cs')
    logger.critical('you should use run.py instead')
