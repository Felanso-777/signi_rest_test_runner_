# signi_rest_test_runner
# API Test Runner Framework

This is a simple Python-based tool for testing REST APIs using scenario files written in YAML. It also includes a sample API server for demonstration.

---

## Project Structure

```
INTERNSHIP_SIGNI_5_SYS/
├── signi_rest_test_runner/
│   ├── sample_api/
│   │   ├── main.py
│   │   ├── requirements.txt
│   ├── scenarios/
│   │   └── example.yaml
│   └── src/
│       └── signi_rest_test_runner/      
│           ├── executor.py
│           ├── runner.py
│           ├── scenario_loader.py
│           ├── utils.py
│           └── validator.py
├── test_results/
│   └── test_results.md                     ← ✅ test outputs & config
├── findings.md                             ← ✅ code analysis & comparison
├── ai_usage.md                             ← ✅ AI usage disclosure
├── README.md                               ← ✅ updated with all info
├── pyproject.toml
├── poetry.toml

---

## Requirements

* Python 3.9 or higher
* Install dependencies:

```bash
pip install -r sample_api/requirements.txt
```

---

## How to Use

### 1. Start the Sample API

```bash

uvicorn main:app --reload
```

### 2. Run the Scenario

```bash
python runner.py
```

You can also specify your own YAML file:

```bash
python runner.py path/to/custom.yaml
```

---

## Scenario Format (YAML)

Each scenario has multiple steps:

```yaml
steps:
  - name: Login
    request:
      method: POST
      url: "http://127.0.0.1:8000/login"
      body:
        email: "test@example.com"
        password: "secret"
    extract:
      token: "$.access_token"

  - name: Get Profile
    request:
      method: GET
      url: "http://127.0.0.1:8000/profile"
      headers:
        Authorization: "Bearer {{ token }}"
    assert:
      status_code: 200
      $.email: "test@example.com"
```

---

## Notes

* Test responses must be JSON
* Assertions only support simple JSONPath and status codes
* Does not support retries or parallel steps yet

---

## Suggestions to Improve

* Add better error messages
* Support timeouts, retries, and loops
* Add a test report or summary at the end

---

## AI Usage

This project used ChatGPT (OpenAI) for help with:

* Refactoring and comparing code
* Improving logic for assertions and variable extraction
* Generating commit messages, findings.md, and this README.md

See [ai\_usage.md](ai_usage.md) for details.

---

