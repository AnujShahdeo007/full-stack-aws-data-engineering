# Assignment Guidelines

## Overview

This document provides comprehensive guidelines for completing and submitting assignments throughout the Full Stack AWS Data Engineering course.

## Assignment Types

### 1. **Practice Exercises** (No Submission)
- Short coding tasks to reinforce concepts
- Practice before assessments
- Solutions available for reference
- **Time**: 15-30 minutes each
- **Purpose**: Skill building

### 2. **Graded Assignments** (Submission Required)
- Evaluated for correctness and code quality
- Contributes to course grade
- **Time**: 2-4 hours each
- **Frequency**: 2-3 per week
- **Grade Weight**: 20%

### 3. **Mini Projects** (Submission Required)
- Practical application of 2-3 modules
- More complex than assignments
- **Time**: 4-8 hours each
- **Frequency**: 1 per week (after Week 5)
- **Grade Weight**: 30%

### 4. **Capstone Project** (Submission Required)
- End-to-end integration project
- Covers entire course curriculum
- **Time**: 40-60 hours
- **Frequency**: 1 (Weeks 24-26)
- **Grade Weight**: 30%

## Submission Requirements

### For All Submissions

#### 1. **Code Requirements**
- ✅ Well-commented code
- ✅ Meaningful variable names
- ✅ Follows PEP 8 (for Python)
- ✅ No hardcoded values (use config files)
- ✅ Error handling implemented
- ✅ Logging included for data flows

#### 2. **File Organization**
```
assignment_name/
├── src/
│   ├── main.py
│   ├── utils.py
│   ├── config.py
│   └── ...
├── tests/
│   ├── test_main.py
│   └── ...
├── data/
│   ├── input/
│   └── output/
├── README.md
├── requirements.txt
└── .gitignore
```

#### 3. **Documentation**
- README.md with:
  - Project description
  - How to run the code
  - Dependencies and versions
  - Sample input/output
  - Any assumptions made
  - Known limitations

#### 4. **Requirements File**
```
# requirements.txt
package_name==version
```

Example:
```
pandas==2.0.0
numpy==1.24.0
mysql-connector-python==8.0.32
boto3==1.26.0
```

#### 5. **Executable Instructions**
Provide step-by-step instructions to run:
```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Set up configuration
# Edit config.py with your settings

# Step 3: Run the script
python src/main.py
```

### For Python Assignments

#### Code Quality Standards

1. **Naming Conventions**
   ```python
   # ✅ Good
   def process_customer_data(customer_file):
       total_customers = 0
       for customer in customers:
           ...
   
   # ❌ Bad
   def p_c_d(f):
       t = 0
       for c in cs:
           ...
   ```

2. **Comments & Docstrings**
   ```python
   def calculate_discount(amount, discount_percentage):
       """
       Calculate discounted price.
       
       Args:
           amount (float): Original amount
           discount_percentage (float): Discount percentage (0-100)
           
       Returns:
           float: Discounted amount
       """
       return amount * (1 - discount_percentage / 100)
   ```

3. **Error Handling**
   ```python
   try:
       data = pd.read_csv('data.csv')
   except FileNotFoundError:
       logger.error("File not found: data.csv")
       raise
   except pd.errors.ParserError:
       logger.error("Error parsing CSV file")
       raise
   ```

4. **Logging**
   ```python
   import logging
   
   logger = logging.getLogger(__name__)
   logger.info(f"Processing {len(data)} records")
   logger.warning(f"Found {null_count} null values")
   logger.error(f"Failed to process record: {record}")
   ```

### For SQL Assignments

#### SQL Standards

1. **Formatting**
   ```sql
   -- ✅ Good - Readable and formatted
   SELECT 
       customer_id,
       customer_name,
       SUM(order_amount) AS total_spent
   FROM customers c
   JOIN orders o ON c.customer_id = o.customer_id
   WHERE order_date >= '2024-01-01'
   GROUP BY customer_id, customer_name
   HAVING SUM(order_amount) > 1000
   ORDER BY total_spent DESC;
   
   -- ❌ Bad - Hard to read
   SELECT customer_id, customer_name, SUM(order_amount) FROM customers c JOIN orders o ON c.customer_id = o.customer_id WHERE order_date >= '2024-01-01' GROUP BY customer_id, customer_name HAVING SUM(order_amount) > 1000;
   ```

2. **Comments**
   ```sql
   -- Purpose: Get top customers by spending
   -- Period: Since 2024-01-01
   -- Notes: Excludes customers with less than $1000 spent
   ```

3. **Query Organization**
   - Use meaningful aliases
   - Include business logic explanations
   - Show query results with sample data

### For AWS Assignments

#### AWS Best Practices

1. **IAM Security**
   - Use least privilege principle
   - Never use root account
   - Create specific roles and policies
   - Never hardcode credentials

2. **S3 Organization**
   - Use meaningful bucket names
   - Organize with prefixes
   - Document structure
   - Include sample data

3. **Configuration**
   - Use AWS Systems Manager Parameter Store
   - Environment-specific configs
   - Document all assumptions

### For Data Engineering Projects

#### Data Pipeline Standards

1. **Data Validation**
   ```python
   def validate_data(dataframe):
       """Validate data quality"""
       assert not dataframe.empty, "DataFrame is empty"
       assert dataframe.isnull().sum().sum() == 0, "Contains nulls"
       assert dataframe['amount'].min() >= 0, "Negative amounts found"
       return True
   ```

2. **Logging Data Flows**
   ```python
   logger.info(f"Extracted {row_count} rows from source")
   logger.info(f"Transformed {processed_count} rows")
   logger.info(f"Loaded {loaded_count} rows to target")
   ```

3. **Error Recovery**
   - Document failed records
   - Implement retry logic
   - Provide recovery procedures

## Submission Process

### Step 1: Prepare Your Work
- [ ] Code complete and tested
- [ ] All requirements met
- [ ] Documentation complete
- [ ] No sensitive data included

### Step 2: Create GitHub Repository
```bash
# Initialize local repository
git init

# Add files
git add .

# Commit with meaningful message
git commit -m "Assignment: [Name] - [Description]"

# Push to GitHub
git push origin main
```

### Step 3: Submission Portal
1. Go to assignment submission portal
2. Paste GitHub repository link
3. Add any additional notes
4. Click Submit

### Step 4: Late Submission
- Submissions accepted up to 7 days late
- 10% penalty per day late
- No submissions accepted after 7 days
- Exceptions require written approval

## Grading Criteria

### Code Quality (40%)
- Code clarity and readability
- Proper naming conventions
- Comments and documentation
- Error handling
- Modularity and reusability

### Functionality (40%)
- Meets all requirements
- Handles edge cases
- Produces correct output
- Performance acceptable
- No obvious bugs

### Documentation (20%)
- README quality
- Inline comments
- Code comments
- Usage examples
- Setup instructions

### Bonus Criteria (Up to +10%)
- Extra features implemented
- Performance optimizations
- Additional test cases
- Creative solutions

## Example Grading Rubric

| Criteria | Excellent (90-100) | Good (80-89) | Satisfactory (70-79) | Needs Improvement (<70) |
|----------|------------------|--------------|---------------------|-----------------------|
| **Code Quality** | Well-organized, clear, DRY | Good structure, minor issues | Acceptable but could improve | Poor organization, duplicate code |
| **Functionality** | All requirements met, edge cases handled | All requirements met | Most requirements met | Missing requirements |
| **Documentation** | Comprehensive, clear | Good, mostly clear | Adequate but incomplete | Minimal or unclear |
| **Testing** | Thorough tests included | Basic tests included | Limited testing | No tests |
| **Performance** | Optimized | Acceptable | Works but slow | Very slow |

## Common Mistakes to Avoid

### 1. **Not Following Instructions**
- ❌ Using different naming conventions
- ❌ Submitting in wrong format
- ❌ Missing required components
- ✅ Read instructions 2-3 times
- ✅ Create checklist before submitting

### 2. **Poor Code Quality**
- ❌ No comments or unclear comments
- ❌ Hardcoded values
- ❌ No error handling
- ✅ Write clean, readable code
- ✅ Handle exceptions properly

### 3. **Incomplete Documentation**
- ❌ No README
- ❌ No setup instructions
- ❌ No explanation of approach
- ✅ Write comprehensive README
- ✅ Include step-by-step instructions

### 4. **Security Issues**
- ❌ Hardcoded credentials
- ❌ Exposed API keys
- ❌ Sensitive data in repo
- ✅ Use environment variables
- ✅ Add .gitignore

### 5. **Not Testing**
- ❌ Code not tested before submission
- ❌ No unit tests
- ❌ Missing edge case handling
- ✅ Test thoroughly
- ✅ Write test cases

### 6. **Late Submission**
- ❌ Missing deadlines
- ❌ No notification of delays
- ✅ Start early
- ✅ Plan time buffer

## Testing Your Work

### Before Submission Checklist

```bash
# 1. Check code runs without errors
python src/main.py

# 2. Test with different inputs
python src/main.py --input test_data.csv

# 3. Check all requirements met
# [ ] All features implemented
# [ ] No hardcoded values
# [ ] Error handling present
# [ ] Logging implemented

# 4. Review documentation
# [ ] README complete
# [ ] Instructions clear
# [ ] Examples provided

# 5. Check file organization
# [ ] Organized in proper structure
# [ ] No unnecessary files
# [ ] requirements.txt updated

# 6. Verify git repository
git log  # Check commits
git status  # Ensure everything committed
```

## Feedback & Resubmission

### Receiving Feedback
- Submitted work graded within 5-7 days
- Detailed feedback provided
- Score with justification
- Suggestions for improvement

### Resubmission (If Needed)
- Allowed if score < 70%
- Must address all feedback
- Can resubmit within 3 days
- Grade cap at 85% for resubmission

## Plagiarism Policy

### What Constitutes Plagiarism
- ❌ Copying code from peers
- ❌ Using code without attribution
- ❌ Submitting others' work
- ❌ Using online solutions directly

### Consequences
- First offense: Score = 0 for assignment
- Second offense: Score = 0 for module
- Third offense: Removal from course

### Proper Attribution
```python
# Code adapted from https://example.com/solution
# Original author: John Doe
# Modified for: [your use case]
```

### Allowed Practices
- ✅ Referencing official documentation
- ✅ Using Stack Overflow solutions with attribution
- ✅ Using libraries and frameworks
- ✅ Learning from peers and discussing
- ✅ Using AI tools with documentation

## Getting Help

### Before Asking for Help
- [ ] Read assignment instructions 2-3 times
- [ ] Check course documentation
- [ ] Search for similar solutions
- [ ] Try debugging independently
- [ ] Check error messages

### How to Ask Questions
1. Search Q&A forum first
2. Provide specific error messages
3. Share relevant code snippet
4. Describe what you've tried
5. Mention your Python/Tool versions

### Available Support
- Community forums: 24-48 hour response
- Mentor office hours: Scheduled
- Live Q&A sessions: Weekly
- Instructor email: 48-hour response

## Assignment Deadline Calendar

| Week | Assignment Type | Deadline | Grade Weight |
|------|-----------------|----------|--------------|
| 1-4 | Weekly exercises | Friday EOD | 5% each |
| 5-12 | Bi-weekly assignments | Friday EOD | 5% each |
| 5-26 | Mini projects | Sunday EOD | 30% |
| 24-26 | Capstone project | Final date | 30% |

## Celebrating Success

### Showcase Your Work
- Share interesting projects
- Explain your approach
- Help peers understand
- Build your portfolio

### Contributing to Course
- Submit solutions to be shared
- Provide feedback to peers
- Answer questions in forums
- Improve course materials

---

**Assignment Guidelines Version**: 1.0  
**Last Updated**: June 2026  
**Questions?**: Check FAQ or contact instructors
