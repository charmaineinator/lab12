# Your code here
# Declare any desired classes to be used by LCSMatrix

class LCSMatrix:
    def __init__(self, str1, str2):
        self.row_count = len(str1)
        self.column_count = len(str2)
        # Your code here
    
    # Returns the number of columns in the matrix, which also equals the length
    # of the second string passed to the constructor.
    def get_column_count(self):
        return self.column_count
    
    # Returns the matrix entry at the specified row and column indices, or 0 if
    # either index is out of bounds.
    def get_entry(self, row_index, column_index):
        # Your code here (remove placeholder line below)
        return 0
    
    # Returns the number of rows in the matrix, which also equals the length
    # of the first string passed to the constructor.
    def get_row_count(self):
        return self.row_count
    
    # Returns the set of distinct, longest common subsequences between the two
    # strings that were passed to the constructor.
    def get_longest_common_subsequences(self):
        # Your code here (remove placeholder line below)
        return set()