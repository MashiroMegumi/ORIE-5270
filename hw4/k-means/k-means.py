import sys
import numpy as np
from pyspark import SparkContext

def pyspark_kmeans(data_file,seed_file, itera = 100):
    '''
    parameters:
    data_file: the data file containing the data points
    seed_file: the data file containing the initial centroid
    itera: the number of iterations we use
    '''
    
    data = sc.textFile(data_file).map(lambda l: np.array([float(x) for x in l.split(' ')]))
    cent = sc.textFile(seed_file).map(lambda l: np.array([float(x) for x in l.split(' ')])).collect()
    
    for i in range(itera):
        cluster = data.map(lambda l: (np.argmin([np.linalg.norm(l-c) for c in cent]),(l,1)))
        clustered_data = cluster.reduceByKey(lambda l_1,l_2: (l_1[0]+l_2[0],l_1[1]+l_2[1])).sortByKey()
        new_cent = clustered_data.map(lambda l: l[1][0]/l[1][1])
        cent = new_cent.collect()
    
    write_out(cent)
    sc.stop()

def write_out(txt):
    txt = open("result.txt","w")
    for i in cent:
        txt.write(str(i)+"\n")
    txt.close()
    
if __name__ == "__main__":
    pyspark_kmeans(sys.argv[1],sys.argv[2])
