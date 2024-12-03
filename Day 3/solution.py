import re

def extract_and_multiply(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        memory = file.read()
    
    # Regular expression to find valid mul(X,Y) instructions
    pattern = r'mul\((\d+),(\d+)\)'
    
    # Find all matches in the memory string
    matches = re.findall(pattern, memory)
    
    # Calculate the sum of the results of the multiplications
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

# Path to the input file
file_path = 'input.txt'

# Calculate the result
result = extract_and_multiply(file_path)
print("The sum of the results of the multiplications is:", result)
