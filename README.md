# AWS Data Engineering Pipeline: Lambda + Glue + S3

This project demonstrates a serverless data pipeline on AWS where: 

- A **CSV file uploaded to S3** triggers 
- An **AWS Lambda function**, which 
- **Starts an AWS Glue Job** to 
- **Transform the CSV** and write the output to another S3 folder. 

## 📁 Folder Structure 

  
``` 

s3-lambda-glue-etl/ 
├── lambda_function.py           # Lambda function code 
├── glue_job_script.py           # AWS Glue ETL script 
├── input_data/ 
│   └── sample.csv               # Sample raw CSV for testing 
├── README.md                    # Project documentation 
└── architecture.png             # Diagram of the pipeline 

```

---

## 🧪 AWS Services Used
- **AWS S3** – Storage for raw and processed data 
- **AWS Lambda (Python 3.12)** - Trigger on CSV upload, invoke Glue job
- **AWS Glue (PySpark)** - ETL transformation script
- **AWS CloudWatch** - Logging and monitoring 
- **IAM Roles & Policies** - Permissions for Lambda and Glue

---

## ✅ Summary of Steps

### 1. Created an S3 Bucket
Created a bucket with folders `incoming/` and `processed/` to simulate raw and processed data zones.

### 2. Uploaded Sample CSV
Uploaded a sample CSV file to the `incoming/` folder of the S3 bucket.

### 3. Created AWS Lambda Function
Set up a Lambda function triggered by S3 file uploads to the `incoming/` folder. The function parses the uploaded CSV file.

### 4. Configured Permissions
Attached the required IAM policies to allow the Lambda function to access S3 and write to CloudWatch Logs.

### 5. Verified Lambda Logs
Checked CloudWatch Logs to ensure the Lambda function correctly processed the file.

### 6. Created AWS Glue Job
Built a Glue job to read, transform, and write data using PySpark. Output is written to the `processed/` folder.

### 7. Triggered Glue from Lambda
Modified the Lambda function to start the Glue job after successful file parsing.

### 8. Wrote Transformed Data to S3
The Glue job writes cleaned/transformed data to the `processed/` folder without removing the original file from the `incoming/` folder.

## 📷 Architecture Diagram
