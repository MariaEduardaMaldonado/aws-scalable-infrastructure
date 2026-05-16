# Scalable and Highly-Available Infrastructure on AWS

**Final Graduation Project (TCC)**  
Instituto Federal de Educação, Ciência e Tecnologia Fluminense — Campus Itaperuna  
Bachelor's Degree in Information Systems

Official repository for the Final Graduation Project (TCC) — implementation of a scalable and highly-available infrastructure on AWS. This repository contains a sample web application, infrastructure-as-code templates (CloudFormation), and CI/CD configuration to demonstrate an automated deployment pipeline using containers (ECR / ECS).

## Overview
The goal of this project is to design and implement an architecture that provides high availability and automatic scalability for a simple Flask web application. The solution uses AWS services such as VPC, Application Load Balancer (ALB), Auto Scaling (ASG), Elastic Container Registry (ECR), Elastic Container Service (ECS), and a CI/CD pipeline with CodeBuild / CodePipeline.

Architecture diagram: see `docs/arquitetura.png`.

## Technologies
- AWS CloudFormation (IaC)
- Amazon VPC
- Application Load Balancer (ALB)
- EC2 Auto Scaling / ECS
- Amazon ECR
- AWS CodeBuild / CodePipeline (CI/CD)
- Docker
- Flask (sample application)

## Repository layout

```
aws-scalable-infrastructure/
  README.md                           # Portuguese documentation
  README_EN.md                        # This file (English)
  app/                                # Flask app (source, Dockerfile, requirements)
    app.py
    Dockerfile
    requirements.txt
    static/
      style.css
  iac/
    buildspec/
      buildspec.yaml
    cloudformation/
      main.yaml
      vpc.yaml
      alb.yaml
      asg.yaml
      ecs.yaml
      cicd.yaml
      cloudwatch.yaml
  docs/
    arquitetura.png                   # Architecture diagram
    images/                           # Screenshots and implementation images
    implementation.md                 # Implementation details
```

## Run locally (development)
Requirements: Docker and Git.

1. Clone the repository and go to project folder:

```powershell
git clone <REPO_URL>
cd aws-scalable-infrastructure
```

2. Run the application locally with Docker:

```powershell
cd app
docker build -t flask-app .
docker run -p 8080:80 flask-app
# Open http://localhost:8080
```

3. Or run without container (EC2 metadata calls will be unavailable locally):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r app/requirements.txt
python app/app.py
# Open http://localhost:80
```

## Deploy on AWS (CloudFormation)
The CloudFormation templates are stored in `iac/cloudformation/`. In this project the templates were uploaded to an S3 bucket and `main.yaml` references nested templates by TemplateURL pointing to S3 objects.

Steps used to deploy via the AWS Console (the same approach used during the implementation):

1. Open the AWS Console and go to CloudFormation.
2. Click "Create stack" → "With new resources (standard)".
3. In "Upload template", upload the main.yaml template.  
4. Click "Next" and fill in "Stack name" (e.g., `FlaskApplication`) and required parameters (`ProjectName`, `GitHubv2ConnectionArn`, `ACMCertificateArn`, `EcsImage`, `EcsMinTasksNumber`, etc.).
5. Review, acknowledge IAM capabilities if requested (e.g., `CAPABILITY_IAM`), and click "Create stack". CloudFormation will create the main stack and the nested stacks referenced by `TemplateURL` automatically.

CLI equivalent (using the template URL):

```powershell
aws cloudformation create-stack --stack-name FlaskApplication --template-url https://s3.amazonaws.com/YOUR_BUCKET/main.yaml --capabilities CAPABILITY_IAM --parameters ParameterKey=ProjectName,ParameterValue=my-project
```

Notes:
- Monitor the stack "Events" tab to follow progress and troubleshoot errors.
- Check the "Outputs" tab to find exported resources (ALB DNS, ARNs, names, etc.).
- Confirm that dependent services were created: ECR repository, ECS cluster/service, AutoScalingGroup, ALB, CodeBuild/CodePipeline, etc.

Do not modify the templates if you want to reproduce the exact infrastructure used in the deliverable; instead provide the correct parameters and the S3 URL of the main template.

## CI/CD
The CI/CD pipeline is defined in `iac/buildspec/buildspec.yaml` and expects environment variables/parameters such as ECR repository name, ECS cluster, and GitHub connection (Codestar/GitHubv2 ARN). The pipeline builds the Docker image, pushes it to ECR, and forces a new deployment on ECS.

## Implementation Details
See [`docs/implementation.md`](docs/implementation.md) for a detailed description of the implementation steps, including screenshots and evidence of functionality.

## Author
Maria Eduarda Lopes Maldonado

## Supervisor
Prof. Francisco Alves de Freitas Neto, M.Sc.
