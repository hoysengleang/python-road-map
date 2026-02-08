#!/bin/bash

# CI Setup and Verification Script
# This script helps you verify your CI setup locally

echo "🚀 Python Learning Repository - CI Setup Verification"
echo "======================================================"
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
echo "🐍 Checking Python version..."
python_version=$(python --version 2>&1)
echo "   $python_version"
echo ""

# Check if virtual environment is active
if [[ -z "${VIRTUAL_ENV}" ]]; then
    echo -e "${YELLOW}⚠️  Warning: Virtual environment not activated${NC}"
    echo "   Recommendation: Activate your venv with 'source venv/bin/activate'"
    echo ""
else
    echo -e "${GREEN}✅ Virtual environment active: ${VIRTUAL_ENV}${NC}"
    echo ""
fi

# Install/Update dependencies
echo "📦 Installing development dependencies..."
pip install -r requirements.txt --quiet
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Dependencies installed successfully${NC}"
else
    echo -e "${RED}❌ Failed to install dependencies${NC}"
    exit 1
fi
echo ""

# Run Black formatting check
echo "🎨 Checking code formatting with Black..."
black --check src/ > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Code is properly formatted${NC}"
else
    echo -e "${YELLOW}⚠️  Code formatting issues found${NC}"
    echo "   Run 'black src/' to auto-format"
fi
echo ""

# Run Flake8
echo "🔍 Running Flake8 linter..."
flake8 src/ --count --select=E9,F63,F7,F82 --statistics > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ No critical linting errors${NC}"
else
    echo -e "${RED}❌ Critical linting errors found${NC}"
    flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics
fi
echo ""

# Run Pylint
echo "📊 Running Pylint..."
pylint_output=$(pylint src/ --exit-zero 2>&1 | tail -n 2)
echo "   $pylint_output"
echo ""

# Run tests if they exist
if [ -d "tests" ]; then
    echo "🧪 Running tests..."
    pytest tests/ -v --tb=short
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ All tests passed${NC}"
    else
        echo -e "${RED}❌ Some tests failed${NC}"
    fi
else
    echo -e "${YELLOW}ℹ️  No tests directory found${NC}"
fi
echo ""

# Security check
echo "🔒 Running security scan..."
bandit -r src/ -ll -q > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ No high/medium security issues found${NC}"
else
    echo -e "${YELLOW}⚠️  Security issues detected${NC}"
    bandit -r src/ -ll
fi
echo ""

# Summary
echo "======================================================"
echo "✨ CI verification complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Fix any issues reported above"
echo "   2. Run 'black src/' to format code"
echo "   3. Install pre-commit hooks: 'pre-commit install'"
echo "   4. Commit and push your changes"
echo ""
echo "🔗 For more info, see: docs/CI_SETUP.md"
