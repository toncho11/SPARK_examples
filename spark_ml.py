# source https://www.bmc.com/blogs/python-spark-machine-learning-classification/

import pandas as pd
from pyspark.sql.types import StructType, StructField, NumericType

import findspark
findspark.init("C:\\Work\\spark-3.2.1-bin-hadoop3.2\\")

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()

def isSick(x):
    if x in (3,7):
        return 0
    else:
        return 1

cols = ('age',       
'sex',         
'chest pain',           
'resting blood pressure',    
'serum cholesterol',       
'fasting blood sugar',         
'resting electrocardiographic results', 
'maximum heart rate achieved',  
'exercise induced angina',     
'ST depression induced by exercise relative to rest',  
'the slope of the peak exercise ST segment',     
'number of major vessels ',       
'thal',  
'last')

data = pd.read_csv('heart.csv', delimiter=' ', names=cols)
data = data.iloc[:,0:13] #remove last column

data['isSick'] = data['thal'].apply(isSick)

df = spark.createDataFrame(data) #create spark data frame from panda dataframe 

from pyspark.ml.feature import StandardScaler
from pyspark.ml.feature import VectorAssembler

features =   ('age',       
'sex',         
'chest pain',           
'resting blood pressure',    
'serum cholesterol',       
'fasting blood sugar',         
'resting electrocardiographic results', 
'maximum heart rate achieved',  
'exercise induced angina',     
'ST depression induced by exercise relative to rest',  
'the slope of the peak exercise ST segment',     
'number of major vessels ') 

# We use the VectorAasembler to put all twelve of those fields into a new column called features that contains all of these as an array.
assembler = VectorAssembler(inputCols=features,outputCol="features")
raw_data=assembler.transform(df) #new column "features" is added
raw_data.select("features","age").show(truncate=False)

# We use the Standard Scaler to put all the numbers on the same scale.
# This takes the observation and subtracts the mean, and then divides that by the standard deviation.
from pyspark.ml.feature import StandardScaler
standardscaler=StandardScaler().setInputCol("features").setOutputCol("Scaled_features")
raw_data=standardscaler.fit(raw_data).transform(raw_data)
raw_data.select("features","Scaled_features").show(5)

# We split the data into training and test datasets
from pyspark.ml.tuning import ParamGridBuilder, TrainValidationSplit
training, test = raw_data.randomSplit([0.5, 0.5], seed=12345)

# We create the logistic Regression Model and train it
from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression(labelCol="isSick", featuresCol="Scaled_features",maxIter=10)
model=lr.fit(training)
predict_train=model.transform(training)
predict_test=model.transform(test)
predict_test.select("isSick","prediction").show(10)

import pyspark.sql.functions as F
check = predict_test.withColumn('correct', F.when(F.col('isSick') == F.col('prediction'), 1).otherwise(0))

print("Accuracy on test data: ", check.agg(F.sum("correct")).collect()[0][0] / predict_test.select("*").count())