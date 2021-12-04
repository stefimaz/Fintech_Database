# Module 12 Report

## Overview of the Analysis

In this section, describe the analysis you completed for the machine learning models used in this Challenge. This might include:

* Explain the purpose of the analysis.
The purpose of this analysis is to evaluate if the resampled training data is more effective at predicting high risk loans

* Explain what financial information the data was on, and what you needed to predict.
The data provided via the csv file contain information of borrowers including: loan size, interest rate, borrower income, debt to income, number of accounts, derogatory marks, total debt and loan status. We are trying to predict the likelihood of the borower defaulting on the loan. 

* Provide basic information about the variables you were trying to predict (e.g., `value_counts`).
After separating the data into labels(y) and features(X), we used "value_counts" to see the numbers of labels variable. We were able to see that the data was imbalanced. There was a much larger amount of (0), healthy loan(75036) compare to (1), high risk loan(2500). This coould could be a problem for training the model. 

* Describe the stages of the machine learning process you went through as part of this analysis.
Split the data into training and testing datasets by using train_test_split.
Fit a logistic regression model by using the training data (X_train and y_train).
Save the predictions on the testing data labels by using the testing feature data (X_test) and the fitted model
Evaluate the model’s performance by: Calculate the accuracy score of the model, generate a confusion matrix, and print the classification report.

* Briefly touch on any methods you used (e.g., `LogisticRegression`, or any resampling method).
We used Logistic Regression for both models. 
But since we had an original data that was imbalanced, we also used the resampling method (RandomOverSampler) so that the labels have an equal number of data points for the second model. 


## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

* Machine Learning Model 1:
  * Description of Model 1 Accuracy, Precision, and Recall scores.
   Accuracy: The accuracy score 95% 
   Precision: The precision was 100% for the healthy loan and 85% for the high risk loan
   Recall: The recall score was 99% for the healthy loan and 91% for the high risk loan
   ![original](images/model1.png)
* Machine Learning Model 2:
  * Description of Model 2 Accuracy, Precision, and Recall scores.
   Accuracy: The accuracy score 99% 
   Precision: The precision was 100% for the healthy loan and 84% for the high risk loan
   Recall: The recall score was 99% for the healthy loan and 99% for the high risk loan
   ![original](images/model2.png)
   
## Summary

Summarize the results of the machine learning models, and include a recommendation on the model to use, if any. For example:
* Which one seems to perform best? How do you know it performs best?
Looking at the accuracy numbers only, we would choose the second model as the better one. Model 2 also performed better on the recall as well and did pretty much the same for precision as model 1 (only 1% difference on the high risk loan). 

But looking at what the goal was for this analysis and the context of the data. The most important was to make sure we limit as much as possible the issue of high risk loan were the borrower will default. So in that case, the goal would be to have as less as possible False Negative. This is represented by the recall. The best recall is found in the model 2 (99%) that used resampled training data.

* Does performance depend on the problem we are trying to solve? (For example, is it more important to predict the `1`'s, or predict the `0`'s? )

Yes. Performance depends on what we are trying to solve. In this case, predicting the defaulting borrowers or the '1'. 


If you do not recommend any of the models, please justify your reasoning.
