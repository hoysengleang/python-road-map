# Continuous Integration (CI) Setup

This repository uses GitHub Actions for Continuous Integration to ensure code quality and consistency.

## 🔄 CI Workflows

### 1. Main CI Workflow (`ci.yml`)
Runs on every push and pull request to `main`, `master`, or `develop` branches.

**What it does:**
- ✅ Tests on Python 3.10, 3.11, and 3.12
- ✅ Lints code with flake8
- ✅ Checks code formatting with black
- ✅ Runs pylint for additional code quality checks
- ✅ Executes all Python files with `__main__` blocks
- ✅ Runs pytest tests (if tests directory exists)
- ✅ Security scanning with bandit
- ✅ Dependency vulnerability check with safety

### 2. Formatting Check Workflow (`formatting.yml`)
Runs on pull requests to ensure code is properly formatted.

**What it does:**
- ✅ Checks if all code follows black formatting standards
- ✅ Provides diff of formatting issues if found

## 🚀 Running CI Checks Locally

Before pushing your code, run these checks locally to catch issues early:

### 1. Install Development Dependencies
```bash
pip install -r requirements.txt
```

### 2. Format Your Code
```bash
# Automatically format all Python files
black src/

# Check formatting without making changes
black --check src/
```

### 3. Run Linting
```bash
# Check for syntax errors and undefined names
flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics

# Full linting (with warnings)
flake8 src/ --count --max-complexity=10 --max-line-length=127 --statistics

# Run pylint
pylint src/
```

### 4. Run Tests
```bash
# Run all tests with coverage
pytest tests/ -v --cov=src/ --cov-report=term-missing

# Run specific test file
pytest tests/test_example.py -v
```

### 5. Security Checks
```bash
# Check for security issues
bandit -r src/

# Check for vulnerable dependencies
safety check
```

## 🎣 Pre-commit Hooks (Optional but Recommended)

Pre-commit hooks automatically run checks before each commit.

### Setup
```bash
# Install pre-commit
pip install pre-commit

# Install the git hooks
pre-commit install
```

### Usage
```bash
# Runs automatically on 'git commit'
# Or run manually on all files:
pre-commit run --all-files
```

### What Pre-commit Checks
- Trailing whitespace removal
- End-of-file fixing
- YAML validation
- Large file detection
- Merge conflict detection
- Black formatting
- Flake8 linting
- Pylint checks

## 📊 CI Status Badge

Add this badge to your README to show CI status:

```markdown
[![Python CI](https://github.com/YOUR_USERNAME/python-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/python-ai/actions/workflows/ci.yml)
```

Replace `YOUR_USERNAME` with your GitHub username.

## 🔧 Configuration Files

### `.pylintrc`
Controls pylint behavior. We've configured it to be more lenient for learning code:
- Disabled docstring requirements
- Allows short variable names (i, j, k, etc.)
- Max line length: 127 characters

### `.pre-commit-config.yaml`
Defines pre-commit hooks and their versions.

### `requirements.txt`
Lists all development and project dependencies.

## 🐛 Troubleshooting

### CI Fails on Formatting
Run `black src/` locally and commit the changes.

### CI Fails on Linting
Review the flake8/pylint output and fix the issues:
```bash
flake8 src/ --show-source
pylint src/
```

### Tests Fail Locally but Not in CI (or vice versa)
- Check Python version: `python --version`
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Clear Python cache: `find . -type d -name __pycache__ -exec rm -rf {} +`

### Pre-commit Hooks Too Strict
You can skip hooks temporarily:
```bash
git commit --no-verify
```
(But try to fix issues instead!)

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Black Formatter](https://black.readthedocs.io/)
- [Flake8 Rules](https://flake8.pycqa.org/)
- [Pylint Messages](https://pylint.pycqa.org/en/latest/messages/messages_list.html)
- [Pre-commit Hooks](https://pre-commit.com/)

## 🎯 Goals

The CI setup helps:
1. **Learn best practices** - See what professional Python projects check
2. **Catch errors early** - Before they become bigger problems
3. **Maintain consistency** - All code follows the same style
4. **Build good habits** - Write clean, tested, secure code

---

**Remember:** CI is here to help, not to frustrate. If you have questions about any CI failures, don't hesitate to ask!
