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
├── incoming/ 
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
Created a bucket `data-ingestion-ayshan ` with folders `incoming/` and `processed/` to simulate raw and processed data zones.

<img width="1482" height="363" alt="image" src="https://github.com/user-attachments/assets/70fd7c8f-7a18-424d-a715-5cdcc42c6eb4" />


### 2. Created AWS Lambda Function
Set up a Lambda function `processCSVFile` triggered by S3 file uploads to the `incoming/` folder. The function parses the uploaded CSV file.

### 3. Configured Permissions
Attached the required IAM policies to allow the Lambda function to access S3 and write to CloudWatch Logs.

<img width="1198" height="322" alt="image" src="https://github.com/user-attachments/assets/59d3c306-6897-469a-a976-2b7cfc9f2084" />


### 4. Verified Lambda Logs
Checked CloudWatch Logs to ensure the Lambda function correctly processed the file.

<img width="1204" height="171" alt="image" src="https://github.com/user-attachments/assets/fa93b40d-1216-4cde-91ea-e157342c2e10" />


### 5. Created AWS Glue Job
Built a Glue job to read, transform, and write data using PySpark. Output is written to the `processed/` folder.

### 6. Triggered Glue from Lambda
Modified the Lambda function to start the Glue job after successful file parsing.

### 7. Wrote Transformed Data to S3
The Glue job writes cleaned/transformed data to the `processed/` folder without removing the original file from the `incoming/` folder.

<img width="1492" height="405" alt="image" src="https://github.com/user-attachments/assets/d8b02de6-26a4-41c2-859f-22afbcbcdc29" />


## 📷 Architecture Diagram
