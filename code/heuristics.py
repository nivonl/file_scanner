import re
import pandas as pd

# Define individual rule functions

def contains_credit_card(column):
    # Regex pattern to match credit card numbers with 13 to 16 digits, 
    # allowing spaces or hyphens between digits.
    credit_card_pattern = re.compile(r'\b(?:\d[ -]*?){13,16}\b')
    
    # Apply the pattern to the column and return True if the pattern is found.
    return column.apply(lambda x: bool(credit_card_pattern.match(str(x))))

def contains_mbi(column):
    # Regex pattern to match Medicare Beneficiary Identifier (MBI) which consists 
    # of 11 characters including letters (A-Z ,without S, L, O, I, B, and Z) and digits (0-9), and enabaling up to 2 dashes
    mbi_pattern = re.compile(r'^(?=(?:[^-]*-){0,2}[^-]*$)[AC-HJ-MN-RT-Y0-9-]{11}$')
    
    # Apply the pattern to the column and return True if the pattern is found.
    return column.apply(lambda x: bool(mbi_pattern.match(str(x))))

# Define Heuristics Dictionary
heuristics_dict = {
    "Credit Card Number": contains_credit_card,
    "Medicare Beneficiary Identifier": contains_mbi
}
