#!/usr/bin/python3
"""
A function to determine the fewest number of coins
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet the total."""
    if total <= 0:
        return 0
    
    # Create a list to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make a total of 0
    
    # Build the dp table
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
