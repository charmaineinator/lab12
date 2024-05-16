from LCSTestCase import LCSTestCase

class PrintFeedback:
    def write(self, string_to_write):
        print(string_to_write, end="")
test_feedback = PrintFeedback()

test_cases = [
    
    LCSTestCase(
        "ABCEDEFGHIJKL",
        "MNOPQRSTUVWXYZ",
        set()
    ),
    LCSTestCase(
        "",
        "",
        set()
    )
]
# Execute each test case and count the number that pass
pass_count = 0;
for test_case in test_cases:
    if test_case.execute(test_feedback):
        pass_count += 1
    test_feedback.write("\n")
#
# Print the summary
test_feedback.write(f"{pass_count} of {len(test_cases)}")
test_feedback.write(" test cases passed\n\n")