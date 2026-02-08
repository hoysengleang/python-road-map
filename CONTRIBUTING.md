# Contributing to Python Learning Repository

## 🎯 About This Repository
This is a personal learning repository focused on mastering Python for AI Research and Development. While this is primarily for personal learning, contributions that improve the learning materials are welcome!

## 🔧 Setting Up Your Development Environment

1. **Fork and clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/python-ai.git
cd python-ai
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# venv\Scripts\activate    # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 📝 Code Style Guidelines

### Python Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Keep functions focused and small
- Add comments for complex logic

### Before Committing
Run these commands to ensure code quality:

```bash
# Format your code
black src/

# Check for linting issues
flake8 src/

# Run pylint
pylint src/
```

## 🧪 Testing
While this is a learning repository, adding tests is encouraged:

```bash
# Run tests (if any)
pytest tests/ -v
```

## 🚀 Making a Pull Request

1. Create a new branch for your changes
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit
```bash
git add .
git commit -m "Description of your changes"
```

3. Push to your fork
```bash
git push origin feature/your-feature-name
```

4. Open a Pull Request on GitHub

## 💡 What to Contribute

### Welcomed Contributions
- ✅ Bug fixes in existing code
- ✅ Better explanations or comments
- ✅ Additional examples or exercises
- ✅ Improved code structure
- ✅ Documentation improvements

### Not Needed
- ❌ Major refactoring (this is learning code)
- ❌ Overly complex solutions
- ❌ Removing educational comments

## 📚 Learning Resources
When adding new examples, consider including:
- Clear comments explaining the concept
- Real-world use cases
- Common pitfalls to avoid
- Links to additional resources

## ⚠️ Code of Conduct
Be respectful, helpful, and constructive. This is a learning environment!

## 🤔 Questions?
Feel free to open an issue for any questions or suggestions.

---
Happy Learning! 🐍
