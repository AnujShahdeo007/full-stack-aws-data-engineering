# Tools Required - Complete Tech Stack

## Overview

This document lists all the tools, software, and services you'll need for the Full Stack AWS Data Engineering course. Ensure you have access to these before starting.

## System Requirements

### Minimum Requirements
- **OS**: Windows 10+, macOS 10.15+, or Ubuntu 18.04+
- **RAM**: 8GB (16GB recommended)
- **Storage**: 50GB free space
- **Processor**: Intel i5/AMD Ryzen 5 or equivalent
- **Internet**: Stable broadband connection (5+ Mbps)

### Recommended Setup
- **OS**: macOS 12+ or Ubuntu 20.04+
- **RAM**: 16GB or more
- **Storage**: 100GB SSD
- **Processor**: Intel i7/Apple Silicon or AMD Ryzen 7
- **GPU**: Optional but helpful for Spark jobs

## Programming & Development

### 1. **Python**
- **Version**: Python 3.9 or higher (3.10+ recommended)
- **Installation**: Follow guide in `06_installation_guides/`
- **Use**: Core programming language for data engineering
- **Download**: https://www.python.org/downloads/
- **Status**: 🔴 Required

### 2. **IDE/Code Editor**
- **Primary**: Visual Studio Code (VS Code)
- **Alternative**: PyCharm, IntelliJ IDEA
- **Download**: https://code.visualstudio.com/
- **Extensions**: Python, Pylance, Git Graph
- **Status**: 🔴 Required

### 3. **Git & Version Control**
- **Tool**: Git (version control system)
- **Download**: https://git-scm.com/downloads
- **Account**: GitHub (free account)
- **Website**: https://github.com
- **Status**: 🔴 Required

### 4. **Package Managers**
- **pip**: Python package manager (comes with Python)
- **conda**: Alternative package manager (optional)
- **Download**: https://docs.conda.io/miniconda.html
- **Status**: 🟢 Included with Python

## Databases & SQL

### 1. **MySQL**
- **Version**: 8.0 or higher
- **Purpose**: Relational database practice
- **Download**: https://dev.mysql.com/downloads/mysql/
- **GUI Tool**: MySQL Workbench
- **Status**: 🔴 Required

### 2. **PostgreSQL**
- **Version**: 12 or higher
- **Purpose**: Advanced SQL practice
- **Download**: https://www.postgresql.org/download/
- **GUI Tool**: pgAdmin or DBeaver
- **Status**: 🔴 Required

### 3. **DBeaver**
- **Purpose**: Database management and queries
- **Download**: https://dbeaver.io/download/
- **Type**: Universal database tool
- **Status**: 🟢 Recommended

### 4. **SQLite**
- **Purpose**: Lightweight database for practice
- **Status**: 🟢 Lightweight alternative

## Big Data & Processing Frameworks

### 1. **Apache Spark**
- **Version**: 3.3.0 or higher
- **Installation**: Via Python (PySpark)
- **Installation Method**: `pip install pyspark`
- **Prerequisites**: Java 8+ or 11+
- **Status**: 🔴 Required

### 2. **Java Development Kit (JDK)**
- **Version**: Java 8, 11, or 17
- **Purpose**: Required for Spark, Hadoop, Kafka
- **Download**: https://www.oracle.com/java/technologies/javase-downloads.html
- **Alternative**: OpenJDK (free)
- **Status**: 🔴 Required (for Spark)

### 3. **Apache Kafka**
- **Version**: 3.4.0 or higher
- **Purpose**: Message streaming platform
- **Download**: https://kafka.apache.org/downloads
- **Status**: 🔴 Required (after Week 15)

### 4. **Apache Airflow**
- **Version**: 2.5.0 or higher
- **Installation**: `pip install apache-airflow`
- **Purpose**: Workflow orchestration
- **Status**: 🔴 Required (after Week 17)

## Cloud & AWS

### 1. **AWS Account**
- **Type**: Free tier account
- **Website**: https://aws.amazon.com/free/
- **Status**: 🔴 Required
- **Services Used**:
  - S3 (Storage)
  - Lambda (Serverless computing)
  - Glue (ETL service)
  - Athena (Query service)
  - Redshift (Data warehouse)
  - EC2 (Compute)
  - RDS (Managed database)
  - DynamoDB (NoSQL database)
  - CloudWatch (Monitoring)
  - IAM (Security & access)

### 2. **AWS CLI**
- **Version**: 2.0 or higher
- **Installation**: https://aws.amazon.com/cli/
- **Command**: `aws configure`
- **Status**: 🔴 Required

### 3. **AWS Console**
- **Access**: Web browser
- **URL**: https://console.aws.amazon.com
- **Status**: 🔴 Required

## Infrastructure as Code

### 1. **Terraform**
- **Version**: 1.3.0 or higher
- **Installation**: https://www.terraform.io/downloads.html
- **Purpose**: Infrastructure provisioning
- **Status**: 🔴 Required (after Week 19)

### 2. **AWS CloudFormation** (Alternative)
- **Type**: AWS native IaC
- **Status**: 🟢 Alternative to Terraform

## CI/CD & DevOps

### 1. **Jenkins**
- **Version**: Latest LTS
- **Installation**: Docker-based recommended
- **Purpose**: CI/CD pipeline automation
- **Status**: 🔴 Required (after Week 19)

### 2. **Docker**
- **Version**: 20.10 or higher
- **Download**: https://www.docker.com/products/docker-desktop
- **Purpose**: Containerization
- **Status**: 🔴 Required

### 3. **Kubernetes (kubectl)**
- **Version**: Latest stable
- **Installation**: https://kubernetes.io/docs/tasks/tools/
- **Purpose**: Container orchestration
- **Alternatives**: Docker Desktop has built-in Kubernetes
- **Status**: 🔴 Required (after Week 20)

### 4. **Minikube** (Optional for local K8s)
- **Download**: https://minikube.sigs.k8s.io/
- **Purpose**: Local Kubernetes cluster
- **Status**: 🟢 Optional

## Containerization

### 1. **Docker Desktop**
- **Includes**: Docker Engine, CLI, Docker Compose
- **Download**: https://www.docker.com/products/docker-desktop/
- **Status**: 🔴 Required

### 2. **Docker Hub**
- **Account**: Free account
- **Website**: https://hub.docker.com/
- **Purpose**: Container image repository
- **Status**: 🟢 Recommended

## Communication & Collaboration

### 1. **Postman**
- **Version**: Latest
- **Download**: https://www.postman.com/downloads/
- **Purpose**: API testing and development
- **Status**: 🔴 Required

### 2. **Slack** (Optional)
- **Purpose**: Team communication
- **Download**: https://slack.com/download
- **Status**: 🟢 Optional

### 3. **Zoom** (For live sessions)
- **Download**: https://zoom.us/download
- **Status**: 🟢 For classes

## Monitoring & Logging

### 1. **CloudWatch**
- **Purpose**: AWS monitoring and logging
- **Access**: AWS Console
- **Status**: 🔴 Required

### 2. **DataDog** (Optional)
- **Purpose**: Advanced monitoring
- **Website**: https://www.datadoghq.com/
- **Status**: 🟢 Optional

## Documentation & Learning

### 1. **Jupyter Notebook**
- **Installation**: `pip install jupyter`
- **Purpose**: Interactive coding and documentation
- **Status**: 🟢 Recommended

### 2. **VS Code Extensions**
- Python
- Pylance
- Git Graph
- Docker
- Kubernetes
- Markdown Preview
- Thunder Client (API testing)

### 3. **Documentation Tools**
- Markdown
- GitBook (optional)
- Notion (optional)

## Optional Tools

### 1. **Anaconda/Miniconda**
- **Purpose**: Environment management
- **Download**: https://docs.conda.io/miniconda.html
- **Status**: 🟢 Optional (pip is sufficient)

### 2. **VS Code Remote Development**
- **Purpose**: Work in containers
- **Status**: 🟢 Optional

### 3. **GitHub Copilot**
- **Purpose**: AI-assisted coding
- **Status**: 🟢 Optional (paid)

### 4. **ChatGPT/Claude**
- **Purpose**: Code assistance
- **Status**: 🟢 Helpful

## Browser Requirements

- **Chrome** (recommended): Latest version
- **Firefox**: Latest version
- **Safari**: Latest version (Mac)

### Required Browser Features
- JavaScript enabled
- Cookies enabled
- Local storage enabled
- Modern CSS support

## Installation Checklist

### Before Week 1
- [ ] Python 3.9+ installed
- [ ] VS Code installed with extensions
- [ ] Git installed and configured
- [ ] GitHub account created
- [ ] MySQL installed
- [ ] PostgreSQL installed
- [ ] DBeaver installed

### Before Week 5
- [ ] Java installed (JDK 8+)
- [ ] Spark installed
- [ ] Jupyter Notebook installed
- [ ] Postman installed

### Before Week 10
- [ ] AWS account created
- [ ] AWS CLI installed and configured
- [ ] Terraform installed

### Before Week 19
- [ ] Docker installed
- [ ] Jenkins ready (via Docker)
- [ ] kubectl installed

### Before Week 20
- [ ] Kubernetes cluster access
- [ ] Minikube or Docker Kubernetes enabled

## Installation Guides Location

Detailed installation guides for each tool:
- **Python**: `06_installation_guides/python_setup.md`
- **Databases**: `06_installation_guides/database_setup.md`
- **Spark**: `06_installation_guides/spark_setup.md`
- **AWS**: `06_installation_guides/aws_setup.md`
- **Docker**: `06_installation_guides/docker_setup.md`
- **Kubernetes**: `06_installation_guides/kubernetes_setup.md`

## Troubleshooting Common Issues

### Python Issues
- Python not in PATH
- pip not found
- Virtual environment not working

**Solution**: Follow `06_installation_guides/python_setup.md`

### Database Connection Issues
- Port conflicts (3306, 5432)
- Authentication errors
- Service not running

**Solution**: Check `06_installation_guides/database_setup.md`

### AWS Issues
- Credentials not configured
- Region issues
- IAM permissions

**Solution**: Refer to `06_installation_guides/aws_setup.md`

### Docker Issues
- Docker daemon not running
- Permission denied
- Image build failures

**Solution**: Check `06_installation_guides/docker_setup.md`

## Bandwidth & Storage Requirements

### Average Tool Sizes
- Python: ~100 MB
- Java: ~200 MB
- Spark: ~300 MB
- Docker: ~500 MB
- Databases: ~1-2 GB each
- Total minimum: ~5 GB

### Bandwidth Needed
- Initial setup: ~10-15 GB downloads
- Weekly updates: ~500 MB
- Recommended: Broadband (5+ Mbps)

## Cost Estimates

### Free Tier Services (Covered)
- ✅ AWS Free Tier (12 months)
- ✅ GitHub (free account)
- ✅ VS Code (free)
- ✅ Postman (free plan)
- ✅ All open-source tools

### Optional Paid Services
- **AWS**: After free tier (~$10-50/month depending on usage)
- **DataDog**: ~$15/month
- **GitHub Copilot**: ~$10/month
- **ChatGPT Plus**: ~$20/month

### Total Cost: $0 (fully free except optional tools)

## Verification Checklist

After installation, verify each tool:

```bash
# Python
python --version

# Git
git --version

# Java (for Spark)
java -version

# Docker
docker --version

# AWS CLI
aws --version

# Terraform
terraform --version

# kubectl
kubectl version --client
```

## Getting Help

If you encounter issues with any tool:

1. Check the specific installation guide: `06_installation_guides/`
2. Search the troubleshooting section
3. Post in community forums
4. Contact mentors or instructors
5. Refer to official documentation

## Next Steps

1. Review this list thoroughly
2. Check your system meets minimum requirements
3. Follow installation guides in order
4. Run verification commands
5. Contact support for any issues

---

**Tools List Version**: 1.0  
**Last Updated**: June 2026  
**Status**: Complete & Verified
