# Python Setup & Environment Configuration

## Table of Contents
1. [Installation](#installation)
2. [Virtual Environments](#virtual-environments)
3. [IDE Setup](#ide-setup)
4. [Package Management](#package-management)
5. [Verification](#verification)
6. [Troubleshooting](#troubleshooting)

## Installation

### macOS Installation

#### Step 1: Download Python
```bash
# Method 1: Using Homebrew (Recommended)
brew install python@3.10

# Method 2: Download from python.org
# Visit https://www.python.org/downloads/ and download the .pkg file
```

#### Step 2: Verify Installation
```bash
python3 --version
# Output: Python 3.10.x

pip3 --version
# Output: pip 23.x from ...
```

#### Step 3: Add to PATH (if needed)
```bash
# Add to ~/.zshrc or ~/.bash_profile
export PATH="/usr/local/opt/python@3.10/bin:$PATH"

# Reload shell
source ~/.zshrc
```

### Windows Installation

#### Step 1: Download Installer
- Visit: https://www.python.org/downloads/
- Download Windows Installer (64-bit recommended)

#### Step 2: Run Installer
- Check ✅ "Add python.exe to PATH" (IMPORTANT!)
- Choose "Install Now" or customize installation
- Wait for installation to complete

#### Step 3: Verify Installation
```cmd
python --version
pip --version
```

### Linux Installation (Ubuntu/Debian)

```bash
# Update package manager
sudo apt-get update
sudo apt-get upgrade

# Install Python and pip
sudo apt-get install python3 python3-pip python3-venv

# Verify
python3 --version
pip3 --version
```

## Virtual Environments

### What is a Virtual Environment?

A virtual environment is an isolated Python environment that allows you to:
- Install packages for specific projects
- Avoid conflicts between projects
- Use different package versions
- Keep system Python clean

### Creating Virtual Environment

#### Using venv (Built-in)

```bash
# Navigate to your project directory
cd ~/my-data-engineering-project

# Create virtual environment named 'venv'
python3 -m venv venv

# Create with specific Python version
python3.10 -m venv venv
```

#### Using conda (Alternative)

```bash
# Create conda environment
conda create -n data-eng python=3.10

# Install packages
conda install -n data-eng pandas numpy

# List environments
conda env list
```

### Activating Virtual Environment

#### macOS/Linux
```bash
# Activate
source venv/bin/activate

# Check activation (should show (venv) prefix)
# Output: (venv) user@machine ~/project $

# Deactivate
deactivate
```

#### Windows
```cmd
# Activate
venv\Scripts\activate

# Check activation (should show (venv) prefix)
# Output: (venv) C:\Users\user\project>

# Deactivate
deactivate
```

### Project Structure with Virtual Environment

```
my-data-engineering-project/
├── venv/                          # Virtual environment (don't commit!)
│   ├── bin/                       # Executable scripts
│   ├── lib/                       # Python packages
│   └── include/                   # C headers
├── src/
│   ├── main.py
│   ├── utils.py
│   └── config.py
├── tests/
│   └── test_main.py
├── data/
│   ├── input/
│   └── output/
├── requirements.txt               # Package list
├── README.md
├── .gitignore
└── setup.py                       # Project setup
```

## IDE Setup

### Visual Studio Code Setup

#### Installation
1. Download from: https://code.visualstudio.com/
2. Install the application
3. Open VS Code

#### Python Extension Installation

```bash
# Method 1: From Command Palette
Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (Mac)
Type: "Extensions: Install Extensions"
Search: "Python" (by Microsoft)
Click Install
```

#### Essential Extensions

1. **Python** (Microsoft)
   - Code execution
   - Debugging
   - IntelliSense

2. **Pylance**
   - Fast Python language server
   - Type checking
   - Better IntelliSense

3. **Jupyter**
   - Notebook support
   - Interactive computing

4. **Git Graph**
   - Git visualization

#### VS Code Settings

Create or update `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length", "88"],
    "editor.formatOnSave": true,
    "editor.rulers": [88],
    "[python]": {
        "editor.defaultFormatter": "ms-python.python",
        "editor.formatOnSave": true
    },
    "files.exclude": {
        "**/__pycache__": true,
        "**/.pytest_cache": true,
        "**/venv": true
    }
}
```

#### Debugging in VS Code

Create `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Python: Module",
            "type": "python",
            "request": "launch",
            "module": "mymodule",
            "console": "integratedTerminal"
        }
    ]
}
```

### PyCharm Setup (Alternative)

#### Installation
1. Download from: https://www.jetbrains.com/pycharm/
2. Install Community Edition (free)

#### Configure Interpreter
```
Settings → Project → Python Interpreter
Click ⚙️ → Add → Existing Environment
Select: venv/bin/python (macOS/Linux) or venv\Scripts\python.exe (Windows)
```

#### Keyboard Shortcuts
- `Ctrl+Shift+A`: Find action
- `Ctrl+/`: Comment/uncomment
- `Ctrl+Alt+L`: Format code
- `Shift+F10`: Run
- `Shift+F9`: Debug

## Package Management

### Installing Packages

#### Using pip

```bash
# Activate virtual environment first!
source venv/bin/activate

# Install single package
pip install pandas

# Install specific version
pip install pandas==2.0.0

# Install multiple packages
pip install pandas numpy scipy matplotlib

# Install from requirements file
pip install -r requirements.txt

# Install with development dependencies
pip install -e ".[dev]"
```

#### Common Data Engineering Packages

```bash
# Data manipulation
pip install pandas numpy scipy

# Databases
pip install mysql-connector-python psycopg2-binary pymongo

# APIs and HTTP
pip install requests httpx

# File formats
pip install openpyxl xmltodict

# Cloud
pip install boto3 azure-storage-blob

# Big Data
pip install pyspark

# Async
pip install asyncio aiohttp

# Testing
pip install pytest pytest-cov

# Code quality
pip install black flake8 pylint mypy
```

### Creating Requirements File

#### Freeze Current Environment
```bash
# Generate requirements.txt
pip freeze > requirements.txt

# Pin specific versions
pip freeze --all > requirements.txt
```

#### Manual Requirements File Creation

Create `requirements.txt`:

```
# Data Processing
pandas==2.0.0
numpy==1.24.0
scipy==1.10.0

# Databases
mysql-connector-python==8.0.32
psycopg2-binary==2.9.6

# APIs
requests==2.31.0
httpx==0.24.1

# Testing
pytest==7.4.0
pytest-cov==4.1.0

# Code Quality
black==23.7.0
flake8==6.1.0
pylint==2.17.4
```

### Requirements File Best Practices

```
# requirements.txt
# Production dependencies

# Data processing
pandas>=2.0.0,<3.0.0
numpy>=1.24.0,<2.0.0

# CLI and utilities
click>=8.1.0
pyyaml>=6.0

# Testing
pytest>=7.0.0
pytest-cov>=4.0.0


# requirements-dev.txt
# Development dependencies
-r requirements.txt

black>=23.0.0
flake8>=6.0.0
pylint>=2.17.0
mypy>=1.0.0
pre-commit>=3.0.0
```

### Installing from Requirements

```bash
# Install all
pip install -r requirements.txt

# Install dev dependencies
pip install -r requirements-dev.txt

# Reinstall after updating requirements.txt
pip install --force-reinstall -r requirements.txt

# Remove all packages before fresh install
pip freeze | xargs pip uninstall -y
pip install -r requirements.txt
```

## Verification

### Verify Complete Setup

```bash
# Test 1: Python version
python3 --version
# Expected: Python 3.9.x or higher

# Test 2: pip version
pip --version
# Expected: pip 23.x or higher

# Test 3: Virtual environment
source venv/bin/activate
which python
# Expected: /path/to/venv/bin/python

# Test 4: Install and import package
pip install requests
python -c "import requests; print(requests.__version__)"

# Test 5: Create and run simple script
cat > test.py << 'EOF'
print("Python setup complete!")
import sys
print(f"Python version: {sys.version}")
import platform
print(f"Platform: {platform.platform()}")
EOF

python test.py
```

### Verification Script

Create `verify_setup.py`:

```python
"""
Verify Python setup is complete and working.
Run: python verify_setup.py
"""

import sys
import subprocess
import platform

def verify_python_version():
    """Check Python version is 3.9+"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 9:
        print(f"✓ Python version: {sys.version}")
        return True
    else:
        print(f"✗ Python version too old: {sys.version}")
        return False

def verify_pip():
    """Check pip is installed"""
    try:
        result = subprocess.run(
            ['pip', '--version'],
            capture_output=True,
            text=True
        )
        print(f"✓ Pip version: {result.stdout.strip()}")
        return True
    except:
        print("✗ Pip not found")
        return False

def verify_virtual_env():
    """Check if running in virtual environment"""
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    if in_venv:
        print(f"✓ Virtual environment active: {sys.prefix}")
        return True
    else:
        print("⚠ Not in virtual environment (activate venv first)")
        return False

def verify_common_packages():
    """Check common packages are available"""
    packages = ['pip', 'requests', 'json', 'csv']
    found = 0
    
    for package in packages:
        try:
            __import__(package)
            print(f"  ✓ {package}")
            found += 1
        except ImportError:
            print(f"  ✗ {package} (run: pip install {package})")
    
    return found == len(packages)

def main():
    """Run all verifications"""
    print("=" * 50)
    print("Python Setup Verification")
    print("=" * 50)
    print(f"Platform: {platform.platform()}\n")
    
    checks = [
        ("Python Version", verify_python_version()),
        ("Pip", verify_pip()),
        ("Virtual Environment", verify_virtual_env()),
        ("Common Packages", verify_common_packages())
    ]
    
    print("\n" + "=" * 50)
    print("Summary:")
    print("=" * 50)
    
    passed = sum(1 for _, result in checks if result)
    total = len(checks)
    
    print(f"\nPassed: {passed}/{total}")
    
    if passed == total:
        print("\n✓ Setup complete and ready to go!")
    else:
        print("\n⚠ Please fix the issues above before proceeding")
    
    return passed == total

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
```

## Troubleshooting

### Problem: Python command not found

**macOS/Linux:**
```bash
# Check if python3 is available
which python3

# If not found, install via Homebrew
brew install python@3.10

# Create alias
echo "alias python=python3" >> ~/.zshrc
source ~/.zshrc
```

**Windows:**
- Re-run installer
- Make sure to check "Add python.exe to PATH"
- Restart terminal after installation

### Problem: pip command not found

```bash
# Try pip3
pip3 --version

# Install pip if missing
python -m pip install --upgrade pip

# Create alias
alias pip=pip3
```

### Problem: Virtual environment not activating

```bash
# Check venv exists
ls venv/bin

# Recreate venv
rm -rf venv
python3 -m venv venv

# Activate again
source venv/bin/activate
```

### Problem: ImportError after package installation

```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Verify package installation
pip list | grep package_name

# Try reinstalling
pip uninstall package_name
pip install package_name
```

### Problem: Different Python versions conflicting

```bash
# View all Python versions on system
ls /usr/local/bin/python*

# Use specific version
python3.10 -m venv venv
python3.10 -m pip install package_name
```

## Best Practices

### Project Setup Checklist

```bash
# 1. Create project directory
mkdir my-project
cd my-project

# 2. Initialize git
git init

# 3. Create virtual environment
python3 -m venv venv

# 4. Activate virtual environment
source venv/bin/activate

# 5. Create .gitignore
echo "venv/
__pycache__/
*.pyc
.env
.vscode/
.idea/
.pytest_cache/" > .gitignore

# 6. Create project structure
mkdir -p src tests data

# 7. Create initial files
touch src/__init__.py
touch src/main.py
touch tests/__init__.py
touch requirements.txt
touch README.md

# 8. First commit
git add .
git commit -m "Initial project setup"
```

### Environment Variables

Create `.env` file:

```bash
# Database
DATABASE_URL=mysql://user:password@localhost:3306/dbname
DATABASE_USER=data_engineer
DATABASE_PASSWORD=secure_password

# API
API_KEY=your_api_key_here
API_BASE_URL=https://api.example.com

# AWS
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1

# Logging
LOG_LEVEL=INFO
LOG_FILE=app.log
```

Load in code:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
database_url = os.getenv('DATABASE_URL')
```

---

**Setup Guide Version**: 1.0  
**Last Updated**: June 2026
