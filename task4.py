
X_train=[
    [1, 60],
    [2, 65],
    [2, 80],
    [3, 70],
    [4, 75],
    [5, 80]
    ]
X_test=[ [6, 85],
    [7, 90],[8, 95],
    [9, 90]]
Y_train = ["Fail","Fail","Pass","Fail","Pass","Fail"]
Y_test=["Pass","Pass","Pass","Pass"]
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

Ycopy = ["Fail","Fail","Pass","Fail","Pass","Fail","Pass","Pass","Pass","Pass"]

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
        if testthreshold>maxfeature1 and done==0:
            feature=1
            step=X[1][1]/1000
            testthreshold=0
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
leaf, leafdata = tree(X_train, Y_train)
def predict(x):
    rightnodes=[]
    leftnodes=[]
    
    currentbranch=X_train
    
    while True:
        foundsplit=False
        
        for split in splits:
            inputbranch,feature,threshold,leftbranch,rightbranch=split
            
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
            
def accuracy(X,Y):
    print( X,Y)
    correct=0
    
    for i in range(len(X)):
        result=predict(X[i])[2]
        
        if result==Y[i]:
            correct+=1
    
    return correct/len(X)
print("Training accuracy: ",accuracy(X_train,Y_train))
print("Testing accuracy: ",accuracy(X_test,Y_test))
