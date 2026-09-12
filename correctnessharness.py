import task4
from sklearn.tree import DecisionTreeClassifier
X = [[1], [2], [3], [4], [5], [6]]
Y = ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass"]
sklearn_tree = DecisionTreeClassifier(criterion="gini", random_state=42)
sklearn_tree.fit(X, Y)
sklearn_predictions = sklearn_tree.predict(X)
expected = 0.5
actual = task4.gini(Y)
if actual == expected:
    print("Gini test: Pass")
else:
    print("Gini test: Fail")
task4.leaf = []
task4.leafdata = []
task4.pendingnodes = []
task4.pendingdata = []
task4.splits = []
task4.tree(X, Y)
test_tree = (X,Y,task4.splits.copy(),task4.leaf.copy(),task4.leafdata.copy())
my_predictions = []
for x in X:
    result = task4.predict(x, test_tree)[2]
    my_predictions.append(result)
if my_predictions == list(sklearn_predictions):
    print("Tree comparison: Pass")
else:
    print("Tree comparison: Fail")
from sklearn.ensemble import RandomForestClassifier
reference_forest = RandomForestClassifier(n_estimators=100,criterion="gini",random_state=42)
reference_forest.fit(task4.X_train, task4.Y_train)
reference_predictions = reference_forest.predict(task4.X_test)
reference_accuracy = reference_forest.score(task4.X_test, task4.Y_test)
my_accuracy = task4.forest_accuracy(task4.X_test, task4.Y_test)
if abs(my_accuracy - reference_accuracy) <= 0.15:
    print("Random forest comparison: Pass")
else:
    print("Random forest comparison: Fail")
