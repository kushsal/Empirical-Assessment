# EmpiricalAssessment

A robust, scalable Selenium-Pytest automation framework built for empirical UI assessment and data-driven testing. Designed and maintained by Kushal, a Senior Test Engineer and certified Scrum Master passionate about Agile quality and maintainable automation.


## Overview

This framework supports:
- Pytest-based test execution
- Selenium WebDriver integration
- Excel-driven test data mapping
- HTML reporting via `pytest-html`
- Modular POM structure
- Utility-driven design for reusability
- Logger functionality for individual test cases


## 📁 Project Structure
EmpiricalAssessment/
├── POM/
├── Tests/
├── Utilities/
├── TestData/
├── reports/
├── requirements.txt
└── README.md


## ⚙️ Technologies Used

- Python 3.x
- Selenium WebDriver
- Pytest
- openpyxl
- pytest-html
- PyCharm IDE


## How to Run Tests
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run all tests with HTML report:
   pytest --html=reports/report.html

3. If anything is unclear, refer the demo video here to get more elaborate details - https://screenrec.com/share/SEjPLZWHXN