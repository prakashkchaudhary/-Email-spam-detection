# Contributing to Email Spam Detection System

Thank you for your interest in contributing to the Email Spam Detection System! This document provides guidelines for contributing to the project.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [How to Contribute](#how-to-contribute)
4. [Development Guidelines](#development-guidelines)
5. [Pull Request Process](#pull-request-process)
6. [Reporting Bugs](#reporting-bugs)
7. [Suggesting Enhancements](#suggesting-enhancements)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

### Our Standards

- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic understanding of Machine Learning and Flask

### Setup Development Environment

1. **Fork the repository**
   ```bash
   # Click "Fork" button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/email-spam-detection.git
   cd email-spam-detection
   ```

3. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug fixes**: Fix issues in existing code
- **New features**: Add new functionality
- **Documentation**: Improve or add documentation
- **Tests**: Add or improve test coverage
- **Performance**: Optimize existing code
- **UI/UX**: Improve user interface and experience

### Areas for Contribution

1. **Machine Learning**
   - Implement new ML algorithms
   - Improve model accuracy
   - Add hyperparameter tuning
   - Implement cross-validation

2. **Natural Language Processing**
   - Add new preprocessing techniques
   - Implement advanced NLP features
   - Support multiple languages

3. **Web Application**
   - Improve UI/UX design
   - Add new features (file upload, batch processing)
   - Implement user authentication
   - Add API documentation

4. **Testing**
   - Write unit tests
   - Add integration tests
   - Improve test coverage

5. **Documentation**
   - Improve README
   - Add code comments
   - Create tutorials
   - Write API documentation

## Development Guidelines

### Code Style

**Python:**
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions small and focused

**Example:**
```python
def preprocess_text(text):
    """
    Preprocess text for spam detection.
    
    Args:
        text (str): Raw text to preprocess
        
    Returns:
        str: Preprocessed text
    """
    # Implementation
    pass
```

**JavaScript:**
- Use ES6+ features
- Use camelCase for variables
- Add comments for complex logic

**CSS:**
- Use meaningful class names
- Follow BEM naming convention
- Keep selectors specific

### Commit Messages

Write clear, descriptive commit messages:

```
feat: Add batch prediction feature
fix: Resolve model loading issue
docs: Update installation guide
test: Add tests for preprocessing
style: Format code according to PEP 8
refactor: Simplify feature extraction logic
perf: Optimize model prediction speed
```

### Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for >80% code coverage

**Run tests:**
```bash
python -m pytest tests/ -v
```

### Documentation

- Update README.md for new features
- Add docstrings to new functions
- Update API documentation
- Include examples in documentation

## Pull Request Process

### Before Submitting

1. **Update your fork**
   ```bash
   git fetch upstream
   git merge upstream/main
   ```

2. **Run tests**
   ```bash
   python -m pytest tests/
   ```

3. **Check code style**
   ```bash
   flake8 src/ app.py
   ```

4. **Update documentation**
   - Update README if needed
   - Add docstrings
   - Update CHANGELOG

### Submitting Pull Request

1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request**
   - Go to GitHub repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in PR template

3. **PR Description Template**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Performance improvement
   
   ## Testing
   - [ ] Tests pass locally
   - [ ] Added new tests
   - [ ] Updated documentation
   
   ## Screenshots (if applicable)
   Add screenshots here
   
   ## Related Issues
   Closes #issue_number
   ```

### Review Process

1. Maintainers will review your PR
2. Address any requested changes
3. Once approved, PR will be merged

## Reporting Bugs

### Before Reporting

- Check if bug already reported
- Verify bug exists in latest version
- Collect relevant information

### Bug Report Template

```markdown
**Describe the bug**
Clear description of the bug

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen

**Screenshots**
If applicable, add screenshots

**Environment:**
- OS: [e.g., Windows 10]
- Python version: [e.g., 3.11]
- Browser: [e.g., Chrome 120]

**Additional context**
Any other relevant information
```

## Suggesting Enhancements

### Enhancement Template

```markdown
**Is your feature request related to a problem?**
Clear description of the problem

**Describe the solution you'd like**
Clear description of desired solution

**Describe alternatives you've considered**
Alternative solutions or features

**Additional context**
Any other relevant information
```

## Development Workflow

### Typical Workflow

1. **Find an issue** or create one
2. **Comment** on the issue to claim it
3. **Fork** the repository
4. **Create branch** from main
5. **Make changes** and commit
6. **Write tests** for changes
7. **Update documentation**
8. **Push** to your fork
9. **Create Pull Request**
10. **Address review** comments
11. **Merge** after approval

### Branch Naming

- `feature/feature-name` - New features
- `fix/bug-description` - Bug fixes
- `docs/what-changed` - Documentation
- `test/what-tested` - Tests
- `refactor/what-refactored` - Refactoring

## Code Review Guidelines

### For Reviewers

- Be respectful and constructive
- Explain reasoning for requested changes
- Approve when ready
- Provide specific feedback

### For Contributors

- Respond to feedback promptly
- Ask questions if unclear
- Make requested changes
- Thank reviewers

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in documentation

## Questions?

- Open an issue for questions
- Join our community discussions
- Email: your.email@example.com

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to Email Spam Detection System!** 🎉
