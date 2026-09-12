from task4 import gini

test_data = ["Pass", "Pass", "Fail", "Fail"]

expected = 0.5
actual = gini(test_data)

if actual == expected:
    print("Gini test: PASS")
else:
    print("Gini test: FAIL")