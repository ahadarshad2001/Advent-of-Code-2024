MOD = 16777216  # A large prime-like modulus to keep numbers within range

def next_secret_number(secret):
    """
    Calculate the next secret number using the three-step pseudorandom procedure.
    """
    # --- Step 1 ---
    multiplied = secret * 64
    secret ^= multiplied  # XOR with the current value
    secret %= MOD         # Modulo operation to wrap around

    # --- Step 2 ---
    divided = secret // 32
    secret ^= divided      # XOR with divided value
    secret %= MOD          # Modulo operation

    # --- Step 3 ---
    multiplied = secret * 2048
    secret ^= multiplied  # XOR with multiplied value
    secret %= MOD         # Modulo operation

    return secret

def get_price_arrays(buyers):
    """
    Generate 2001 secret numbers for each buyer and extract prices (last digit).
    """
    all_prices = []
    for initial_secret in buyers:
        secrets = [initial_secret]
        s = initial_secret
        # Generate 2000 more secret numbers
        for _ in range(2000):
            s = next_secret_number(s)
            secrets.append(s)
        prices = [x % 10 for x in secrets]  # Extract last digit
        all_prices.append(prices)
    return all_prices

def solve_part_two(filename='input.txt'):
    """
    Main function to process input, find patterns, and calculate the best sum of bananas.
    """
    # Step 1: Read buyers' initial secrets
    buyers = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                buyers.append(int(line))

    # Step 2: Generate prices for each buyer
    all_prices = get_price_arrays(buyers)

    # Step 3: Initialize a pattern dictionary to track patterns and buyer results
    from collections import defaultdict
    pattern_dict = defaultdict(lambda: [0] * len(buyers))

    # Step 4: Process each buyer's price data
    for b_idx, prices in enumerate(all_prices):
        changes = []
        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            changes.append(diff)

        # Identify patterns of 4 consecutive changes
        for i in range(len(changes) - 3):
            c1, c2, c3, c4 = changes[i], changes[i + 1], changes[i + 2], changes[i + 3]
            pattern = (c1, c2, c3, c4)

            if pattern_dict[pattern][b_idx] == 0:  # Record the earliest occurrence
                sell_price = prices[i + 4]  # The price after the 4th change
                pattern_dict[pattern][b_idx] = sell_price

    # Step 5: Calculate the best pattern sum
    best_sum = 0
    for pattern, buyer_sells in pattern_dict.items():
        total_for_pattern = sum(buyer_sells)
        if total_for_pattern > best_sum:
            best_sum = total_for_pattern

    return best_sum

if __name__ == "__main__":
    # Run the solver and print the result
    answer = solve_part_two("input.txt")
    print(answer)
