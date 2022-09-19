# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:15:50 2022

source1: https://towardsdatascience.com/your-first-apache-spark-ml-model-d2bb82b599dd
source2: https://github.com/FavioVazquez/first_spark_model/blob/master/SparkTitanic.ipynb

"""

from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName('Titanic Data') \
    .getOrCreate()
    
df = (spark.read
          .format("csv")
          .option('header', 'true')
          .load("titanic.csv"))

# Cast numeric columns
from pyspark.sql.functions import col

dataset = df.select(col('Survived').cast('float'),
                         col('Pclass').cast('float'),
                         col('Sex'),
                         col('Age').cast('float'),
                         col('Fare').cast('float'),
                         col('Embarked')
                        )

# Drop missing values
dataset = dataset.replace('null', None)\
        .dropna(how='any')
        
# Index categorical columns with StringIndexer
from pyspark.ml.feature import StringIndexer
dataset = StringIndexer(
    inputCol='Sex', 
    outputCol='Gender', 
    handleInvalid='keep').fit(dataset).transform(dataset)
dataset = StringIndexer(
    inputCol='Embarked', 
    outputCol='Boarded', 
    handleInvalid='keep').fit(dataset).transform(dataset)

# Drop unnecessary columns
dataset = dataset.drop('Sex')
dataset = dataset.drop('Embarked')

# Assemble all the features with VectorAssembler

required_features = ['Pclass',
                    'Age',
                    'Fare',
                    'Gender',
                    'Boarded'
                   ]

from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(inputCols=required_features, outputCol='features')

transformed_data = assembler.transform(dataset)

# Split the data
(training_data, test_data) = transformed_data.randomSplit([0.8,0.2])

# Define the model
from pyspark.ml.classification import RandomForestClassifier

rf = RandomForestClassifier(labelCol='Survived', 
                            featuresCol='features',
                            maxDepth=5)

# Fit the model
model = rf.fit(training_data)

# Predict with the test dataset
predictions = model.transform(test_data)

# Evaluate our model
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(
    labelCol='Survived', 
    predictionCol='prediction', 
    metricName='accuracy')

# Accuracy
accuracy = evaluator.evaluate(predictions)
print('Test Accuracy = ', accuracy)