import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'SOURCE_PATH', 'DEST_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_path = args['SOURCE_PATH']  
dest_path = args['DEST_PATH']  

# Load CSV from incoming folder
df = spark.read.option("header", "true").csv(source_path)

# Simple Transformation Example: uppercase 'name' column
from pyspark.sql.functions import upper
df_transformed = df.withColumn("name", upper(df["name"]))

# Write transformed data to S3/processed/
df_transformed.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(dest_path)

print(f"Transformed data written to: {dest_path}")

job.commit()