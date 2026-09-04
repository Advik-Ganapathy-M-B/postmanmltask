X = [
    [1, 60],
    [2, 65],
    [2, 80],
    [3, 70],
    [4, 75],
    [5, 80],
    [6, 85],
    [7, 90],
    [8, 95],
    [9, 90]
]

Y = [
    "Fail",
    "Fail",
    "Fail",
    "Fail",
    "Pass",
    "Pass",
    "Pass",
    "Pass",
    "Pass",
    "Pass"
]
#making the function to calculate gini impurity
def gini(y):
    truecount=0
    falsecount=0
    for i in range(0,len(y)):
        if (y[i]=="Pass"):
            truecount+=1
        elif (y[i]=="Fail"):
            falsecount+=1
    impurity=1-((truecount/len(y))**2)-((falsecount/len(y))**2)
    return impurity
print(gini(["Pass","Fail","Fail","Fail"]))