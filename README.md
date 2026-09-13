# postmanmltask

## Postman AI/ML Task
Name: Advik Ganapathy M B  
BITS ID: 2026A7PS0354P  

### Task Description

Implemented a Decision Tree and Random Forest classifier from scratch in Python. Feature importance was also implemented as a stretch goal.

## Requirements

The main Decision Tree and Random Forest implementation uses Python's built-in `random` module.
`scikit-learn` is used for comparison with its Decision Tree and Random Forest implementations.
The correctness harness uses `scikit-learn` to compare my implementation with trusted reference models.

## Running the Project
Run `task4.py` to build the Decision Tree and Random Forest.
Run `correctnessharness.py` to run the correctness checks.

## Output
The print statements used to check things like accuracy, overfitting, and feature importance have been commented out for now. They can be uncommented whenever these results need to be checked.

The correctness harness checks the Gini calculation, Decision Tree predictions, and Random Forest performance against reference results.