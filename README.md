# aws-cloud-resume-challenge

Repository containing all the source code, personal notes, diagrams related to the Cloud Resume Challenge. The Cloud Resume Challenge is an initiative to demonstrate proficiency in AWS cloud services and build a professional cloud-based resume. I've created this project to highlight my experience in working with various AWS services and implementing best practices for cloud-based applications.

## Technologies Used

- AWS Services:
  - Amazon S3: Hosting the static website content.
  - Amazon CloudFront: Content Delivery Network for improved performance and security.
  - AWS Lambda: Backend serverless functions for dynamic content written in python.
  - Amazon DynamoDB: NoSQL database for storage of the visitor counter.
  - AWS API Gateway: Exposing Lambda functions through RESTful APIs.
  - AWS IAM: Identity and Access Management for secure access control.
  - AWS Certificate Manager: Provisioning SSL/TLS certificates for secure connections.
- Frontend:
  - HTML, CSS, JavaScript: Building the frontend user interface.
- Version Control:
  - Git: Tracking changes
- Deployment:
  - GitHub Actions: Automating the deployment process.


## Application architecture

![System architecture diagram of how this project is deployed in AWS.](/docs/images/architecture-diagram.png)

## Application Details

# S3 Configurtation

This solution contains an S3 bucket that hosts my static website. The website is only accessible through the CloudFront distribution, not directly from S3. This was accomplished with an Origin Access Control restricting access to only CloudFront.

# CloudFront Configuration

A CloudFront distribution was created to serve my website to users. My distribution was configured with Origin Access Control and an ![S3 Bucket Policy](/docs/s3-bucket-policy.json) restricting access to only CloudFront.

# AWS Certificate Manager Configuration

An SSL/TLS certificate was created in ACM and attached to the CloudFront distribution.  This enables CloudFront to serve its content using HTTPS.

# AWS API Gateway Configuration

A RESTful API gateway was created enabling JavaScript from the website to trigger to a Lambda function serving the visitor counter.

# AWS Lambda Configuration

An AWS Lambda function was written in Python to retrieve the current visitor count from DynamoDB, increment it by one, return the new value to the website, and write the new value back to DynamoDB. This allows the visitor counter to increment each time someone visits my website. An IAM role was created and assigned to my Lambda function allowing access to DynamoDB for this purpose

# Amazon DynamoDB Configuration

Amazon DynamoDB was configured with a single table containing a record representing the number of visitors to my website. This is updated by the Lambda function each time it is triggered.

# AWS IAM Configuration

AWS Identity and Access Management was used to create IAM roles allowing my Lambda function to access DynamoDB, as well as creating a programmatic access user with roles allowing updating of my infrastructure and content. This allows me to utilize GitHub Actions to create a CI/CD pipeline for automated updating of my infrastructure and website content. You can view my GitHub Action ![here](/docs/cicd.yaml).


## Deployment pipeline

This project is built using GitHub Actions, which syncs the website to S3 and performs a CloudFront invalidation when a change is pushed to the main branch.