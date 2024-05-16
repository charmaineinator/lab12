from LCSTestCase import LCSTestCase

class PrintFeedback:
    def write(self, string_to_write):
        print(string_to_write, end="")
test_feedback = PrintFeedback()

test_cases = [
    
    LCSTestCase(
        "ZYBOOKS",
        "LOOK",
        { "OOK" }
    ),
    LCSTestCase(
        "A_B_C",
        "X_Y_Z",
        { "__" }
    ),
    
    LCSTestCase(
        "DATA STRUCTURES",
        "ALGORITHMS",
        { "ARTS" }
    ),
    
    LCSTestCase(
        "RELATIVELY",
        "ACTIVE",
        { "ATIVE" }
    ),
    LCSTestCase(
        "ACTIVE",
        "RELATIVELY",
        { "ATIVE" }
    ),
    LCSTestCase(
        "very very very very very very very very very long string",
        "short string",
        { "o string", "r string" }
    ),
    LCSTestCase(
        "five food groups",
        "dairy, vegetables, fruits, grains, and protein",
        { "ive f grp", "ive fd ro", "ive f gro", "ive f grs" }
    ),
    LCSTestCase(
        "A MAN A PLAN A CANAL PANAMA",
        "THE RAIN IN SPAIN STAYS MAINLY IN THE PLAIN",
        { " AN  PAN A ANL PAN" }
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