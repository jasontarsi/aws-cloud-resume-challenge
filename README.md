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

![System architecture diagram of how this project is deployed in AWS.](/docs/architecture_diagram.png)


## Deployment pipeline

This project is built using GitHub Actions, which syncs the website to S3 when a change is pushed to the main branch.