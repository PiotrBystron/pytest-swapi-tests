# Star Wars API Tests (SWAPI) — Pytest

Automated API tests for the **Star Wars API (SWAPI)** using **Pytest** and **Requests**.  
The SWAPI service is public, read-only, and supports only `GET` requests — perfect for practicing REST API test automation.

---

## Features

- Tests for multiple SWAPI endpoints:
  - `/people/{id}`
  - `/planets/{id}`
  - `/starships/{id}`
- Positive and negative test scenarios  
- Validation of:
  - status codes
  - response structure
  - response data
- Parametrized test cases  
- HTML reporting using `pytest-html`  

---

## Project structure

pytest-swapi-tests/
│── tests/
│ │── conftest.py
│ │── test_people_api.py
│ │── test_planets_api.py
│ └── test_starships_api.py
│
│── pytest.ini
│── README.md
└── requirements.txt

---

## How to run

### 1. Clone repository

```bash
git clone https://github.com/PiotrBystron/pytest-swapi-tests.git
```

```bash
cd pytest-swapi-tests
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the tests and generate an HTML test report

```bash
pytest --html=report.html --self-contained-html
```

A detailed report will be generated as report.html in the project folder.