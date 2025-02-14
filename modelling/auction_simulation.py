#!/usr/bin/env python3
"""
Auction mechanism simulation with incentive compatibility.
This script simulates a Vickrey auction where bidders submit bids.
The highest bidder wins but pays the second-highest bid.
"""

import random

def run_auction(bidders):
    """
    Run a Vickrey auction.
    - bidders: a dictionary mapping bidder names to their true valuations.
    Bidders submit a bid (simulated here with some noise around their valuation).
    """
    # Simulate bids (bid = true valuation modified by a random factor)
    bids = {bidder: random.uniform(0.5 * value, 1.5 * value) for bidder, value in bidders.items()}
    print("Bids:", bids)
    # Determine winner and second-highest bid.
    sorted_bidders = sorted(bids.items(), key=lambda x: x[1], reverse=True)
    winner, winning_bid = sorted_bidders[0]
    second_bid = sorted_bidders[1][1] if len(sorted_bidders) > 1 else 0
    print(f"Winner: {winner} with bid {winning_bid:.2f}, pays {second_bid:.2f}")
    return winner, winning_bid, second_bid

def main():
    # Define bidders and their true valuations.
    bidders = {
        "Alice": 100,
        "Bob": 80,
        "Charlie": 90
    }
    run_auction(bidders)

if __name__ == "__main__":
    main()
