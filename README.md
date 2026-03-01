# QA Automation Portfolio

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green?logo=selenium)
![pytest](https://img.shields.io/badge/pytest-8.x-orange)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-black?logo=github)

Professional QA automation portfolio demonstrating end-to-end expertise in manual testing,
Selenium WebDriver automation, framework design, API testing, data-driven testing,
and database validation -- built and maintained from 2021 to present.

## Repository Structure
```
qa-portfolio/
├── framework/          # Core hybrid automation framework
│   ├── base_page.py    # Base class: waits, actions, assertions
│   ├── browser_factory.py  # Cross-browser WebDriver setup
│   └── logger.py       # Centralised logging
├── pages/              # Page Object Model (POM) classes
├── tests/              # Pytest test suites (60+ test cases)
├── api_tests/          # REST API tests (requests library)
├── utils/              # ExcelReader, DBValidator, test_data
├── sql-scripts/        # Backend validation SQL queries
├── manual-testing/     # Test plans, test cases, bug reports, RTM
├── docs/               # SDLC/STLC methodology docs
└── .github/workflows/  # GitHub Actions CI/CD pipeline
```

## Skills Demonstrated
| Area | Technologies |
|---|---|
| Automation | Selenium WebDriver 4.x, Python, pytest |
| Framework | Hybrid Framework, Page Object Model (POM) |
| Data-Driven | openpyxl, Excel-based test data |
| API Testing | requests, REST API validation |
| Manual Testing | Test plans, RTM, bug reports, STLC |
| Database | SQL SELECT, JOIN, GROUP BY, WHERE |
| CI/CD | GitHub Actions (headless, nightly) |
| Tools | JIRA, Xray, Bugzilla, Git |
| Browsers | Chrome, Firefox, Edge, Headless |

## Test Coverage
| Suite | Tests |
|---|---|
| Login | 9 |
| Inventory | 8 |
| Cart | 6 |
| Checkout | 7 |
| Advanced Selenium | 7 |
| ActionChains | 5 |
| Data-Driven | 6 |
| API | 14 |
| **Total** | **62** |

## Quick Start
```bash
git clone https://github.com/dhimanrgv/qa-portfolio.git
cd qa-portfolio
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
pytest --headless
pytest -m smoke
pytest tests/test_login.py -v
```

## About
Built by **dhimanrgv** -- QA Analyst, Toronto, Canada
Completed: Selenium WebDriver with Python from Scratch + Frameworks (Rahul Shetty Academy)
