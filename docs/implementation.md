# Implementation

The solution implements a high-availability infrastructure for a Flask web application using CloudFormation templates (VPC, ALB, ASG, ECS, CI/CD, CloudWatch). The templates were uploaded to an S3 bucket, and the main stack (`main.yaml`) was created through the AWS Console; nested stacks and resources were created automatically. The CI/CD pipeline creates Docker images, pushes them to ECR, and triggers deployments in ECS.

Screenshots (images in `docs/images/`).