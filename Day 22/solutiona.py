# Function to compute the next secret number
def next_secret_number(secret):
    for _ in range(2000):
        # Step 1: Multiply by 64, mix, and prune
        secret ^= (secret * 64) % 16777216

        # Step 2: Divide by 32 (floor), mix, and prune
        secret ^= (secret // 32) % 16777216

        # Step 3: Multiply by 2048, mix, and prune
        secret ^= (secret * 2048) % 16777216

        # Prune the secret number
        secret %= 16777216

    return secret

# Read input from the file
with open("input.txt", "r") as file:
    initial_secrets = [int(line.strip()) for line in file]

# Compute the 2000th secret number for each buyer and sum them up
result = sum(next_secret_number(secret) for secret in initial_secrets)

# Output the result
print(result)
