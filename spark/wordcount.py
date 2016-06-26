#wordcount.py

from pyspark import SparkContext, SparkConf

conf=SparkConf().setAppName("wordcount")
sc=SparkContext(conf=conf)

# Creating RDD from wordcount.txt file
wcRDD=sc.textFile('/user/cloudera/wordcount.txt')

# Flatout the data in the file
# Eg : line "hi how are you"
# Converts to
# hi
# how
# are
# you

wcFlatRDD=wcRDD.flatMap(lambda x : x.split(" "))

# Next adding 1 in from of every word

wcMapRDD=wcFlatRDD.map(lambda x : (x,1))

# Now we have key value pair as
# (hi,1)
# (how,1)
# (are,1)
# (you,1)
# We will apply to reduceByKey to get counts now

wcCntRDD=wcMapRDD.reduceByKey(lambda x,y : x+y)

print (wcCntRDD.collect()) 
