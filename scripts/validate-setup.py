#!/usr/bin/env python3
"""
CI/CD Setup Validator
Tests all CI components to ensure proper setup
"""
import subprocess
import sys
from pathlib import Path


def run_command(cmd, description):
    """Run a command and report results."""
    print(f"\n{'='*60}")
    print(f"Testing: {description}")
    print(f"{'='*60}")
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            print(f"✅ PASSED: {description}")
            return True
        else:
            print(f"❌ FAILED: {description}")
            print(f"Error: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"⏱️  TIMEOUT: {description}")
        return False
    except Exception as e:
        print(f"❌ ERROR: {description}")
        print(f"Exception: {str(e)}")
        return False


def check_file_exists(filepath, description):
    """Check if a file exists."""
    print(f"\n{'='*60}")
    print(f"Checking: {description}")
    print(f"{'='*60}")
    if Path(filepath).exists():
        print(f"✅ EXISTS: {filepath}")
        return True
    else:
        print(f"❌ MISSING: {filepath}")
        return False


def main():
    """Run all validation checks."""
    print("\n" + "="*60)
    print("🚀 CI/CD Setup Validation")
    print("="*60)

    results = []

    # Check critical files
    critical_files = [
        (".github/workflows/ci.yml", "Main CI workflow"),
        (".github/workflows/formatting.yml", "Formatting workflow"),
        (".pylintrc", "Pylint configuration"),
        (".pre-commit-config.yaml", "Pre-commit config"),
        ("requirements.txt", "Requirements file"),
        ("scripts/verify-ci.sh", "Verification script"),
        ("tests/test_example.py", "Example test"),
        ("docs/QUICK_START.md", "Quick start guide"),
        ("docs/CI_SETUP.md", "CI documentation"),
        ("CONTRIBUTING.md", "Contributing guide"),
    ]

    for filepath, description in critical_files:
        results.append(check_file_exists(filepath, description))

    # Check Python files syntax
    results.append(
        run_command(
            "python3 -m py_compile tests/test_example.py",
            "Python syntax check"
        )
    )

    # Check if script is executable
    results.append(
        check_file_exists("scripts/verify-ci.sh", "Verify script executable")
    )

    # Summary
    print("\n" + "="*60)
    print("📊 VALIDATION SUMMARY")
    print("="*60)
    passed = sum(results)
    total = len(results)
    print(f"✅ Passed: {passed}/{total}")
    print(f"❌ Failed: {total - passed}/{total}")

    if passed == total:
        print("\n🎉 All validations passed! CI/CD setup is complete!")
        print("\n📝 Next steps:")
        print("   1. Read docs/QUICK_START.md")
        print("   2. Install dependencies: pip install -r requirements.txt")
        print("   3. Run: ./scripts/verify-ci.sh")
        print("   4. Commit and push to GitHub")
        return 0
    else:
        print("\n⚠️  Some validations failed. Please review the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
