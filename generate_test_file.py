import random
import string
import csv

def random_string(min_len=1, max_len=20):
    length = random.randint(min_len, max_len)
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_row():
    # 3 int columns
    ints = [random.randint(-10000, 10000) for _ in range(3)]
    # 3 float columns
    floats = [round(random.uniform(-10000, 10000), 4) for _ in range(3)]
    # 4 string columns
    strings = [random_string() for _ in range(4)]
    # Combine all columns
    return ints + floats + strings

def main():
    with open("test_generated.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for _ in range(500):
            writer.writerow(generate_row())

if __name__ == "__main__":
    main()