# test_harness.py
# Copyright 2025 Takayuki Takagi
# This script serves as the test harness for the Adaptive SRTA Cognitive Architecture.
# It runs a series of predefined test cases with varying complexities to validate
# that the main controller (`adaptive_srta.py`) selects the appropriate thinking mode.

# Import the main controller function we want to test
from adaptive_srta import adaptive_srta_controller
# We also need to import the metacognitive agent to run the controller
# Make sure metacognitive_agent.py is in the same folder.
import metacognitive_agent

print("="*25)
print("INITIALIZING TEST HARNESS")
print("="*25)

# --- Test Cases ---
# We define a list of test explanations, each with an expected complexity level.
# This allows us to verify if the system's metacognition is working correctly.

test_cases = [
    {
        "id": "Test Case 1: Simple & Clear",
        "explanation": "The model chose 'cat' because the image contained a cat.",
        "expected_complexity": "LOW",
        "notes": "A straightforward, factual statement. Should trigger fast, single-pass evaluation."
    },
    {
        "id": "Test Case 2: Moderately Complex",
        "explanation": "While the linear regression model is simple, its feature interactions suggest a non-obvious quadratic relationship that requires careful interpretation.",
        "expected_complexity": "MEDIUM",
        "notes": "Contains some nuance and requires deeper thought. Should trigger introspective (Fibonacci) mode."
    },
    {
        "id": "Test Case 3: High Conflict / Ambiguity",
        "explanation": "The model's logic is sound, but its verbose and jargon-heavy explanation makes it nearly incomprehensible to non-experts.",
        "expected_complexity": "HIGH",
        "notes": "Contains a direct conflict between logical soundness and expressive clarity. Should trigger dialectical mode."
    }
]

# --- Test Execution Loop ---

for i, test in enumerate(test_cases):
    print(f"\n\n--- RUNNING {test['id']} ---")
    print(f"Notes: {test['notes']}")
    print(f"Expected Complexity Category: {test['expected_complexity']}")
    print("-"*(len(test['id']) + 14))

    # To make the simulation work for our test cases, we need to adjust the mock LLM
    # in the metacognitive agent to produce different variances for each case.
    if test['expected_complexity'] == "LOW":
        # Simulate low variance (high agreement)
        metacognitive_agent.mock_llm_call_single_pass = lambda p, r: {"overall": 7.0}
    elif test['expected_complexity'] == "MEDIUM":
        # Simulate medium variance
        def medium_variance_mock(prompt, role):
            if "Principle" in role: return {"overall": 7.0}
            if "Expression" in role: return {"overall": 6.5}
            return {"overall": 6.0}
        metacognitive_agent.mock_llm_call_single_pass = medium_variance_mock
    else: # HIGH
        # Simulate high variance (strong disagreement)
        def high_variance_mock(prompt, role):
            if "Principle" in role: return {"overall": 7.5}
            if "Expression" in role: return {"overall": 6.0}
            return {"overall": 5.5}
        metacognitive_agent.mock_llm_call_single_pass = high_variance_mock


    # Run the main controller with the test explanation
    adaptive_srta_controller(test["explanation"])
    print(f"--- TEST CASE {i+1} COMPLETE ---")

print("\n\n" + "="*28)
print("ALL TEST CASES COMPLETED.")
print("="*28)
