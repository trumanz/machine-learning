
import datetime
from sklearn.neighbors import NearestNeighbors
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import sys

def getSampleDate():
    point_num = 50*1000
    dimension = 20
    step = 1
    return np.arange(0,point_num*dimension*step,step).reshape(point_num,dimension)
def getData():
    point_num = 2*1000
    dimension = 20
    step = 2
    return np.arange(0, point_num * dimension * step, step).reshape(point_num, dimension)


def testBrute(algorithm, samples, points):
    result = {}
    print('<<<Start Test ' + algorithm)
    #1. fit date
    pre_time = datetime.datetime.now();
    nbrs = NearestNeighbors(n_neighbors=2, algorithm=algorithm).fit(samples)
    result["fitDur"] = datetime.datetime.now() - pre_time
    print("Fit sample data time" + str(result["fitDur"]))
    #2. find
    pre_time = datetime.datetime.now();
    distances,indices = nbrs.kneighbors(points)
    result["firstFindDur"] = datetime.datetime.now() - pre_time
    print("First find time" + str(result["firstFindDur"]))
    #2. find again
    pre_time = datetime.datetime.now();
    distances,indices = nbrs.kneighbors(points)
    result["secondFindDur"] = datetime.datetime.now() - pre_time
    print("Second find Time" + str(result["secondFindDur"]))
    #print("distances:\n" + str(distances) + "\n===")
    #print("indices:\n" + str(indices) + "\n===")

    for i in range(points.shape[0]):
        p = points[i]
        info = str(p) + "=>nearest n_neighbors"
        for j in range(len(indices[i])):
            info +=  str(samples[indices[i][j]])
            info += "distance=" + str(distances[i][j]) + "; "
        #print(info)
    #plt.scatter(samples[:,0],samples[:,1])
    #plt.show()
    return result

if __name__ == '__main__':
    samples = getSampleDate()
    points = getData()
    result = []
    for algorithm in ["brute", 'kd_tree', "ball_tree"] :
        r = testBrute(algorithm, samples, points)
        r['algorithm'] = algorithm
        result.append(r)
    print(result)
    df = pd.DataFrame(result)
    print(df)


















