# SPARK_examples
Provides samples and installation notes on how to use SPARK with empahasis on Python and Windows.

# Installing Spark:
* download Spark. The download file should be similar to spark-3.2.1-bin-hadoop3.2.tgz
* install Java 8
* dowload Hadoop. The download file should be similar to hadoop-3.3.1.tar.gz
* On Windows you need to download separately winutils.exe and put it in HADOOP_HOME\bin (otherwise it fails to start)
* Make a .bat file that sets both Spark and Hadoop home folders and paths. One is provided in this repository. You can use it as "call sethome.bat".

# Initial repository set-up

Next you should create a new Python virtual environment and install PySpark.
A new Python environment guarantees that you will not have problem with package dependencies (Python dependency hell). The price for that is a lot of extra disk space used.

* $git clone this repository
* $cd the repository 
* $python -m venv my_spark_env (better use your full path to python.exe as windows has reserved python.exe and python3.exe as shorcuts to the Windows Store like this C:\Work\python38\python.exe -m venv my_spark_env)
* $call .\my_spark_env\Scripts\activate (activating your new virtualenv)
* $where python.exe (verfication: the first output line should point to python.exe in your newly created environment)
* (my_spark_env)$ pip install --upgrade pip
* (my_spark_env)$ pip install pyspark findspark

# Running from the console
Now you can test the provided python scripts for Core, SQL and ML.

* got to your SPARK_examples folder
* call .\my_spark_env\Scripts\activate
* sethome.bat (part of this repository)
* .\Scripts\python pyspark_test.py

Alternatively you can use SPARK-HOME\bin\spark-submit.cmd to execute a Python script.

# Usage notes
* In each script you need to modify the following line: findspark.init("C:\\Work\\spark-3.2.1-bin-hadoop3.2\\") to point to your Spark home folder.
* If you are using the Spyder IDE you must install it with pip in your pyspark virtual environment and run it from there. Also each time you might need to set manually the Python interpreter in Spyder to use the python.exe from your pyspark environment.
* Do not forget to call your sethome.bat file where you set up Spark and Hadoop home folders before testing the pyspark scripts. 








