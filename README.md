# Python Learning Repository

[![Python CI](https://github.com/YOUR_USERNAME/python-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/python-ai/actions/workflows/ci.yml)

## 🎯 Goal
Learning Python to accomplish my goal: **AI Research and Development Backend**

## 📚 Topics Covered
- Object-Oriented Programming (OOP)
- Decorators
- Inheritance
- Dictionary & Array Mastery
- And more...

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher

### Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/python-ai.git
cd python-ai

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🧪 Running the Code
Navigate to any exercise and run it:
```bash
python src/exercise/Decorators/Property.py
```

## 🛠️ Development

### Code Quality Tools
This project uses several tools to maintain code quality:
- **flake8**: Linting
- **black**: Code formatting
- **pylint**: Additional linting
- **pytest**: Testing framework
- **bandit**: Security scanning
- **pre-commit**: Git hooks for automatic checks

### Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Set up pre-commit hooks (optional but recommended)
pre-commit install

# Verify your setup
./scripts/verify-ci.sh
```

### Running Code Quality Checks
```bash
# Format code automatically
black src/

# Check code style
flake8 src/

# Run pylint
pylint src/

# Run tests
pytest tests/ -v

# Run security check
bandit -r src/
```

For more details, see:
- 📖 [Quick Start Guide](docs/QUICK_START.md)
- 📖 [CI Setup Documentation](docs/CI_SETUP.md)
- 📖 [Contributing Guidelines](CONTRIBUTING.md)

## 📝 Project Structure
```
src/
├── basic/
│   └── OOP/
├── exercise/
│   ├── Decorators/
│   ├── Dictionary & Array Mastery/
│   └── inheritance/
└── project-small/
```

## 🤝 Contributing
This is a personal learning repository, but suggestions and improvements are welcome!

## 📄 License
This project is for educational purposes.