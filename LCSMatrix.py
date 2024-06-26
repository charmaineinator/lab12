class LCSMatrix:
    def __init__(self, string1, string2):
        self.string1 = string1  # Initialize string1
        self.string2 = string2  # Initialize string2
        self.row_count = len(string1)
        self.column_count = len(string2)
        self.matrix_data = [[0] * (self.column_count + 1) for _ in range(self.row_count + 1)]
        
        for i in range(1, self.row_count + 1):
            for j in range(1, self.column_count + 1):
                if string1[i - 1] == string2[j - 1]:
                    self.matrix_data[i][j] = 1 + self.matrix_data[i - 1][j - 1]
                else:
                    self.matrix_data[i][j] = max(self.matrix_data[i - 1][j], self.matrix_data[i][j - 1])
    
    # Returns the number of columns in the matrix, which also equals the length
    # of the second string passed to the constructor.
    def get_column_count(self):
        return self.column_count
    
    # Returns the matrix entry at the specified row and column indices, or 0 if
    # either index is out of bounds.
    def get_entry(self, row_index, column_index):
        if 0 <= row_index <= self.row_count and 0 <= column_index <= self.column_count:
            return self.matrix_data[row_index][column_index]
        else:
            return 0
    
    # Returns the number of rows in the matrix, which also equals the length
    # of the first string passed to the constructor.
    def get_row_count(self):
        return self.row_count
    
    # Returns the set of distinct, longest common subsequences between the two
    # strings that were passed to the constructor.
    def get_longest_common_subsequences(self):
        # Check if there is no common subsequence
        if self.matrix_data[self.row_count][self.column_count] == 0:
            return set()  # No common subsequences
        
        result = set()
        self._find_lcs(self.row_count, self.column_count, "", result)
        return result
    
    def _find_lcs(self, i, j, current_str, result):
        if i == 0 or j == 0:
            result.add(current_str[::-1])
            return
    
        if self.string1[i - 1] == self.string2[j - 1]:
            self._find_lcs(i - 1, j - 1, current_str + self.string1[i - 1], result)
        else:
            if self.matrix_data[i - 1][j] == self.matrix_data[i][j - 1]:
                self._find_lcs(i - 1, j, current_str, result)
                self._find_lcs(i, j - 1, current_str, result)
            elif self.matrix_data[i - 1][j] > self.matrix_data[i][j - 1]:
                self._find_lcs(i - 1, j, current_str, result)
            else:
                self._find_lcs(i, j - 1, current_str, result)

