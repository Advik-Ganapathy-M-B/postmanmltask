import random
#the features are StudyHours,Attendance,AssignmentScore,PreviousScore,SleepHours
X_train = [
    [2, 65, 45, 50, 6],
    [3, 70, 50, 55, 6],
    [4, 72, 55, 58, 7],
    [2, 68, 48, 52, 5],
    [5, 75, 62, 60, 7],
    [3, 78, 55, 64, 6],
    [6, 80, 68, 65, 7],
    [4, 82, 60, 67, 6],
    [7, 85, 72, 70, 7],
    [5, 80, 65, 68, 8],
    [8, 88, 75, 73, 7],
    [6, 86, 70, 75, 6],
    [9, 90, 82, 78, 8],
    [7, 91, 78, 80, 7],
    [10, 92, 85, 82, 8],
    [8, 89, 80, 79, 7],
    [11, 94, 88, 85, 8],
    [9, 93, 84, 83, 7],
    [12, 95, 90, 87, 8],
    [10, 96, 86, 89, 7],

    [1, 60, 40, 45, 5],
    [2, 62, 42, 48, 6],
    [3, 66, 46, 51, 6],
    [4, 69, 52, 54, 7],
    [5, 71, 58, 57, 6],
    [3, 73, 50, 59, 5],
    [6, 76, 64, 62, 7],
    [7, 79, 66, 65, 8],
    [8, 83, 70, 69, 7],
    [9, 84, 74, 72, 6],
    [10, 87, 78, 76, 8],
    [11, 89, 81, 79, 7],
    [12, 91, 83, 81, 8],
    [13, 92, 87, 84, 7],
    [14, 94, 89, 86, 8],
    [15, 95, 92, 90, 7],
    [4, 77, 59, 61, 6],
    [5, 74, 61, 63, 7],
    [7, 81, 69, 67, 6],
    [8, 86, 76, 71, 8],
    [6, 78, 63, 66, 5],
    [9, 88, 77, 74, 7],
    [10, 90, 80, 77, 6],
    [11, 93, 85, 82, 8],
    [13, 96, 91, 88, 7],
    [14, 97, 93, 91, 8],
    [2, 67, 44, 49, 7],
    [4, 70, 53, 56, 5],
    [5, 76, 57, 60, 6],
    [6, 82, 67, 64, 7],
    [8, 87, 73, 70, 6],
    [9, 85, 79, 73, 8],
    [10, 89, 82, 78, 7],
    [12, 94, 88, 85, 8],
    [13, 95, 90, 87, 6],
    [15, 98, 94, 92, 8],
    [3, 64, 47, 50, 5],
    [5, 73, 56, 58, 7],
    [7, 80, 68, 64, 6],
    [9, 91, 81, 76, 8],
    [11, 90, 84, 80, 7],
    [14, 96, 92, 89, 8]
]

Y_train = [
    "Fail","Fail","Fail","Fail","Fail",
    "Fail","Pass","Fail","Pass","Pass",
    "Pass","Pass","Pass","Pass","Pass",
    "Pass","Pass","Pass","Pass","Pass",
    "Fail","Fail","Fail","Fail","Fail",
    "Fail","Pass","Pass","Pass","Pass",
    "Pass","Pass","Pass","Pass","Pass",
    "Pass","Pass","Pass","Pass","Pass",
    "Fail","Pass","Pass","Pass","Pass",
    "Pass","Pass","Fail","Fail","Pass",
    "Pass","Pass","Pass","Pass","Pass",
    "Fail","Fail","Pass","Pass","Pass",
    "Pass","Pass"
]

X_test = [
    [2, 66, 43, 49, 6],
    [4, 71, 54, 57, 7],
    [6, 77, 65, 63, 6],
    [7, 82, 71, 68, 7],
    [9, 86, 76, 73, 8],
    [10, 91, 83, 79, 7],
    [12, 93, 87, 84, 8],
    [13, 96, 90, 88, 7],
    [15, 97, 93, 91, 8],
    [3, 69, 49, 53, 5],

    [5, 75, 60, 59, 6],
    [8, 84, 72, 70, 7],
    [11, 92, 84, 81, 8],
    [14, 95, 91, 89, 7],
    [1, 61, 39, 44, 6],
    [6, 79, 66, 65, 7],
    [9, 89, 78, 75, 6],
    [12, 95, 89, 86, 8],
    [4, 68, 51, 55, 5],
    [10, 88, 80, 77, 7]
]

Y_test = [
    "Fail","Fail","Pass","Pass","Pass",
    "Pass","Pass","Pass","Pass","Fail",
    "Fail","Pass","Pass","Pass","Fail",
    "Pass","Pass","Pass","Fail","Pass"
]

#making the function to calculate gini impurity
def random_features(X):
    feature=random.randint(0,len(X[0])-1)
    return feature
def bootstrap(X,Y):
    X_bootstrap=[]
    Y_bootstrap=[]
    length=len(X)
    for i in range(length):
        i=random.randint(0,length-1)
        X_bootstrap.append(X[i])
        Y_bootstrap.append(Y[i])
    return X_bootstrap,Y_bootstrap
def gini(y):
    truecount=0
    falsecount=0
    for i in range(0,len(y)):
        if (y[i]=="Pass"):
            truecount+=1
        elif (y[i]=="Fail"):
            falsecount+=1
    if len(y)==0:
        impurity=0.0
    else:
        impurity=1-((truecount/len(y))**2)-((falsecount/len(y))**2)
    return impurity

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

def ginisplit(set1,set2):
    avg= (gini(set1)*len(set1)/(len(set1)+len(set2)))+gini(set2)*len(set2)/(len(set1)+len(set2))
    return avg

def bestsplit(X,Y):
    feature=random_features(X)
    testthreshold=0
    maxfeature=max(row[feature] for row in X)
    step=maxfeature/1000 
    mingini=1
    nodeleft=None
    noderight=None
    dataleft=None
    dataright=None
    setthreshold=None
    setfeature=feature
    while testthreshold<=maxfeature:
        X_left,X_right,Y_left,Y_right=split_data(X,Y,feature,testthreshold)
        if len(X_left)>0 and len(X_right)>0:
            score=ginisplit(Y_left,Y_right)
            if score<mingini:
                mingini=score
                nodeleft=X_left
                noderight=X_right
                dataleft=Y_left
                dataright=Y_right
                setthreshold=testthreshold
                setfeature=feature
        testthreshold+=step
    if nodeleft is None:
        return None
    return(nodeleft,noderight,dataleft,dataright,setthreshold,setfeature)
leaf=[]
leafdata=[]
pendingnodes=[] #using as a stack
pendingdata=[]  #using as a stack
splits = []

def regulation(X):
    if len(X)<=5:
        return 1
    else:
        return 0
def tree(X,Y):
    finish=0
    passcount=0
    while True:
            if gini(Y)==0:#for case when its already pure at start
                leaf.append(X)
                leafdata.append(Y)
                break
            if regulation(X):
                leaf.append(X)
                passcount=0
                for i in Y:
                    if i=="Pass":
                        passcount+=1
                if passcount/len(Y)>=0.5:
                    majority="Pass"
                else:
                    majority="Fail"
                leafdata.append([majority])

                if len(pendingnodes) == 0:
                    break
                else:
                    X = pendingnodes.pop()
                    Y = pendingdata.pop()
                    continue
            if len(set(map(tuple, X))) == 1:
                leaf.append(X)
                leafdata.append(Y)
                if len(pendingnodes) == 0:
                    break
                else:
                    X = pendingnodes.pop()
                    Y = pendingdata.pop()
                    continue
            result=bestsplit(X,Y)

            if result is None:
                leaf.append(X)
                leafdata.append([Y[0]])
                if len(pendingnodes) == 0:
                    break
                else:
                    X = pendingnodes.pop()
                    Y = pendingdata.pop()
                    continue
            nodeleft,noderight,dataleft,dataright,setthreshold,setfeature=result
            splits.append((X,Y,setfeature, setthreshold,nodeleft, noderight,dataleft,dataright))
            pendingnodes.append(noderight)
            pendingdata.append(dataright) #for all the right branches that we eval after all left
            if gini(dataleft)==0 and finish==0:
                leaf.append(nodeleft)
                leafdata.append(dataleft)
                finish=1
            else:
                X=nodeleft
                Y=dataleft
                continue
            if finish==1:
                noderight=pendingnodes.pop()
                dataright=pendingdata.pop()
            if gini(dataright)==0 and finish==1:
                leaf.append(noderight)
                leafdata.append(dataright)
                if len(pendingnodes)==0:
                    break
                else:
                    X=pendingnodes.pop()
                    Y=pendingdata.pop()
                    finish=0
            else:
                X=noderight
                Y=dataright
                finish=0
    return leaf,leafdata
single_majority = "Pass" if Y_train.count("Pass") >= Y_train.count("Fail") else "Fail"
leaf = []
leafdata = []
pendingnodes = []
pendingdata = []
splits = []
#stretch goal
def impuritydecrease(Y,dataleft,dataright):
    parentgini=gini(Y)
    childgini=ginisplit(dataleft,dataright)
    decrease=parentgini-childgini
    return decrease
def importancecalc(splits,totalsamples):
    for split in splits:
        decrease=impuritydecrease(split[1],split[6],split[7])
        weighted_decrease = decrease * len(split[1]) /totalsamples
        feature_importance[split[2]] += weighted_decrease
    return feature_importance

tree(X_train, Y_train)

single_tree = (X_train,Y_train, splits.copy(), leaf.copy(), leafdata.copy())
feature_importance = [0, 0, 0, 0, 0]
forest = []
forest_importance = [0,0,0,0,0]
for i in range(100):
    X_bootstrap, Y_bootstrap = bootstrap(X_train, Y_train)

    leaf = []
    leafdata = []
    pendingnodes = []
    pendingdata = []
    splits = []

    tree(X_bootstrap, Y_bootstrap)

    current_tree = (X_bootstrap, splits.copy(), leaf.copy(), leafdata.copy())
    forest.append(current_tree)
    treeimportance = importancecalc(splits, len(X_bootstrap))
    for i in range(len(treeimportance)):
        forest_importance[i]+=treeimportance[i]
for i in range(len(forest_importance)):
    forest_importance[i]=forest_importance[i]/100
total = sum(forest_importance)
for i in range(len(forest_importance)):
    forest_importance[i] = (forest_importance[i] / total)*100
def singletreepredict(x):
    rightnodes=[]
    leftnodes=[]
    X_train,Y_train,splits,leaf,leafdata = single_tree
    currentbranch=X_train

    while True:
        foundsplit=False

        for split in splits:
            inputbranch,inputdata,feature,threshold,leftbranch,rightbranch,dataleft,dataright = split

            if currentbranch==inputbranch:

                if x[feature]<threshold:
                    leftnodes.append(x)
                    currentbranch=leftbranch
                else:
                    rightnodes.append(x)
                    currentbranch=rightbranch

                foundsplit=True
                break

        if foundsplit==False:
            for i in range(len(leaf)):
                if currentbranch==leaf[i]:
                    result=leafdata[i][0]
                    return rightnodes,leftnodes,result
            return rightnodes,leftnodes,single_majority

def predict(x,current_tree):
    rightnodes=[]
    leftnodes=[]
    
    X_bootstrap,Y_bootstrap,splits, leaf, leafdata = current_tree
    currentbranch=X_bootstrap
    while True:
        foundsplit=False
        
        for split in splits:
            inputbranch,inputdata,feature,threshold,leftbranch,rightbranch,dataleft,dataright=split
            
            if currentbranch==inputbranch:
                
                if x[feature]<threshold:
                    leftnodes.append(x)
                    currentbranch=leftbranch
                else:
                    rightnodes.append(x)
                    currentbranch=rightbranch
                
                foundsplit=True
                break
        
        if foundsplit==False:
            for i in range(len(leaf)):
                if currentbranch==leaf[i]:
                    result=leafdata[i][0]
                    return rightnodes,leftnodes,result
            return rightnodes,leftnodes,None
def accuracy(X,Y):
    correct=0
    
    for i in range(len(X)):
        result=singletreepredict(X[i])[2]
        
        if result==Y[i]:
            correct+=1
    
    return correct/len(X)
def forest_predict(x):
    predictions=[]

    for i, tree in enumerate(forest):
        result=predict(x,tree)[2]
        predictions.append(result)

    if predictions.count("Pass") >= predictions.count("Fail"):
        return "Pass"
    else:
        return "Fail"
def forest_accuracy(X, Y):
    correct = 0

    for i in range(len(X)):
        result = forest_predict(X[i])

        if result == Y[i]:
            correct += 1

    return correct / len(X)
"""
print("Forest training accuracy", forest_accuracy(X_train, Y_train))
print("Forest testing accuracy", forest_accuracy(X_test, Y_test))"""

from sklearn.tree import DecisionTreeClassifier
sklearn_tree = DecisionTreeClassifier(criterion="gini")
sklearn_tree.fit(X_train, Y_train)

sklearn_predictions = sklearn_tree.predict(X_test)
sklearn_accuracy = sklearn_tree.score(X_test, Y_test)
#saving the 4.6 print commands as comments 
"""print("My accuracy on testing data: ",accuracy(X_test,Y_test))
print("Sklearn testing accuracy:", sklearn_accuracy)
print("Actual test data",Y_test)
print("Sklearn predictions:", sklearn_predictions)
my_predictions = []
for x in X_test:
    my_predictions.append(singletreepredict(x)[2])
print("My predictions: ",my_predictions)"""
#to compare accuracy and overfitting
"""print("Forest training accuracy", forest_accuracy(X_train, Y_train))
print("Forest testing accuracy", forest_accuracy(X_test, Y_test))
print("Single tree training accuracy",accuracy(X_train, Y_train))
print("Single tree testing accuracy",accuracy(X_test, Y_test))"""
for i in range (1,len(forest_importance)+1):
    print("Importance of feature number",i," ",forest_importance[(i-1)],"%")