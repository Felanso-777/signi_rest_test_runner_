# 📁 Test Results & Configurations

This folder contains the results and configuration files used during testing of the REST API test runner project.

---

## 🔧 Sample Scenario File (`example.yaml`)

This file defines the test steps executed during the validation run:

```yaml
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
```

---

## 🧪 Sample Output Log (`output_log.txt`)

```
📄 Using scenario file: scenarios/example.yaml
🚀 Executing step: Login
✅ Step 'Login' executed with status: 200
🔧 Extracted 'token' = mocked-access-token
🚀 Executing step: Get Profile
✅ Step 'Get Profile' executed with status: 200
✅ Status code assertion passed
✅ Assertion passed: $.email = test@example.com
```

---

## 📝 Summary

* ✅ Test scenario executed end-to-end with no failures
* 🔑 Access token successfully extracted and reused
* 📥 Profile details validated using JSONPath assertion

---

## 📎 Files to Include in This Folder

* `test_results.md` — This summary file ✅
* `example.yaml` — The scenario used for testing
* `output_log.txt` — Terminal log of the run (optional)
* `screenshot_result.png` — (Optional) screenshot showing success in terminal or browser

---

> These results demonstrate the system's ability to run test scenarios, extract and use tokens, and validate responses.
