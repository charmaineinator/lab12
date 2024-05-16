from LCSTestCase import LCSTestCase

class PrintFeedback:
    def write(self, string_to_write):
        print(string_to_write, end="")
test_feedback = PrintFeedback()

test_cases = [
    LCSTestCase(
        "ALASKAN",
        "BANANAS",
        { "AAA", "AAS", "AAN" },
        [
            [ 0, 1, 1, 1, 1, 1, 1 ],
            [ 0, 1, 1, 1, 1, 1, 1 ],
            [ 0, 1, 1, 2, 2, 2, 2 ],
            [ 0, 1, 1, 2, 2, 2, 3 ],
            [ 0, 1, 1, 2, 2, 2, 3 ],
            [ 0, 1, 1, 2, 2, 3, 3 ],
            [ 0, 1, 2, 2, 3, 3, 3 ]
        ]
    ),
    LCSTestCase(
        "BAAB",
        "ABBA",
        { "AA", "BB", "AB", "BA" },
        [
            # A  B  B  A
            [ 0, 1, 1, 1 ], # B
            [ 1, 1, 1, 2 ], # A
            [ 1, 1, 1, 2 ], # A
            [ 1, 2, 2, 2 ]  # B
        ]
    ),
    LCSTestCase(
        "ABBA",
        "BAAB",
        { "AA", "BB", "AB", "BA" },
        [
            # B  A  A  B
            [ 0, 1, 1, 1 ], # A
            [ 1, 1, 1, 2 ], # B
            [ 1, 1, 1, 2 ], # B
            [ 1, 2, 2, 2 ]  # A
        ],
    ),
    LCSTestCase(
        "lower case",
        "UPPER CASE",
        { " " },
        [
            # U  P  P  E  R     C  A  S  E
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # l
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # o
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # w
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # e
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # r
            [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ], #
            [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ], # c
            [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ], # a
            [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ], # s
            [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ]  # e
        ],
    ),
    LCSTestCase(
        "PROGRAMMING",
        "PROBLEM",
        { "PROM" },
        [
            [ 1, 1, 1, 1, 1, 1, 1 ],
            [ 1, 2, 2, 2, 2, 2, 2 ],
            [ 1, 2, 3, 3, 3, 3, 3 ],
            [ 1, 2, 3, 3, 3, 3, 3 ],
            [ 1, 2, 3, 3, 3, 3, 3 ],
            [ 1, 2, 3, 3, 3, 3, 3 ],
            [ 1, 2, 3, 3, 3, 3, 4 ],
            [ 1, 2, 3, 3, 3, 3, 4 ],
            [ 1, 2, 3, 3, 3, 3, 4 ],
            [ 1, 2, 3, 3, 3, 3, 4 ],
            [ 1, 2, 3, 3, 3, 3, 4 ]
        ],
    ),
    LCSTestCase(
        "LOOK",
        "ZYBOOKS",
        { "OOK" },
        [
            [ 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 1, 1, 1, 1 ],
            [ 0, 0, 0, 1, 2, 2, 2 ],
            [ 0, 0, 0, 1, 2, 3, 3 ]
        ],
        True
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