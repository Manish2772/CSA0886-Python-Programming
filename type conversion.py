def string_to_numeric(s):
    try:
        num = float(s)
        return num
    except ValueError:
        return "An Error has Occurred."

# Test cases
test_cases = ["5", "a"]

for case in test_cases:
    result = string_to_numeric(case)
    print(f"Input: \"{case}\" -> Output: {result}")
