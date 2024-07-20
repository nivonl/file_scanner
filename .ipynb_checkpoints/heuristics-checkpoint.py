import re
import pandas as pd

# Define individual rule functions
def contains_credit_card(column):
    credit_card_pattern = re.compile(r'\b(?:\d[ -]*?){13,16}\b')
    return column.apply(lambda x: bool(credit_card_pattern.match(str(x))))

def contains_special_characters(column):
    special_char_pattern = re.compile(r'[^\w\s-]')
    return column.apply(lambda x: bool(special_char_pattern.search(str(x))))

def contains_mbi(column):
    mbi_pattern = re.compile(r'^[A-HJ-NP-Z0-9]{11}$')
    return column.apply(lambda x: bool(mbi_pattern.match(str(x))))

# Define Heuristics Dictionary
heuristics_dict = {
    "Credit Card Number": contains_credit_card,
    "Medicare Beneficiary Identifier": contains_mbi
}
