import re

def extract_and_multiply(file_path):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            memory = file.read()
        
        # Regular expressions to find valid mul(X,Y), do(), and don't() instructions
        mul_pattern = r'mul\((\d+),(\d+)\)'
        do_pattern = r'do\(\)'
        dont_pattern = r"don't\(\)"
        
        # Initialize variables
        total_sum = 0
        mul_enabled = True
        
        # Split the memory into tokens based on the patterns
        tokens = re.split(f'({mul_pattern}|{do_pattern}|{dont_pattern})', memory)
        
        # Process each token
        for token in tokens:
            if token is None:
                continue
            if re.match(mul_pattern, token):
                if mul_enabled:
                    x, y = re.findall(r'\d+', token)
                    total_sum += int(x) * int(y)
            elif re.match(do_pattern, token):
                mul_enabled = True
            elif re.match(dont_pattern, token):
                mul_enabled = False
        
        return total_sum
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Path to the input file
file_path = 'inputb.txt'

# Calculate the result
result = extract_and_multiply(file_path)
if result is not None:
    print("The sum of the results of the enabled multiplications is:", result)
else:
    print("An error occurred while processing the file.")
