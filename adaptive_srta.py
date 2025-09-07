# adaptive_srta.py
# Copyright 2025 Takayuki Takagi
# This is the main controller script for the Adaptive SRTA Cognitive Architecture.
# It uses a metacognitive agent to dynamically select the appropriate "thinking mode"
# based on the complexity of the problem.

# We will import the function from our metacognitive agent script.
# For this combined script to work, make sure `metacognitive_agent.py` is in the same folder.
from metacognitive_agent import calculate_complexity_score

# --- Placeholder functions for the different thinking modes ---
# These simulate calls to fibonacci_srta.py and dialectical_srta.py.
# This allows us to test the main controller logic independently.

def run_single_pass_evaluation(explanation):
    """
    Simulates a fast, single-pass evaluation for simple problems.
    This mode is for efficiency when deep thought is unnecessary.
    """
    print("\n>>> COMPLEXITY: LOW. Initiating Single-Pass Mode (Fast Evaluation)...")
    # In a real implementation, this would be a single call to the base agents.
    final_score = 7.1 # Simulate a quick, confident score
    print(f"--- Fast evaluation complete. Final Score: {final_score} ---")
    return final_score

def run_fibonacci_deliberation(explanation):
    """
    Simulates the introspective process from fibonacci_srta.py for
    moderately complex problems that require deeper thought.
    """
    print("\n>>> COMPLEXITY: MEDIUM. Initiating Introspective Mode (Fibonacci Deliberation)...")
    # This would call the logic from fibonacci_srta.py
    final_score = 6.8 # Simulate a well-considered, converged score
    print(f"--- Introspective process complete. Final Score: {final_score} ---")
    return final_score

def run_dialectical_deliberation(explanation):
    """
    Simulates the dialectical process from dialectical_srta.py for
    highly complex problems with conflicting viewpoints.
    """
    print("\n>>> COMPLEXITY: HIGH. Initiating Dialectical Mode (Dialectical Synthesis)...")
    # This would call the logic from dialectical_srta.py
    final_score = 6.5 # Simulate a synthesized, nuanced score
    print(f"--- Dialectical process complete. Final Score: {final_score} ---")
    return final_score

# --- Main Controller Logic ---

def adaptive_srta_controller(explanation_text):
    """
    The main "brain" of the system.
    1. Assesses complexity.
    2. Selects the appropriate thinking mode.
    3. Returns the final evaluation.
    """
    # Step 1: Use the metacognitive agent to assess the problem's complexity.
    complexity = calculate_complexity_score(explanation_text)

    # Step 2: Dynamically choose the thinking mode based on the complexity score.
    # We are adjusting these threshold values based on our test results.
    # これが調整後の、より賢くなった判断基準です。
    if complexity <= 2.0:  # 以前は 3.0 だった
        # If the problem is simple, don't waste resources.
        final_result = run_single_pass_evaluation(explanation_text)
    elif complexity <= 5.0: # 以前は 7.0 だった
        # If the problem is moderately complex, engage in self-reflection.
        final_result = run_fibonacci_deliberation(explanation_text)
    else: # complexity > 5.0
        # If the problem is highly complex and likely contains conflict,
        # engage in dialectical reasoning to find a creative synthesis.
        final_result = run_dialectical_deliberation(explanation_text)

    print("\n\n" + "="*20 + " ADAPTIVE SRTA FINAL CONCLUSION " + "="*20)
    print(f"After selecting the appropriate cognitive mode, the final evaluated score is: {final_result:.4f}")
    print("="*66)


# --- Example Usage ---
if __name__ == "__main__":
    # This sample explanation has internal conflict (logic is good, but expression is bad),
    # so we expect the metacognitive agent to rate its complexity as high.
    sample_explanation = "The model's logic is sound, but its verbose and jargon-heavy explanation makes it nearly incomprehensible to non-experts."
    
    # Run the main controller
    adaptive_srta_controller(sample_explanation)
