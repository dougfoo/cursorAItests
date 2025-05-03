from collections import Counter
from heapq import heappush, heappop, heapify

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # Count frequency of each character
    freq = Counter(text)
    
    # Create priority queue of nodes
    heap = []
    for char, count in freq.items():
        heappush(heap, Node(char, count))
        
    # Build tree by combining nodes
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        
        internal = Node(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        
        heappush(heap, internal)
        
    return heap[0]

def build_codes(root, code="", mapping=None):
    if mapping is None:
        mapping = {}
        
    if root is None:
        return
        
    if root.char is not None:
        mapping[root.char] = code
        return

    build_codes(root.left, code + "0", mapping)
    build_codes(root.right, code + "1", mapping)
    
    return mapping

def huffman_encode(text):
    """
    Encodes text using Huffman coding and returns encoded string
    """
    # Handle empty string
    if not text:
        return ""
        
    # Build Huffman tree
    root = build_huffman_tree(text)
    
    # Generate codes for each character
    codes = build_codes(root)
    
    # Encode text
    encoded = ""
    for char in text:
        encoded += codes[char]
        
    return encoded

def huffman_decode(encoded, root):
    """
    Decodes Huffman-encoded string using the Huffman tree
    """
    if not encoded:
        return ""
        
    decoded = ""
    current = root
    
    for bit in encoded:
        if bit == "0":
            current = current.left
        else:
            current = current.right
            
        if current.char is not None:
            decoded += current.char
            current = root
            
    return decoded

def main():
    # Test sentence
    test_text = "hello world my hell is the bell"
    print(f"Original text: {test_text}")
    
    # Encode the text
    encoded = huffman_encode(test_text)
    print(f"Huffman encoded: {encoded}")
    
    # Build tree for decoding
    root = build_huffman_tree(test_text)
    
    # Decode back to original
    decoded = huffman_decode(encoded, root)
    print(f"Decoded text: {decoded}")

if __name__ == "__main__":
    main()
