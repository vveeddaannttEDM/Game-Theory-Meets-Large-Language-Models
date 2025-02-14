#!/usr/bin/env python3
"""
Simulation of competitive dynamics between LLMs and humans.
This script simulates a series of rounds where an LLM and a human
compete based on random performance metrics.
"""

import random

def simulate_competition(rounds=10):
    llm_score = 0
    human_score = 0
    for i in range(1, rounds+1):
        # Simulate performance scores for LLM and Human (values between 0 and 1)
        llm_performance = random.uniform(0, 1)
        human_performance = random.uniform(0, 1)
        
        # Determine the round winner.
        if llm_performance > human_performance:
            llm_score += 1
            winner = "LLM"
        elif human_performance > llm_performance:
            human_score += 1
            winner = "Human"
        else:
            winner = "Tie"
        print(f"Round {i}: LLM performance = {llm_performance:.3f}, Human performance = {human_performance:.3f} -> Winner: {winner}")
    
    print(f"Final Score: LLM = {llm_score}, Human = {human_score}")

def main():
    simulate_competition()

if __name__ == "__main__":
    main()
