#!/usr/bin/env python3
"""
Simulation of a communication-based game.
In this signaling game:
- The Sender has a type (0 or 1) and sends a signal (with some noise).
- The Receiver observes the signal and chooses an action.
- Both receive a positive payoff if the Receiver's action matches the Sender's true type.
"""

import random

def sender_strategy(sender_type):
    """
    Sender sends a signal based on their type.
    With probability p, the Sender transmits the true type; otherwise, the signal is flipped.
    """
    p = 0.8  # probability of sending the true type
    if random.random() < p:
        return sender_type
    else:
        return 1 - sender_type

def receiver_strategy(signal):
    """
    Receiver's strategy: trusts the received signal.
    """
    return signal

def simulate_round():
    # Randomly assign the Sender's type.
    sender_type = random.choice([0, 1])
    signal = sender_strategy(sender_type)
    receiver_action = receiver_strategy(signal)
    
    # Payoff: if the Receiver's action matches the Sender's type, both get 2; otherwise, 0.
    if receiver_action == sender_type:
        payoff_sender = 2
        payoff_receiver = 2
    else:
        payoff_sender = 0
        payoff_receiver = 0
    return sender_type, signal, receiver_action, payoff_sender, payoff_receiver

def run_simulation(rounds=10):
    total_sender = 0
    total_receiver = 0
    for i in range(1, rounds+1):
        sender_type, signal, receiver_action, ps, pr = simulate_round()
        total_sender += ps
        total_receiver += pr
        print(f"Round {i}: Sender type: {sender_type}, Signal: {signal}, Receiver action: {receiver_action} -> Payoffs: Sender = {ps}, Receiver = {pr}")
    print(f"Total payoff: Sender = {total_sender}, Receiver = {total_receiver}")

if __name__ == "__main__":
    run_simulation()
