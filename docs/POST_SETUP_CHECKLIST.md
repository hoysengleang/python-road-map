# Post-Setup Checklist

Use this checklist to verify and complete your CI/CD setup.

## ✅ Initial Setup

### 1. Review What Was Created
- [ ] Read this checklist
- [ ] Browse through `docs/QUICK_START.md`
- [ ] Check out `docs/CI_SETUP.md`
- [ ] Look at `.github/workflows/ci.yml`

### 2. Install Dependencies
```bash
cd /home/leangdev/workspace/python-ai
source venv/bin/activate  # or activate your venv
pip install -r requirements.txt
```
- [ ] Dependencies installed successfully
- [ ] No error messages

### 3. Test Local CI Verification
```bash
./scripts/verify-ci.sh
```
- [ ] Script runs without errors
- [ ] All checks report status
- [ ] No critical issues found

### 4. Set Up Pre-commit Hooks (Recommended)
```bash
pre-commit install
```
- [ ] Pre-commit hooks installed
- [ ] Test with: `pre-commit run --all-files`

---

## 🔧 Configuration

### 5. Update README Badge
Open `README.md` and replace `YOUR_USERNAME` with your GitHub username:
```markdown
[![Python CI](https://github.com/YOUR_USERNAME/python-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/python-ai/actions/workflows/ci.yml)
```
- [ ] GitHub username updated in README
- [ ] Badge URL is correct

### 6. Format Existing Code
```bash
black src/
```
- [ ] Code formatted successfully
- [ ] Review changes with: `git diff`

### 7. Check for Linting Issues
```bash
flake8 src/ --statistics
```
- [ ] Review any issues found
- [ ] Fix critical issues (E9, F63, F7, F82)
- [ ] Note warnings for future improvement

---

## 📤 Push to GitHub

### 8. Review Changes
```bash
git status
git diff
```
- [ ] All new files listed
- [ ] Changes look correct
- [ ] No sensitive data included

### 9. Commit and Push
```bash
git add .
git commit -m "Add CI/CD pipeline with GitHub Actions

- Added GitHub Actions workflows for CI and formatting
- Configured flake8, black, pylint, and pytest
- Added pre-commit hooks configuration
- Created comprehensive documentation
- Added issue and PR templates
- Included example tests and verification script"

git push origin main  # or your branch name
```
- [ ] Commit successful
- [ ] Push successful
- [ ] No errors

### 10. Verify GitHub Actions
1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. Check if workflows are running

- [ ] Workflows appear in Actions tab
- [ ] CI workflow runs automatically
- [ ] Can see workflow logs

---

## 🧪 Test the CI Pipeline

### 11. Make a Test Change
Create a test branch and make a small change:
```bash
git checkout -b test-ci
echo "# Test CI" >> src/test_ci.py
git add src/test_ci.py
git commit -m "Test CI pipeline"
git push origin test-ci
```
- [ ] Test branch created
- [ ] Test file created and pushed

### 12. Create a Pull Request
1. Go to your repository on GitHub
2. Click "Pull requests"
3. Click "New pull request"
4. Select your test branch
5. Create the pull request

- [ ] PR created
- [ ] CI checks appear on PR
- [ ] Can see check status (pending/passing/failing)

### 13. Review CI Results
- [ ] All checks completed
- [ ] Green checkmarks appear (or investigate failures)
- [ ] CI logs are readable

### 14. Clean Up Test
```bash
git checkout main
git branch -D test-ci
git push origin --delete test-ci
```
- [ ] Test branch deleted locally
- [ ] Test branch deleted on GitHub
- [ ] PR closed or merged

---

## 📚 Final Review

### 15. Documentation
- [ ] Read `CONTRIBUTING.md`
- [ ] Understand the PR template
- [ ] Know where to find CI documentation
- [ ] Bookmarked helpful sections

### 16. Local Workflow
Test your daily workflow:
```bash
# 1. Make a change to any Python file
# 2. Format it
black src/exercise/Decorators/Property.py

# 3. Check linting
flake8 src/exercise/Decorators/Property.py

# 4. Run the file
python src/exercise/Decorators/Property.py

# 5. Verify everything
./scripts/verify-ci.sh
```
- [ ] Can format code
- [ ] Can check linting
- [ ] Can run verification script
- [ ] Understand the workflow

### 17. Security Check
```bash
bandit -r src/
```
- [ ] Security scan completed
- [ ] Understand the output
- [ ] No critical issues (or documented)

---

## 🎯 Optional Enhancements

### 18. Add Tests for Your Code
- [ ] Created test file in `tests/`
- [ ] Tests pass: `pytest tests/ -v`
- [ ] Understand test structure

### 19. Explore Pre-commit Hooks
```bash
pre-commit run --all-files
```
- [ ] Hooks run successfully
- [ ] Understand what each hook does
- [ ] Hooks run automatically on commit

### 20. Set Up Branch Protection (if desired)
On GitHub:
1. Go to Settings → Branches
2. Add rule for `main` branch
3. Enable "Require status checks to pass"
4. Select your CI checks

- [ ] Branch protection configured
- [ ] Required checks selected
- [ ] Settings tested

---

## 📊 Success Criteria

Your CI/CD setup is complete when:
- ✅ GitHub Actions workflows run on push/PR
- ✅ CI badge shows status on README
- ✅ Pre-commit hooks work locally
- ✅ Can run local verification successfully
- ✅ Understand how to fix common issues
- ✅ Documentation is clear and accessible

---

## 🆘 Troubleshooting

### Common Issues

**Issue:** Pre-commit hooks fail
- **Solution:** Run `pre-commit run --all-files` to see details
- **Solution:** Fix issues and try again
- **Workaround:** `git commit --no-verify` (not recommended)

**Issue:** CI fails on GitHub but passes locally
- **Solution:** Check Python version (CI uses 3.10, 3.11, 3.12)
- **Solution:** Ensure all dependencies in `requirements.txt`
- **Solution:** Check for OS-specific code

**Issue:** Black formatting changes too much
- **Solution:** This is normal on first run
- **Solution:** Review changes, commit them
- **Solution:** Future changes will be minimal

**Issue:** Can't push to main branch
- **Solution:** May have branch protection enabled
- **Solution:** Create a PR instead
- **Solution:** Check repository settings

**Issue:** Flake8 reports many warnings
- **Solution:** Fix critical errors first (E9, F63, F7, F82)
- **Solution:** Gradually improve warnings
- **Solution:** Learn from each warning

---

## 📞 Next Steps

1. **Start Learning:** Continue your Python learning journey
2. **Write Tests:** Add tests for new code
3. **Follow Best Practices:** Use the CI feedback to improve
4. **Document:** Comment your code and exercises
5. **Share:** Your setup can help others learn!

---

## 🎉 Congratulations!

Your CI/CD pipeline is set up and ready to use!

This will help you:
- Write better code
- Catch errors early
- Learn professional practices
- Build a strong portfolio

Keep learning and coding! 🚀🐍

---

**Questions?** Check the documentation in `docs/` or open a GitHub issue.

**Date Completed:** _______________

**Notes:**
_________________________________
_________________________________
_________________________________
