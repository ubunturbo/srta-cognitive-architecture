# metacognitive_agent.py
# Copyright 2025 Takayuki Takagi
# This script implements a metacognitive agent that assesses the complexity
# of a given explanation before deep deliberation begins.

import json
import time
import statistics

# --- Mock LLM API ---
# This function simulates calls to a real LLM for the three base agents.
def mock_llm_call_single_pass(prompt, agent_role):
    """Mocks a single-pass evaluation call for initial assessment."""
    print(f". Bouncing idea off {agent_role}...")
    time.sleep(0.5)

    # Simulate different base scores to create variance for testing
    if "Principle" in agent_role:
        score = 7.5
    elif "Expression" in agent_role:
        score = 6.0
    else: # Audit
        score = 5.5

    return {"overall": score, "reasoning": f"Initial thought from {agent_role}."}

# --- Metacognitive Logic ---

def calculate_complexity_score(explanation_text):
    """
    Assesses the complexity of an explanation by measuring the variance
    in scores from an initial, single-pass evaluation by three agents.
    """
    print("=== Running Metacognitive Assessment ===")
    print(f"Analyzing explanation: '{explanation_text[:50]}...'")

    agents = ["Principle Agent", "Expression Agent", "Audit Agent"]
    scores = []

    # 1. Get initial, single-pass evaluations from all agents
    for agent in agents:
        # The prompt for this phase is simple and identical for all agents
        prompt = f"Initial evaluation request for {agent} on the text."
        evaluation = mock_llm_call_single_pass(prompt, agent)
        scores.append(evaluation['overall'])

    print(f"\nInitial scores received: {scores}")

    # 2. Calculate the variance of the scores
    # A high variance indicates disagreement and thus higher complexity.
    if len(scores) < 2:
        variance = 0
    else:
        variance = statistics.variance(scores)

    # 3. Map the variance to a 1-10 complexity score
    # This mapping function can be tuned based on experimental results.
    # For this simulation, we'll use a simple linear mapping.
    # A variance of 2.0 or more will map to the max complexity of 10.
    complexity_score = min(10, 1 + (variance * 4.5))

    print(f"Score Variance: {variance:.4f}")
    print("========================================")
    print(f"COMPLEXITY SCORE: {complexity_score:.2f} / 10")
    print("========================================")

    return complexity_score

# --- Example Usage ---
if __name__ == "__main__":
    # This is a sample explanation that might cause disagreement among agents
    sample_explanation = "The model's logic is sound, but its verbose and jargon-heavy explanation makes it nearly incomprehensible to non-experts."
    
    # Run the metacognitive assessment to get the complexity score
    calculate_complexity_score(sample_explanation)

