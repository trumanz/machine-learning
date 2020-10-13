import os
import csv
import sys
import math
import random
from tqdm import tqdm
import heapq

def get_samll_test_data():
    matrix = [
        #SF: science fiction
        #HI: history
        #SFa, SFb, HIc, HId  movie/ user
        [1,   1,   1,   1 ], #0
        [1,   1,   1,   0 ], #1
        [1,   0,   1,   0 ], #2
        [0,   1,   1,   1 ], #3
        [1,   1,   0,   0 ], #4
        #1 connected, 0 not connected
    ]
    #predict user 5
    train_records = []
    for user in range(len(matrix)):
        for movie in range(len(matrix[user])):
            if matrix[user][movie] == 1:
                train_records.append((user, movie))
    test_records = [(4,3)]
    return  train_records, test_records
def get_1m_data():
    record_set = set()
    x = []
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, "../../datasets-recsys/ml-1m/ratings.dat")
    path = os.path.realpath(path)
    print(path)
    records = []
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            d =line.split(',')
            r = (d[0], d[1])
            records.append(r)
    random.seed(1)
    random.shuffle(records)
    x = int(len(records)*0.8)
    train_records = records[0:x]
    test_records = records[x:]
    return (train_records, test_records)

def readUserMovieRecord():
    record_set = set()
    x = []
    with open(r"C:\Users\truma\git2\RecSys\data\ml-1m\ratings.dat", encoding='utf-8') as f:
      spamreader = csv.reader(f)
      next(spamreader)
      for row  in spamreader:
          #if len(row) != 4 or (row[3].find('2014') < 0 and row[3].find('2015') < 0):
          #    continue
          user  = int(row[0])
          movie = int(row[1])
          #if user >= 18:
          #    continue
          #if movie not in [49530]:
          #    continue
          record_set.add((user, movie))
          x.append((user,movie))
    return x
def tranform2UserView(record_set):
    user_movie_dict = {}
    for row  in record_set:
          user  = row[0]
          movie = row[1]
          if user not in user_movie_dict:
              user_movie_dict[user] = set()
          user_movie_dict[user].add(movie)
    return user_movie_dict
def tranform2MovieView(record_set):
    movie_user_dict = {}
    for row  in record_set:
          user  = row[0]
          movie = row[1]
          if movie not in movie_user_dict:
              movie_user_dict[movie] = set()
          movie_user_dict[movie].add(user)
    return movie_user_dict

