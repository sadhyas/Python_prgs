import re

def isdate(string):
    # Define a pattern to match dates in the format dd/mm/yyyy
    pattern = r'\d{2}/\d{2}/\d{4}'  # This matches any date in the format 'dd/mm/yyyy'
    
    # Use re.search to find the pattern in the input string
    if re.search(pattern, string):
        return True
    else:
        return False

# Test the function
print(isdate('Today is 23/09/2023'))  # This should return True
print(isdate('Today is 24/09/2023'))  # This should return True because it contains a valid date '24/09/2023'
print(isdate('Today is 2023/09/23'))  # This should return False because it's not in the 'dd/mm/yyyy' format
