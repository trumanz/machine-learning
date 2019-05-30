import kdtree
if __name__  ==  '__main__':
    t = kdtree.create([[1, 1], [5, 4], [6, 1]])
    #t = kdtree.create([[500,0], [ 0,10000], [ 1000,10001]])
    kdtree.visualize(t)

    print(t.search_nn([4, 1]))
    #print(t.search_nn([ 1000,5000]))




