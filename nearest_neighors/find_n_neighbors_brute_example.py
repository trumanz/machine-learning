

from sklearn.neighbors import NearestNeighbors
import numpy as np
samples = np.array([[0, 0], [1, 1], [2, 2], [3.5, 3.5], [3.7, 3.7]])
samples = np.array([[0, 500], [10000, 0], [10001, 1000]])
samples = np.array([[500,0], [ 0,10000], [ 1000,10001]])
#training
nbrs = NearestNeighbors(n_neighbors=3, algorithm="kd_tree", leaf_size=1).fit(samples)
#find the K
points = np.array([[0,0,],[4,4]])
points = np.array([[5000,1000]])
points = np.array([[1000,5000]])
distances,indices = nbrs.kneighbors(points)
print("distances")
print(distances)
print("indices")
print(indices)

#[4,4] nearest 2 neighbors is [4,4],[3.5,3.5]
#distacne to [3.5,3.5] is sqrt( ((4-3.5)^2) + ((4-3.5)^2)）
#

for i in range(points.shape[0]):
    p = points[i]
    info = str(p) + "=>nearest n_neighbors "
    for j in range(len(indices[i])):
        info += str(samples[indices[i][j]])
        info += "distance=" + str(distances[i][j]) + "; "
    print(info)
