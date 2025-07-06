# 📁 Test Results & Configurations

This folder contains the results and configuration files used during testing of the REST API test runner project.

---

## 🔧 Sample Scenario File (`example.yaml`)

This file defines the test steps executed during the validation run:

```yaml

```
# ---- scenarios/example.yaml ----
name: User login and fetch profile
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

---

## 🧪  Output Log 

```
�📄 Using scenario file: C:\Users\Lenovo\Documents\Internship_signi_5_sys\signi_rest_test_runner\scenarios\example.ya

�🚀 Executing step: Log
✅ Step 'Login' executed with status: 200
�🔧 Extracted 'token' = mocked-access-tok

�🚀 Executing step: Get Profile
✅ Step 'Get Profile' executed with status: 200
✅ Status code assertion passed
✅ Assertion passed: $.email = test@example.com
Validating step: Login
Validating step: Get Profile

---

## 📝 Summary

* ✅ Test scenario executed end-to-end with no failures


---




