from pyspark.sql import *
from datetime import date,datetime

if __name__ == "__main__":
    spark = SparkSession.builder\
            .appName("CreatingDataFrameDemo")\
            .getOrCreate()

# Use range() function to create dataframe
    df1 = spark.range(5)
    df1.printSchema()
    df1.show()

# Use createDataFrame() to create dataframe. First create a list with required data and datatypes.
    data_list = [(1,2., date(2022,1,1),datetime(2022,1,1,12,0)),
                (2,3., date(2022,1,2),datetime(2022,1,2,12,0)),
                (3,4., date(2022,1,3),datetime(2022,1,3,12,0))]

    df2 = spark.createDataFrame(data_list)
    df2.printSchema()
    df2.show()

#How to replace the column names. To_df is transformation function.
    df3 = spark.createDataFrame(data_list).toDF("a","b","c","d")
    df3.printSchema()
    df3.show()

# How to enforce the schema on the dataframe. There are two ways.
# Define the schema with column names and let it infer the datatype based on the data.
    schema1 = ['a','b','c','d']
    spark.createDataFrame(data_list,schema1).printSchema()

#Deine the schema with column names and data type. This will not infer data types, instead enforce. See exlicitly defined firstr column as int
    schema2 = 'a int,b double,c date,d timestamp'
    spark.createDataFrame(data_list,schema2).printSchema()

