#!/usr/bin/env python
from sklearn import tree
#import numpy as np

if __name__ == '__main__':
    X = [[0, 0], [1, 1]]
    Y = [0, 1]
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)
    x = clf.predict([[2., 2.]])
    print(x)
