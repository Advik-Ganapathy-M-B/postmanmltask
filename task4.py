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

def split_data(X,Y,feature,threshold):
    X_left=[]
    X_right=[]
    Y_right=[]
    Y_left=[]
    for i in range(0,len(X)):
        if X[i][feature]<threshold:
            X_left.append(X[i])
            Y_left.append(Y[i])
        else: 
            X_right.append(X[i])
            Y_right.append(Y[i])
    return X_left,X_right,Y_left,Y_right
leftX,rightX,leftY,rightY=split_data(X,Y,0,4)
print(leftX)
print(leftY)
print(rightX)
print(rightY)