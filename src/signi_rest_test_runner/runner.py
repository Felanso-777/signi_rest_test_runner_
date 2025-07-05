# ---- runner.py  ----
import sys
import os

from scenario_loader import load_scenario
from executor import execute_scenario
from validator import validate_scenario

if __name__ == '__main__':
   
    base_dir = os.path.dirname(os.path.abspath(__file__))

    
    default_path = os.path.join(base_dir, "..", "..", "scenarios", "example.yaml")
    scenario_path = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(default_path)

    print("📄 Using scenario file:", scenario_path)

    scenario = load_scenario(scenario_path)
    results = execute_scenario(scenario)
    validate_scenario(results)
