# ---- executor.py ----
import httpx
from utils import render_template, extract_variables, apply_assertions

# Shared context for variable extraction
context = {}

def execute_step(step: dict) -> dict:
    step_name = step['name']
    print(f"\n🚀 Executing step: {step_name}")

    # Render request
    request = render_template(step['request'], context)
    method = request['method'].upper()
    url = request['url']
    headers = request.get('headers', {})
    body = request.get('body')

    # Execute HTTP request
    with httpx.Client() as client:
        response = client.request(
            method=method,
            url=url,
            headers=headers,
            json=body
        )

    print(f"✅ Step '{step_name}' executed with status: {response.status_code}")

    # Extract variables (if any)
    if 'extract' in step:
        extract_variables(response, step['extract'], context)

    # Assert conditions (if any)
    if 'assert' in step:
        apply_assertions(response, step['assert'], context)

    return {
        'step': step_name,
        'request': request,
        'response': {
            'status_code': response.status_code,
            'json': response.json()
        }
    }

def execute_scenario(scenario: dict) -> list:
    return [execute_step(step) for step in scenario['steps']]
