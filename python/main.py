from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                     roof_width: int, roof_height: int) -> int:
    
    if any(d <= 0 for d in (panel_width, panel_height, roof_width, roof_height)):
        return 0
    
    panels_a = (roof_width // panel_width) * (roof_height // panel_height) + ((roof_width % panel_width) // panel_height) * (roof_height // panel_width)
    panels_b = (roof_width // panel_height) * (roof_height // panel_width) + ((roof_width % panel_height) // panel_width) * (roof_height // panel_height)

    panels_c = (roof_height // panel_width) * (roof_width // panel_height) + ((roof_height % panel_width) // panel_height) * (roof_width // panel_width)
    panels_d = (roof_height // panel_height) * (roof_width // panel_width) + ((roof_height % panel_height) // panel_width) * (roof_width // panel_height)

    return max(panels_a, panels_b, panels_c, panels_d)


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
