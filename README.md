# SPARK_examples
Provides samples and installation notes on how to use SPARK with empahasis on Python and Windows.

# Installing Spark:
* download Spark. The download file should be similar to spark-3.2.1-bin-hadoop3.2.tgz
* install Java 8
* dowload Hadoop. The download file should be similar to hadoop-3.3.1.tar.gz
* On Windows you need to download separately winutils.exe and put it in HADOOP_HOME\bin (otherwise it fails to start)
* Make a .bat file that sets both Spark and Hadoop home folders and paths. One is provided in this repository. You can use it as `call sethome.bat`.

# Initial repository set-up

Next you should create a new Python virtual environment and install PySpark.
A new Python environment guarantees that you will not have problem with package dependencies (Python dependency hell). The price for that is a lot of extra disk space used.

* $`git clone this repository`
* $`cd the repository` 
* $`python -m venv my_spark_env` (better use your full path to python.exe as windows has reserved python.exe and python3.exe as shorcuts to the Windows Store like this `C:\Work\python38\python.exe -m venv my_spark_env`)
* $`call .\my_spark_env\Scripts\activate` (activating your new virtual environment)
* $`where python.exe` (verfication: the first output line should point to python.exe in your newly created environment)
* (my_spark_env)$`pip install --upgrade pip`
* (my_spark_env)$`pip install pyspark findspark` (installs the Python bindings to Spark)

# Running from the console
Now you can test the provided python scripts for Core, SQL and ML. 

* got to your SPARK_examples folder
* `call .\my_spark_env\Scripts\activate`
* `call sethome.bat` (part of this repository, needs to be edited before calling it)
* `python pyspark_test.py` (alternatively you can use `%SPARK_HOME%\bin\spark-submit.cmd pyspark_test.py` to execute a Python script)

If nothing happens first check if you are really using python from your environment. See below for a common error [cannot access class sun.nio.ch.DirectBuffer](https://stackoverflow.com/questions/73465937/apache-spark-3-3-0-breaks-on-java-17-with-cannot-access-class-sun-nio-ch-direct).

# Usage notes
* In each script you need to modify the following line: `findspark.init("C:\\Work\\spark-3.2.1-bin-hadoop3.2\\")` to point to your Spark home folder.
* If you are using the Spyder IDE you must install it with pip in your pyspark virtual environment and run it from there. Also each time you might need to set manually the Python interpreter in Spyder to use the python.exe from your pyspark environment.
* Do not forget to call your `sethome.bat` file where you set up Spark and Hadoop home folders before testing the pyspark scripts. 

# Diagnostic
* Check if you are using `SPARK_HOME` or `SPARK-HOME`
* Check your Python's home folder: `python -c "import sys; print(sys.executable)"`
* Remove all your fake Python interpreters provided from Windows located in  `\AppData\Local\Microsoft\WindowsApps\`
* If Spark searches for "python3" then make a copy of "python.exe" called "python3.exe" in your "\Scripts" folder in your python environment.
* You can check you Spark version using: `%SPARK_HOME%\bin\spark-shell`
* There is a well known bug [cannot access class sun.nio.ch.DirectBuffer](https://stackoverflow.com/questions/73465937/apache-spark-3-3-0-breaks-on-java-17-with-cannot-access-class-sun-nio-ch-direct) that prevents Spark from starting on Java 17. More info [here](https://stackoverflow.com/questions/72724816/running-unit-tests-with-spark-3-3-0-on-java-17-fails-with-illegalaccesserror-cl). The soultion is to use the Java option `--add-exports java.base/sun.nio.ch=ALL-UNNAMED` as it is in this command: 

`
%SPARK_HOME%\bin\spark-submit.cmd --driver-java-options "--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.lang.invoke=ALL-UNNAMED --add-opens=java.base/java.lang.reflect=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.util.concurrent=ALL-UNNAMED --add-opens=java.base/java.util.concurrent.atomic=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/sun.nio.cs=ALL-UNNAMED --add-opens=java.base/sun.security.action=ALL-UNNAMED --add-opens=java.base/sun.util.calendar=ALL-UNNAMED" spark_ml_heart.py
`








