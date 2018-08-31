from pyspark import SparkConf, SparkContext
import sys

def f(x):
    '''
    the function to generate iter object
    '''
    for i in x:
        yield i[1][1], (i[0], i[1][0])

def write_out(sth):
    """
    the function to output a result text file with input sth
    """
    txt = open("result.txt","w")
    for i in sth:
        txt.write(str(i)+"\n")
    txt.close()

def matrix_multi(A.txt,v.txt):
    '''
    params:
    A.txt: the matrix file (index included)
    v.txt: the vector file (index included)
    '''
    A = sc.textFile('A.txt').map(lambda l: [float(x) for x in l.split(",")])
    v = sc.textFile('v.txt').map(lambda l: l.split(","))
    A = A.map(lambda l: [(l[0], (l[i], i)) for i in range(1, len(l))])
    A = A.flatMap(lambda l: f(l))

    v = v.map(lambda l: [(l[0], (l[i], i)) for i in range(1, len(l))])
    v = v.flatMap(lambda l: [(i, l[i]) for i in range(1, len(l))])
    
    joint = A.join(v)
    product = joint.map(lambda l: (l[1][0][0], l[1][0][1] * l[1][1]))
    A_v = product.reduceByKey(lambda l_1,l_2: l_1 + l_2)
    write_out(A_v.collect())
    sc.stop()

if __name__ == "__main__":
    matrix_multi(sys.argv[1],sys.argv[2])
