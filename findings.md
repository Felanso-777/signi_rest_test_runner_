# 🧾 Code Comparison Findings

This document summarizes the differences between correct and incorrect implementations for four key files in the test runner framework.

---

## ✅ `executor.py`

### ❌ Issue in incorrect code:

* No use of shared `context` for rendering dynamic data (headers/body).
* Rendering logic was hardcoded into `executor.py`, making the file less modular.
* No support for response assertions like status code or response field validation.

### ✅ Fixes in correct code:

* Delegated logic to external utility functions: `render_template`, `extract_variables`, `apply_assertions`.
* Introduced a shared `context` dictionary to pass values between steps.
* Added comprehensive response validation using JSONPath and status code assertions.

---

## ✅ `runner.py`

### ❌ Issue in incorrect code:

* Hardcoded import paths like `src.signi_rest_test_runner.*`, which require the module to be installed or added to `PYTHONPATH`.
* Scenario file was assumed to be in the current directory.

### ✅ Fixes in correct code:

* Dynamically resolved the path to `example.yaml` using `os.path`.
* Supports running from any location without altering `PYTHONPATH`.

---

## ✅ `utils.py`

### ❌ Issue in incorrect code:

* `render_template` supported only simple string rendering — could not handle nested dictionaries or lists.
* Less logging and error feedback during assertion or extraction failures.

### ✅ Fixes in correct code:

* Made `render_template` recursive to handle nested templates in dicts and lists.
* Added useful logs and warnings when variable extraction or assertions fail.

---

## ✅ `example.yaml`

### ❌ Issue in incorrect code:

* API URLs pointed to external URLs (`https://api.example.com`) instead of the locally hosted mock API.
* Incorrect `assert` structure: wrapped response body under `body:` key instead of using JSONPath.

### ✅ Fixes in correct code:

* URLs replaced with `http://127.0.0.1:8000` to work with the local `FastAPI` server.
* Assertions now use JSONPath directly (e.g., `$.email`) for accurate response validation.

---

## 🛠 Summary of Fixes

| File         | Fix Type                 | Description                                  |
| ------------ | ------------------------ | -------------------------------------------- |
| executor.py  | Refactor, modularization | Separated logic, added response assertions   |
| runner.py    | Path handling            | Removed hardcoded imports and added fallback |
| utils.py     | Function improvements    | Recursive rendering and better logging       |
| example.yaml | URL and assert fix       | Corrected URL targets and validation syntax  |

---

