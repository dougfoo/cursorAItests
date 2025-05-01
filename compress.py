import random
"""
Run-Length Encoding Compression Program

This program implements a basic run-length encoding compression algorithm.
It works by:
1. Reading a sample text file containing a sequence of repeated characters
2. Counting consecutive occurrences of each character
3. Outputting compressed data in the format "char:count,char:count,..."

The program includes:
- generate_sample_file(): Creates a test file with random repeated characters
- read_chars(): Helper function to count consecutive character occurrences
- Main logic to process the file and output compressed format

Example input: AAABBC
Example output: A:3,B:2,C:1,
"""

def generate_sample_file():
    # Create list of possible characters (A-Z and 0-9)
    chars = [chr(i) for i in range(65, 91)]  # A-Z
    nums = [str(i) for i in range(10)]       # 0-9
    all_chars = chars + nums
    
    # Generate sequence with random characters that can repeat up to 10 times
    result = ''
    while len(result) < 80:
        # Select a random character
        char = random.choice(all_chars)
        # Randomly choose how many times to repeat it (1-10)
        repeat = random.randint(0, 10)
        # Add the repeated character to result
        result += char * repeat
    
    # Truncate to exactly 80 chars
    result = result[:80]
    
    # Write to file
    with open('sample.txt', 'w') as f:
        f.write(result)

def read_chars(chars):
    if not chars:  # Check if list is empty
        return None
    c = chars.pop(0)
    count = 1  # Start with 1 since we already popped one
    while chars and chars[0] == c:  # Check if list is not empty before accessing
        count += 1
        chars.pop(0)
    return (c, count)

def process_chars(chars, delimiter=','):
        buf = ""
        while chars:  # While there are still characters to process
            result = read_chars(chars)
            if result:
                c, count = result
                # print(f"{c} {count}")
                buf += f"{c}:{count}{delimiter}"
        return buf

if __name__ == '__main__':
    # Read sample.txt into array of characters
    with open('sample.txt', 'r') as f:
        chars = list(f.read().strip())    

    buf = process_chars(chars, "*")

    print(buf)

