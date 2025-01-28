#!/usr/bin/python3
"""
A function to determine the fewest number of coins
"""


from collections import deque

def makeChange(coins, total):
    """Find the fewest number of coins needed to make the total."""
    if total <= 0:
        return 0

    # BFS setup
    queue = deque([(0, 0)])  # (current amount, number of coins used)
    visited = set()  # To avoid processing the same amount multiple times

    while queue:
        amount, steps = queue.popleft()
        
        # Check each coin
        for coin in coins:
            next_amount = amount + coin
            
            if next_amount == total:
                return steps + 1  # Reached the target amount
            if next_amount > total or next_amount in visited:
                continue  # Skip invalid or already-visited states
            
            visited.add(next_amount)
            queue.append((next_amount, steps + 1))
    
    return -1  # Not possible to reach the total
