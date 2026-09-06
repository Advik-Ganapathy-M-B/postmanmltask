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

Y = ["Fail","Fail","Pass","Fail","Pass","Fail","Pass","Pass","Pass","Pass"]
Xcopy = [
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

Ycopy = [
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
    feature=0
    testthreshold=0
    step=X[0][1]/1000 
    maxfeature1=max(row[0] for row in X)
    maxfeature2=max(row[1] for row in X)
    mingini=1
    done=0
    while True:
        X_left,X_right,Y_left,Y_right=split_data(X,Y,feature,testthreshold)
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
        if testthreshold>maxfeature1:
            feature=1
            step=X[1][1]/1000
            testshreshold=0
            done=1
        if done==1 and testthreshold>maxfeature2:
            return (nodeleft,noderight,dataleft,dataright,setthreshold,setfeature)
leaf=[]
leafdata=[]
pendingnodes=[] #using as a stack
pendingdata=[]  #using as a stack
splits = []
def tree(X,Y):
    finish=0
    while True:
            if gini(Y)==0:#for case when its already pure at start
                leaf.append(X)
                leafdata.append(Y)
                break
            nodeleft,noderight,dataleft,dataright,setthreshold,setfeature=bestsplit(X,Y)
            splits.append((X,setfeature, setthreshold,nodeleft, noderight))
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
leaf, leafdata = tree(X, Y)
rightnodes=[]
leftnodes=[]
splitscopy=splits.copy()
def predict(x):
    index=0
    while True:
        for i in range(0,index+1):
            inputbranch,feature, threshold,leftbranch, rightbranch=splits.pop(i)
        if x[feature]<threshold: 
            leftnodes.append(x)
            currentbranch=leftbranch
            if inputbranch==currentbranch:
                for i in range(0,len(splits)):
                    if inputbranch==splits[i][0]:
                        index=i

            result=False
        else:
            rightnodes.append(x)
            currentbranch=rightbranch
            if inputbranch==currentbranch:
                for i in range(0,len(splits)):
                    if inputbranch==splits[i][0]:
                        index=i
            result= True
        if len(splits)==0:
            break
    return rightnodes,leftnodes,result
print(predict([5,80]))
