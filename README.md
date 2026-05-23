# Infraestrutura Escalável e de Alta Disponibilidade na AWS

Trabalho de Conclusão de Curso (TCC)

Instituto Federal Fluminense (IFF) – Campus Itaperuna
Bacharelado em Sistemas de Informação

## Sobre o Projeto

Este repositório contém a implementação desenvolvida para o Trabalho de Conclusão de Curso sobre infraestrutura escalável e de alta disponibilidade na AWS.

A solução utiliza serviços da AWS para provisionar automaticamente uma arquitetura baseada em containers, com balanceamento de carga, escalabilidade automática, monitoramento e pipeline de integração e entrega contínua (CI/CD).

## Arquitetura

![Architecture](docs/arquitetura.png)

## Tecnologias

- AWS CloudFormation
- Amazon VPC
- Application Load Balancer (ALB)
- Amazon ECS
- Auto Scaling Groups
- Amazon ECR
- AWS CodeBuild
- AWS CodePipeline
- Amazon CloudWatch
- Docker
- Flask

## Funcionalidades

- Infraestrutura como Código (IaC) com CloudFormation
- Balanceamento de carga com Application Load Balancer
- Escalabilidade automática utilizando Auto Scaling
- Aplicação containerizada com Docker
- Armazenamento de imagens no Amazon ECR
- Orquestração com Amazon ECS
- Pipeline CI/CD automatizado
- Monitoramento com Amazon CloudWatch

## Estrutura do Repositório

```
aws-scalable-infrastructure/
  README.md                         # Documentação geral do projeto
  README_EN.md                      # English documentation
  app/                              # App Flask (código-fonte, Dockerfile, requirements)
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
    arquitetura.png                   # Diagrama de arquitetura
    images/                           # Screenshots e imagens da implementação
    implementation.md                 # Detalhes da implementação realizada
```

## Como executar localmente (desenvolvimento)
Pré-requisitos: Docker e Git.

1. Clone o repositório e entre na pasta do projeto:

```powershell
git clone <URL_DO_REPO>
cd aws-scalable-infrastructure
```

2. Executar a aplicação localmente com Docker:

```powershell
cd app
docker build -t flask-app .
docker run -p 8080:80 flask-app
# Acesse: http://localhost:8080
```

3. Ou executar sem container (requisições a metadata do EC2 falharão localmente):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r app/requirements.txt
python app/app.py
# Acesse: http://localhost:80
```

## Deploy na AWS (via CloudFormation)
Os templates de infraestrutura estão localizados em `iac/cloudformation/` e são organizados como nested stacks. O template principal (`main.yaml`) referencia os demais templates armazenados em um bucket Amazon S3 por meio da propriedade `TemplateURL`.

Na implementação apresentada neste projeto, os templates foram enviados para um bucket S3 e implantados por meio do template principal.

Descrição do procedimento usado (via Console):

1. No Console da AWS, abra o serviço CloudFormation.
2. Clique em "Create stack" → "With new resources (standard)".
3. Em "Upload template", carregue o template main.yaml.  
4. Clique em "Next" e, em "Specify stack details":
  - Stack name: por exemplo `FlaskApplication` (use o nome que você escolheu ao criar a stack).
  - Preencha os parâmetros necessários (ex.: `ProjectName`, `GitHubv2ConnectionArn`, `ACMCertificateArn`, `EcsImage`, `EcsMinTasksNumber`, etc.) conforme a necessidade da sua implantação.

5. Clique em "Next" até a tela de revisão. Marque as boxes de capabilities necessárias (por exemplo, `I acknowledge that AWS CloudFormation might create IAM resources`).
6. Clique em "Create stack". O CloudFormation criará a stack principal e, em seguida, os nested stacks referenciados por `TemplateURL` automaticamente.

Observações/checagens pós-criação:
- Verifique a aba "Events" da stack principal para acompanhar o progresso e identificar erros.
- Veja a aba "Outputs" para consultar recursos exportados (ALB DNS, nomes de recursos, ARNs etc.).
- Confirme que serviços dependentes foram criados (ECR repository, ECS cluster/service, AutoScalingGroup, ALB, S3 artifacts, CodeBuild/CodePipeline).

Se preferir usar a AWS CLI com a URL do template principal no S3, o comando equivalente seria (substitua o URL e parâmetros):

```powershell
aws cloudformation create-stack --stack-name FlaskApplication --template-url https://s3.amazonaws.com/SEU_BUCKET/main.yaml --capabilities CAPABILITY_IAM --parameters ParameterKey=ProjectName,ParameterValue=meu-projeto
```

## CI/CD
O pipeline de CI/CD é definido pelo arquivo `iac/buildspec/buildspec.yaml` e utiliza parâmetros e variáveis de ambiente como nomes de repositórios ECR, cluster ECS e conexão GitHub (GitHub v2 Connection ARN). O pipeline realiza:
- Build da imagem Docker
- Push para ECR
- Atualização do serviço ECS para forçar novo deployment

## Detalhes da Implementação
Consulte [`docs/implementation.md`](docs/implementation.md) para uma descrição detalhada das etapas realizadas na implementação da infraestrutura, incluindo screenshots e evidências de funcionamento.

## Documentação

- Arquitetura: `docs/arquitetura.png`
- Implementação: `docs/implementation.md`

## Autora

Maria Eduarda Lopes Maldonado

## Orientador

Prof. Me. Francisco Alves de Freitas Neto

---