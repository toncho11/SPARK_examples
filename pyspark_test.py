import findspark
findspark.init("C:\\Work\\spark-3.2.1-bin-hadoop3.2\\")

import random

from pyspark import SparkContext
sc = SparkContext(appName="EstimatePi")

def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

NUM_SAMPLES = 1000000

rdd = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside)

print(rdd.take(5))
#print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
sc.stop()
print("Done.===============================================")