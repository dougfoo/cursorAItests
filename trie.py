'''
Trie is a tree-like data structure that stores a dynamic set of strings.
It is used to store a dictionary of words, and to check if a word exists in the dictionary.
It is also used to check if a prefix of a word exists in the dictionary.

Example Trie storing "app", "apple", "ban", "banana":

         root
       /     \\
      a       b
     /         \\
    p           a
   / \           \\
  p   p           n
  *   l           *
     e             a
     *             n
                   a
                   *
* denotes end of word
'''

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end = False  # Flag to mark end of word

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """Insert a word into the trie.
        
        Traverses the trie character by character, creating new nodes as needed.
        For each character in the word:
        - If the character doesn't exist as a child of current node, create new TrieNode
        - Move to the child node for that character
        Finally marks the last node as end of word.
        
        Args:
            word: The string to insert into the trie
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def searchr(self, cur_node, word: str) -> bool:
        """Recursively search for a word in the trie starting from given node.
        
        Time Complexity: O(m) where m is length of word being searched
        - Each recursive call processes one character
        - Maximum recursion depth is length of word
        - Each character comparison and dictionary lookup is O(1)
        
        Space Complexity: O(m) where m is length of word being searched
        - Each recursive call adds one frame to call stack
        - Maximum call stack depth is length of word
        - No additional data structures used beyond call stack
        
        Args:
            cur_node: Current TrieNode in traversal
            word: Remaining substring to search for
        Returns:
            bool: True if word exists in trie, False otherwise
        """
        if len(word) == 0 and cur_node.is_end is True:
            return True
        elif len(word) == 0 or cur_node.children is None:
            return False
        elif word[0] not in cur_node.children:
            return False
        else:
            # handle app and apple where 'app' is intermediate non-end word 
            return self.searchr(cur_node.children[word[0]], word[1:])

    def search(self, word: str) -> bool:
        """Search for a complete word in the trie.
        
        Time Complexity: O(m) where m is length of word being searched
        - Iterates through each character in word once
        - Dictionary lookups are O(1)
        
        Space Complexity: O(1)
        - Only uses a single node reference variable
        - No additional data structures created
        
        Args:
            word: The string to search for in the trie
        Returns:
            bool: True if word exists in trie, False otherwise
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def startsWith(self, prefix: str) -> bool:
        """Check if any word in the trie starts with the given prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def __str__(self):
        """String representation of the trie for debugging"""
        def helper(node, prefix):
            result = []
            if node.is_end:
                result.append(prefix)
            for char, child in node.children.items():
                result.extend(helper(child, prefix + char))
            return result
        return str(helper(self.root, ""))

def main():
    # Example usage
    trie = Trie()
    
    # Insert words
    words = ["apple", "app", "application", "banana", "ball"]
    for word in words:
        trie.insert(word)
    
    # Search for words
    print("Search results:")
    test_words = ['app', 'apple', 'appl', 'ban', 'banana']
    print("\nComparing search() and searchr():")
    for word in test_words:
        print(f"Word: '{word}'")
        print(f"  search(): {trie.search(word)}")
        print(f"  searchr(): {trie.searchr(trie.root, word)}")
    
    # Check prefixes
    print("\nPrefix checks:")
    print(f"Starts with 'app': {trie.startsWith('app')}")  # True
    print(f"Starts with 'ban': {trie.startsWith('ban')}")  # True
    print(f"Starts with 'cat': {trie.startsWith('cat')}")  # False
    
    # Print all words in trie
    print("\nAll words in trie:")
    print(trie)

if __name__ == "__main__":
    main() 