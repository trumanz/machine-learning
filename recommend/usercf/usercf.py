import csv
import sys
import math
import random
from tqdm import tqdm
import heapq
import logging
import pprint
from data import testdata

class MoviePref():
    def  __init__(self, movie, pref):
        self.movie = movie
        self.pref = pref
    def __lt__(self, oth) :
        return self.pref < oth.pref
    def __repr__(self):
        return "m:%d,p:%f"%(self.movie, self.pref)

class UserCF:
    def train(self, train_movie_user_dict):
        self.train_movie_user_dict = train_movie_user_dict
        print("calculating user similarity")
        self.weight_of_user_similarity = self.__cal_user_similarity(train_movie_user_dict)
        #logging.getLogger().debug("weight_of_user_similarity:\n"  + pprint.pformat(self.weight_of_user_similarity))

    def train_v2(self,data):
        self.train_movie_user_dict = testdata.tranform2MovieView(data)
        self.train(self.train_movie_user_dict)

    #calculator user similarity
    def __cal_user_similarity(self, movie_user_dict):
      from collections import defaultdict
      count_same_movie = defaultdict(defaultdict)  #C[i][j] represent same movie count of user i and j
      weight_of_similarity = defaultdict(defaultdict)
      user_movie_count = defaultdict()
      for movie,users in tqdm( movie_user_dict.items() ):
        #print("movie:" + str(movie))
        #print(users)
        for i in users:
            if i not in user_movie_count:
                user_movie_count[i] = 0.0
            user_movie_count[i]+= 1.0
            for j in users:
                if i >= j:
                    continue
                if j not in count_same_movie[i].keys():
                    count_same_movie[i][j] = 0.0
                if i not in count_same_movie[j].keys():
                    count_same_movie[j][i] = 0.0
                #count_same_movie[i][j] += 1.0
                weight = 1.0/( math.log( 1.0 + len(users)))  #punish hot movie
                count_same_movie[i][j] += weight
                count_same_movie[j][i] += weight

      #print(count_same_movie)
      #print(user_movie_count)

      for i, jcount in tqdm(count_same_movie.items() ):
        for j,count in jcount.items():
            if i >= j:
                continue
            denominator = math.sqrt ( user_movie_count[i] * user_movie_count[j] )
            #denominator = 1.0
            x = count / denominator
            count_same_movie[i][j] = x
            count_same_movie[j][i] = x

      return count_same_movie

    def recommend_multi_users(self,users, k, n):
        recommendataion = {}
        for user in users:
            recommendataion[user] = self.recommend(user, k, n)
        return recommendataion


    def recommend(self, user, k, n):
      first_n_movies = []
      #debug_movies = []
      if user not in self.weight_of_user_similarity:
          return first_n_movies
      us = self.weight_of_user_similarity[user]
      first_k_similar_user = [(u,w) for u, w in sorted(us.items(), key=lambda kv : kv[1], reverse=True)]
      first_k_similar_user = first_k_similar_user[0:k]
      #logging.getLogger().debug("recommend for user " + str(user) +", first_k_similiar_usr:\n" + pprint.pformat(first_k_similar_user))
      #print(first_k_similar_user)
      for movie in self.train_movie_user_dict:
        #print("movie:" + str(movie))
        pref = 0.0
        users_of_movie = self.train_movie_user_dict[movie]
        #print("users_of_movie:" + str(users_of_movie))
        #print("user:"+ str(user))
        if  user in users_of_movie:
             continue
        for  s_user, weight_of_similary in first_k_similar_user:
             if s_user in users_of_movie:
                 pref += weight_of_similary * 1.0
        mr = MoviePref(movie, pref)
        heapq.heappush(first_n_movies, mr)
        #debug_movies.append(mr)
        if len(first_n_movies) > n:
            heapq.heappop(first_n_movies)
      x = [ heapq.heappop(first_n_movies).movie for i in range(len(first_n_movies)) ]
      x.reverse()
      #logging.getLogger().debug("debug_movies:" + pprint.pformat(debug_movies))
      #logging.getLogger().debug("first_n_movies:" + pprint.pformat(first_n_movies))
      #logging.getLogger().debug("x:" + pprint.pformat(x))
      return x
