import findspark
findspark.init("C:\\Work\\spark-3.2.1-bin-hadoop3.2\\")

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()

spark.conf.set("spark.sql.repl.eagerEval.enabled", True) # Property used to format output tables better

spark

# Load the csv into a dataframe
titanic_df = spark.read.csv("titanic.csv", header=True, inferSchema=True)

print(titanic_df.select('PassengerId', 'Survived').limit(5))

print(titanic_df.where((titanic_df.Age > 25) & (titanic_df.Survived == 1)).limit(5))

from pyspark.sql.types import IntegerType
from pyspark.sql.functions import udf

def round_float_down(x):
  return int(x)

round_float_down_udf = udf(round_float_down, IntegerType())

titanic_df.select('PassengerId', 'Fare', round_float_down_udf('Fare').alias('Fare Rounded Down')).limit(5)

titanic_df.createOrReplaceTempView("Titanic")
spark.sql('select * from Titanic')