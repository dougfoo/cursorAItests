import re

def load_file_to_array(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return [line.rstrip('\n') for line in lines]

def split_string_to_words(s):
    return s.split()
    
def split_string_custom(s):
    return re.split(r'[ ,./-]+', s.strip())

def main():
    print("hello world")

if __name__ == "__main__":
    main()
    
