
import datetime
from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt

import sys

def getSampleDate():
    point_num = 50*1000
    dimension = 7
    step = 1
    return np.arange(0,point_num*dimension*step,step).reshape(point_num,dimension)
def getData():
    point_num = 20*1000
    dimension = 7
    step = 2
    return np.arange(0, point_num * dimension * step, step).reshape(point_num, dimension)


def testBrute(algorithm):
    print('<<<Start Test ' + algorithm)
    samples = getSampleDate()
    points = getData()
    pre_time = datetime.datetime.now();
    pre_time = datetime.datetime.now();
    nbrs = NearestNeighbors(n_neighbors=2, algorithm=algorithm).fit(samples)
    print("Fit sample data time" + str(datetime.datetime.now() - pre_time))
    distances,indices = nbrs.kneighbors(points)
    print("First find time" + str(datetime.datetime.now() - pre_time))
    pre_time = datetime.datetime.now();
    distances,indices = nbrs.kneighbors(points)
    print("Second find Time" + str(datetime.datetime.now() - pre_time))
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

if __name__ == '__main__':
    testBrute("brute")
    testBrute('kd_tree')
    testBrute("ball_tree")


















