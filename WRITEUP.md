# Explanation of code and technical choices made
Name: Advik Ganapathy M B
BITS ID: 2026A7PS0354P

## task4.py 

Line 1: Importing random library

Line 2 - 115 : Initializing data used for training and testing. Each row of X has 5 columns. Each row is a student in a class. The first column shows their study hours per day, second shows their attendance percentage, third shows their assignment score, fourth shows their previous score and fifth shows their hours of sleep on the day before the exam.
The Y datasets show if the student corresponding to that row number passed or failed

Line 117 to 128 is related to the random forest implementation. The two functions help us select a random feature and to bootstrap the data respectively. randint is used to send the index of one of the features. To boostrap we pick a random index of the data and append it to X_bootstrap and the pass/fail status to Y_boostrap. This allows duplicates in the bootstrapped datasets too.

Line 129-141 : These lines define a function called gini to find the gini impurity of the dataset of Pass or Fail passed as y to this function.It counts number of pass and number of fail values then it returns the impurity after using the formula for finding gini impurity.

Line 143-155: This function takes input of both student attributes and their pass/fail status with the feature to be split on and the threshold for that feature. Then based on this feature it is split, where the attribute of the student is less than the threshold the student goes to the left branch, else the student goes to the right branch. It returns all the branches and the pass/fail status of each branch

Line 157-159 : After a root node or a node is split into two parts to find the overall gini impurity we need the average of the two impurities. This also needs to be a weighted average as branches on either side might have different number of members. So this function returns the weighted average of the gini impurity of the two branches using gini function within it

Line 161 - 188 : Here the first line assigns feature variable to a random feature using the function random_features in line 117-119. The first feature is index 0, then 2nd is index 1 and so on. 
Initially here I had made feature set to 0 and then switch to 2nd feature after splitting based on this feature is checked and so on. But this function was changed to random feature for the random forest implementation. 
The old feature =0 logic is in my `third commit with the name: Made function to find threshold and feature`

Continuing down the function, the max value for that feature is found and divided by 1000 to find the step size (this can be 100 or any appropriate number but I chose 1000). We start a loop to find the split which had the least gini impurity so that we can get the best possible split at each place where we need to split. 
Initially this was a while True loop while working on single tree as seen in my third commit of this file. The action remains the same but I changed it to this condition to avoid using that extra done variable. I also had to add a fallback return None here as in random forest due to the variety of splits possible I was getting errors due to the case where if there is no threshold leading to non empty groups my nodeleft would stay none so by implementing this fallback I can deal with this later as done in the function tree() later

Line 189-193- Initializing some variables needed for the next funciton

Line 195-199: This is a regulation function to fix overfitting. Before I was setting a node as leaf only if the gini impurity was 0, here I regulate it by making it a leaf if it has less than or equal to 5 entries even if its not completely pure. It returns 1 for when it has less than 5 members in that set. 

Line 200-274: This is the tree building function. We start an infinite loop then we check if we have received a pure dataset as input and make that a leaf (add it to a list of leaves and its data to leafdata list) if it is. 
Then the next part checks if the regulation is met, if it is, the dataset is added as a leaf and the majority vote from its pass/fail status of its members is stored in leafdata. This was needed for the random forest implementation so was not there in earlier commits. 
Pending nodes is all the rightside nodes that I havent processed through yet. Initially my idea was to go through all the left side then do all the right side as seen in commit 4. I was not able to implement it like this and rather had to settle it to do a left branch then continue doing left branches till it was possible then a right branch and so on. One of the main issues was the pending nodes so by changing my logic and using this pendingnodes list for right side branches I could fix the errors. Intially I was not storing my rightside branches so it was not working. 
I'm constantly storing information of each split into a splits list for later. 
This function also involves changing X and Y entered to keep the loop running and make the first line of the function not only a check for the input data but also for the next iteration's Y. 
You can see the constant left side checking from the use of continue until left side is done and the finish variable is changed. Then we evaluate the right side branches. Once right is done till wherever possible we again switch to left by making finish=0. This function finally returns the leaf and leafdata


I have only implemented classification and not basic regression as the data I was working on was just Pass/Fail data (categorical) rather than a continuous numerical value so basic regression was not applicable.

Line 275-320: Single majority stores if pass or fail is more common, this is used for a fallback later.
Then we move to the implementation of the stretch goal which is feature importance 
Impurity decrease finds the decrease in gini impurity caused by splitting at that given feature, as each forest involves 100 trees we find the weighted average of each feature's decrease in impurity and normalize it. This is then converted to percentages to show each feature's importance in that run.

Line 321-350: This is the single tree prediction function, initially it was called predict but later changed to singletreepredict as I used predict for the forest implementation. It is used to find the result if we give it a data point. It returns either Pass or fail. All branches made from a split are retrieved from the splits variable. We make an infinite loop. We check if the branch we are standing on (current branch) is our retrieved branch from splits, this is inside the for loop checking each split so eventually we find our split.  If the attribute value is less than the threshold we go left else right (as done during tree building) Once we find the split and check the direction we set found branch as true and come out of the for loop. 
If there is no split from this branch, that means its a leaf. So we store it as a leaf and find its corresponding result from the leafdata list and return it 
Here I made a fallback incase it doesnt find a leaf it will return the majority value of the data set. This is just a safety net to prevent errors

Line 352-381: Uses the same logic as single tree predict, just that for forest we use boostrapped data
Here the fallback for not finding a leaf is set to None as in a forest the majority voting of all the trees will give a Pass/Fail result at the end anyway so I do not need to make this one tree (if any) return a Pass/Fail value incase of error

Line 382-391: Finding number of correct answers by comparisons and returning it

Line 392-402: This forest predict uses the predict function but enforces majority voting for each group that it receives and returns the majority vote 

Line 403-412: Checks accuracy of the forest by comparing each value predicted with actual value

Line 413-414: Print statements to test the accuracy of the forest on training and testing data

Line 417-422: Comparing with sklearn for task 4.6, the print statements are commented out 

Line 423-439: All print statements to test every feature in my program and see the results

## correctnessharness.py 
Imports sklearn and my program and compares their pretrained models with my implementation. 
There are 3 tests for gini, tree predictions and forest predictions.
For gini impurity their gini function and my implementation is tested on a small set of data.
For tree prediction the lists of my predictions and sklearn predictions are compared, if they are same its classified as Pass.
In forest prediction if the sklearn prediction and my prediction are within 15% accuracy it is a Pass.

Thank you.
