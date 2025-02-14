#!/usr/bin/env python3
"""
Modeling the societal impact of LLM-enabled interactions.
This simulation models how the introduction of LLM-generated content
affects the overall quality of human-generated content over time.
A simplistic dynamics model is used and the results are plotted.
"""

import matplotlib.pyplot as plt

def simulate_social_impact(rounds=20):
    human_quality = 50  # initial human content quality
    llm_influence = 0.1  # factor by which LLM presence reduces human quality
    quality_history = []
    
    for i in range(rounds):
        # For demonstration, assume human quality slightly decays each round.
        quality_change = -llm_influence * (human_quality / 100)
        human_quality += quality_change
        quality_history.append(human_quality)
        print(f"Round {i+1}: Human content quality = {human_quality:.2f}")
    
    # Plot the quality over rounds.
    plt.plot(range(1, rounds+1), quality_history, marker='o')
    plt.xlabel("Round")
    plt.ylabel("Human Content Quality")
    plt.title("Societal Impact Simulation: Human Content Quality Over Time")
    plt.grid(True)
    plt.show()

def main():
    simulate_social_impact()

if __name__ == "__main__":
    main()
