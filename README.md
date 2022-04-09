# SPARK_examples
Provides samples on how to use SPARK with empahasis on Python and Windows.

Next you need to install Spark
* download Spark. The download file should be similar to spark-3.2.1-bin-hadoop3.2.tgz
* install Java 8
* dowload Hadoop. The download file should be similar to hadoop-3.3.1.tar.gz
* On Windows you need to download separately winutils.exe and put it HADOOP_HOME\bin
* Make a .bat file that sets both Spark and Hadoop home folders and paths. One is provided in this repository. 

Next you should create a new Python environment and install PySpark.
A new Python environment gurantees that you will not have problem with package dependencies.

* $git clone this repository
* $cd the repository 
* $python -m venv my_spark_env (better use your full path to python.exe as windows has reserved python.exe and python3.exe as shorcuts to the Windows Store)
* $source ./my_spark_env/bin/activate (activating virtualenv, on windows use "call .\my_spark_env\Scripts\activate")
* (my_spark_env)$ pip install --upgrade pip
* (my_spark_env)$ pip install pyspark

Now you can test the provided python scripts for Core, SQL and ML.
If you are using Spyder IDE you should install it with pip in your pyspark environment and run it from there. Also each time you might need to set the Python interpreter in Spyder to use the one from your pyspark environment that you just created.




