#!/usr/bin/env python3
"""
Benchmark runner for game-based simulations.
This script runs both the matrix game simulation and the communication game simulation.
It calls the individual simulation scripts as subprocesses.
"""

import subprocess
import sys

def run_matrix_game():
    print("Running Matrix Game Simulation:")
    subprocess.run([sys.executable, "evaluation/matrix_game.py"])

def run_communication_game():
    print("\nRunning Communication Game Simulation:")
    subprocess.run([sys.executable, "evaluation/communication_game.py"])

def main():
    run_matrix_game()
    run_communication_game()

if __name__ == "__main__":
    main()
