##First, identify the correct order (simple)
##Then, look at order cards are in currently and iterate from left to right
##  - Give each card a value; set the value of the first card to 1
##  - Otherwise, set the value to be one plus the largest value of a card that
##      that we've already set the value for that comes before that card in the
##      correct order
##  - This iteration is cheap (will need a double loop, but not on many elts)
##Finally, pick the maximal value in that list - the answer is the length of the
##  list minus that maximal value.
