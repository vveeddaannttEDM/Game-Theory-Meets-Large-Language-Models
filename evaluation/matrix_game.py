#!/usr/bin/env python3
"""
Simulation of 2x2 matrix games.
This script simulates a repeated 2x2 game between two players.
Player A and Player B have two strategies (0 and 1).
Payoffs are defined for each outcome.
"""

import random

def simulate_round(strategy_a, strategy_b, payoff_matrix):
    """
    Simulate a round of a matrix game.
    - strategy_a, strategy_b: integers 0 or 1.
    - payoff_matrix: tuple of two 2x2 lists (for Player A and Player B).
    Returns the payoffs for Player A and Player B.
    """
    payoff_a = payoff_matrix[0][strategy_a][strategy_b]
    payoff_b = payoff_matrix[1][strategy_a][strategy_b]
    return payoff_a, payoff_b

def best_response(player, opponent_strategy, payoff_matrix):
    """
    Compute the best response for a given player given the opponent's strategy.
    'player' is 0 (Player A) or 1 (Player B).
    Returns the best strategy and its payoff.
    """
    best_payoff = None
    best_strategy = None
    for strategy in [0, 1]:
        if player == 0:
            payoff = payoff_matrix[0][strategy][opponent_strategy]
        else:
            payoff = payoff_matrix[1][opponent_strategy][strategy]
        if best_payoff is None or payoff > best_payoff:
            best_payoff = payoff
            best_strategy = strategy
    return best_strategy, best_payoff

def run_simulation(rounds=10):
    # Define a simple Prisoner's Dilemma-like payoff matrix.
    # Strategies: 0 = Cooperate, 1 = Defect
    # Payoffs for Player A and B respectively.
    payoff_a = [
        [3, 0],  # If A cooperates: (3 if B cooperates, 0 if B defects)
        [5, 1]   # If A defects: (5 if B cooperates, 1 if B defects)
    ]
    payoff_b = [
        [3, 5],  # If B cooperates: (3 if A cooperates, 5 if A defects)
        [0, 1]   # If B defects: (0 if A cooperates, 1 if A defects)
    ]
    payoff_matrix = (payoff_a, payoff_b)
    
    # Start with random initial strategies.
    strategy_a = random.choice([0, 1])
    strategy_b = random.choice([0, 1])
    
    print("Starting strategies: Player A: {}, Player B: {}".format(strategy_a, strategy_b))
    
    total_payoff_a = 0
    total_payoff_b = 0
    
    for round in range(1, rounds+1):
        pa, pb = simulate_round(strategy_a, strategy_b, payoff_matrix)
        total_payoff_a += pa
        total_payoff_b += pb
        print(f"Round {round}: Player A chose {strategy_a}, Player B chose {strategy_b} -> Payoffs: A = {pa}, B = {pb}")
        
        # Each player adjusts their strategy based on a best response.
        best_a, _ = best_response(0, strategy_b, payoff_matrix)
        best_b, _ = best_response(1, strategy_a, payoff_matrix)
        strategy_a = best_a
        strategy_b = best_b
    
    print("Total Payoff: Player A = {}, Player B = {}".format(total_payoff_a, total_payoff_b))

if __name__ == "__main__":
    run_simulation()
