from pyspark import SparkConf, SparkContext

def f(x):
    for a in x:
        yield a[1][1], (a[0], a[1][0])
        
def matrix_multiplication(A_txt, v_txt):
    """
    Calculate A*v
    :param A_txt: A txt file including matrix, with index
    :param v_txt: A txt file including vector, without index
    :return: An RDD object of A*v
    """
    A = sc.textFile(A_txt).map(lambda l: [float(x) for x in l.split(",")])
    v = sc.textFile(v_txt).map(lambda l: [float(x) for x in l.split(",")])
 
    A = A.map(lambda l: [(l[0], (l[i], i-1)) for i in range(1, len(l))])
    A = A.flatMap(lambda l: f(l))
    
    v = v.map(lambda l: [(l[0], (l[i], i)) for i in range(len(l))])
    v = v.flatMap(lambda l: [(i, l[i]) for i in range(len(l))])
    
    Av = A.join(v)
    Av = Av.map(lambda l: (l[1][0][0], l[1][0][1] * l[1][1][1][0]))

    Av = Av.reduceByKey(lambda x, y: x + y)
    print(Av.collect())
    return(Av)
