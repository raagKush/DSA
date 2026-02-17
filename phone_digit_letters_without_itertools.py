# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 11:07:15 2026

@author: INAKUSHW
"""

def letter_combinations_visual(digits_str):
    if not digits_str:
        return []
    
    mapping = {
        "2": "abc","3": "def","4": "ghi","5": "jkl",
        "6": "mno","7": "pqrs","8": "tuv","9": "wxyz"
    }
    
    # Start with an empty combination
    combinations = [""]  
    print(f"Initial combinations: {combinations}\n")
    
    # Process each digit one by one
    for idx, digit in enumerate(digits_str):
        letters = mapping[digit]
        new_combinations = []
        print(f"Processing digit '{digit}' which maps to letters {list(letters)}")
        
        # Build new combinations by adding each letter to existing combos
        for combo in combinations:
            for letter in letters:
                new_combo = combo + letter
                new_combinations.append(new_combo)
                print(f" - Adding letter '{letter}' to '{combo}' -> '{new_combo}'")
        
        # Update combinations
        combinations = new_combinations
        print(f"Combinations after digit {idx+1} ('{digit}'): {combinations}\n")
    
    return combinations

# Example usage
result = letter_combinations_visual("23")
print("Final combinations:", result)
