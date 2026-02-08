# 🚀 Quick Start Guide - CI/CD Setup

Welcome! This guide will help you get started with the CI/CD setup for this Python learning repository.

## 📦 What's Been Set Up

### ✅ GitHub Actions Workflows
1. **Main CI Pipeline** (`.github/workflows/ci.yml`)
   - Runs on: Push and Pull Requests
   - Tests: Python 3.10, 3.11, 3.12
   - Checks: Linting, formatting, security, tests

2. **Formatting Check** (`.github/workflows/formatting.yml`)
   - Runs on: Pull Requests
   - Ensures: Code follows Black formatting

### 📄 Configuration Files
- **`.pylintrc`** - Pylint configuration (learning-friendly)
- **`.pre-commit-config.yaml`** - Pre-commit hooks
- **`.gitignore`** - Already configured
- **`requirements.txt`** - Dev dependencies added

### 📚 Documentation
- **`README.md`** - Updated with badges and instructions
- **`CONTRIBUTING.md`** - Contribution guidelines
- **`docs/CI_SETUP.md`** - Detailed CI documentation

### 🔧 Tools & Scripts
- **`scripts/verify-ci.sh`** - Local CI verification script
- **`tests/test_example.py`** - Example test file

### 🎫 GitHub Templates
- Bug report template
- Enhancement template
- Question template
- Pull request template

## 🏃 Getting Started in 3 Steps

### Step 1: Install Dependencies
```bash
# Make sure you're in the project directory
cd /path/to/python-ai

# Activate virtual environment (if not already active)
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install all dependencies
pip install -r requirements.txt
```

### Step 2: Set Up Pre-commit (Optional but Recommended)
```bash
# Install pre-commit hooks
pre-commit install

# Test it
pre-commit run --all-files
```

### Step 3: Verify Everything Works
```bash
# Run the verification script
./scripts/verify-ci.sh

# Or manually:
black src/              # Format code
flake8 src/            # Check linting
pytest tests/          # Run tests
```

## 🔄 Daily Workflow

### Before Making Changes
```bash
# Update your branch
git pull origin main

# Create a new branch
git checkout -b feature/your-feature
```

### While Coding
```bash
# Run your code
python src/exercise/YourFile.py

# Format as you go
black src/

# Check for issues
flake8 src/
```

### Before Committing
```bash
# Verify everything is good
./scripts/verify-ci.sh

# Or let pre-commit do it
git add .
git commit -m "Your message"
# Pre-commit hooks run automatically!
```

### Pushing Changes
```bash
# Push to your branch
git push origin feature/your-feature

# Create Pull Request on GitHub
# CI will run automatically!
```

## 📊 Understanding CI Results

### ✅ All Checks Passed
Great! Your code is ready to merge.

### ❌ Formatting Failed
```bash
# Fix it locally
black src/
git add .
git commit -m "Fix formatting"
git push
```

### ❌ Flake8 Failed
```bash
# See what's wrong
flake8 src/ --show-source

# Fix the issues
# Commit and push
```

### ❌ Tests Failed
```bash
# Run tests locally
pytest tests/ -v

# Fix the failing tests
# Commit and push
```

## 🎯 Common Tasks

### Add a New Exercise
1. Create your file: `src/exercise/YourTopic/your_file.py`
2. Write your code with a `__main__` block
3. Format: `black src/exercise/YourTopic/your_file.py`
4. Test: `python src/exercise/YourTopic/your_file.py`
5. Commit and push

### Add Tests for Your Code
1. Create test file: `tests/test_your_topic.py`
2. Write tests using pytest
3. Run: `pytest tests/test_your_topic.py -v`
4. Commit and push

### Fix Linting Issues
```bash
# See all issues
flake8 src/ --show-source --statistics

# Fix them manually or:
black src/  # Fixes formatting issues automatically
```

## 🆘 Troubleshooting

### Virtual Environment Not Activated
```bash
# You'll see this warning in verify-ci.sh
source venv/bin/activate
```

### Import Errors in Tests
```bash
# Make sure you're in the project root
cd /path/to/python-ai

# Run tests with Python path
PYTHONPATH=. pytest tests/
```

### Pre-commit Hooks Failing
```bash
# See what failed
pre-commit run --all-files

# Fix issues and try again
# Or temporarily bypass (not recommended):
git commit --no-verify
```

### CI Passes Locally but Fails on GitHub
- Check Python version: CI uses 3.10, 3.11, 3.12
- Ensure all dependencies are in `requirements.txt`
- Check for OS-specific code (paths, line endings)

## 📚 Learning Resources

### Python Code Quality
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Black Documentation](https://black.readthedocs.io/)
- [Flake8 Rules](https://flake8.pycqa.org/en/latest/user/error-codes.html)

### Testing
- [Pytest Documentation](https://docs.pytest.org/)
- [Testing Best Practices](https://docs.python-guide.org/writing/tests/)

### GitHub Actions
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Python CI/CD Guide](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)

## 💡 Pro Tips

1. **Use Pre-commit Hooks** - They catch issues before CI does
2. **Run verify-ci.sh Often** - Don't wait for GitHub CI
3. **Format Early, Format Often** - Run `black src/` regularly
4. **Write Tests** - They help you learn and verify correctness
5. **Read CI Logs** - They tell you exactly what's wrong
6. **Ask Questions** - Use GitHub issues for questions

## 🎓 Why This Matters

As you learn Python for AI Research and Development:
- **Code Quality** - Learn professional standards
- **Testing** - Critical for ML/AI pipelines
- **Documentation** - Essential for research
- **CI/CD** - Industry standard practice
- **Git Workflow** - Collaboration skills

## 📞 Need Help?

1. Check `docs/CI_SETUP.md` for detailed docs
2. Open a GitHub issue with the "Question" template
3. Review the error messages - they're usually helpful!

---

**Remember:** CI is a learning tool, not a gatekeeper. Every failure is a chance to learn something new! 🚀

Happy Learning! 🐍
