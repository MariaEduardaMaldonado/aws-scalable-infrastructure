# Implementation

The solution implements a highly available and scalable infrastructure for a Flask web application on AWS using CloudFormation nested stacks. The architecture includes VPC, Application Load Balancer (ALB), Auto Scaling Group (ASG), Amazon ECS, CI/CD pipeline, and CloudWatch monitoring resources.

The CloudFormation templates are stored in an S3 bucket and deployed through the main stack (`main.yaml`). Once the main stack is created, the nested stacks and associated resources are provisioned automatically.

The CI/CD pipeline builds Docker images, pushes them to Amazon ECR, and deploys new application versions to ECS services.

Implementation screenshots are available in `docs/images/`.