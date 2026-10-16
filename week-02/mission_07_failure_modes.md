# Mission 7: Understanding Machine Learning Failures

## 1. Introduction

Machine Learning models can make incorrect predictions when the training data is poor, the model is unsuitable, or real-world conditions differ from the conditions represented in the training data.

Understanding why a model fails is important because a model that appears accurate during development may not perform reliably in practical applications.

In semiconductor engineering, incorrect predictions can lead to missed defects, unnecessary inspections, or unreliable manufacturing analysis.

## 2. Common Reasons for Machine Learning Failure

| Failure Type | Meaning | Semiconductor Example |
|---|---|---|
| Poor Data Quality | The dataset contains missing, incorrect, or inconsistent values. | Leakage current measurements contain incorrect units. |
| Insufficient Data | There are not enough representative examples for the model to learn reliable patterns. | Only a few examples of defective chips are available. |
| Class Imbalance | One class appears much more frequently than another. | Most chips pass, while only a small number fail. |
| Overfitting | The model learns training-specific details instead of general patterns. | The model performs well on training records but poorly on new chip records. |
| Underfitting | The model fails to learn important relationships in the data. | The model cannot capture meaningful relationships between electrical measurements and failures. |
| Data Leakage | Information unavailable at prediction time incorrectly influences training or evaluation. | A feature derived from the final test outcome is accidentally used to predict that same outcome. |
| Distribution Shift | The data encountered in practice differs from the training data. | A model trained on one manufacturing process performs poorly after process conditions change. |
| Incorrect Evaluation | The chosen metric or testing procedure does not reflect real-world requirements. | A model has high accuracy but misses many defective chips. |

## 3. Detailed Example: High Accuracy but Poor Failure Detection

Consider a dataset containing 1,000 semiconductor chips. Suppose 950 chips pass and 50 chips fail.

A model predicts Pass for every chip. Its accuracy is:

Accuracy = 950 / 1,000 × 100 = 95%

Although the accuracy is 95%, the model does not identify any of the 50 failing chips.

| Metric | Result |
|---|---:|
| Total Chips | 1,000 |
| Actual Passing Chips | 950 |
| Actual Failing Chips | 50 |
| Correct Predictions | 950 |
| Accuracy | 95% |
| Recall for Failures | 0% |

This example demonstrates why accuracy alone may be misleading when the dataset is imbalanced. For semiconductor failure detection, recall and other relevant metrics should also be examined.

These numbers are an illustrative example, not results from a real semiconductor production system.

## 4. How to Identify Model Failures

Engineers can investigate model failures through a systematic process.

1. Check the dataset for missing values, duplicate records, incorrect measurements, and inconsistent units.
2. Examine the distribution of labels to identify class imbalance.
3. Compare training performance with validation and test performance to look for overfitting or underfitting.
4. Review the confusion matrix to understand false positives and false negatives.
5. Check whether the evaluation data represents the conditions in which the model will be used.
6. Investigate whether any features contain information that would not be available at prediction time.
7. Examine the types of examples on which the model makes incorrect predictions.

This process helps engineers identify whether the problem originates from the data, model, evaluation procedure, or changing operating conditions.

## 5. Possible Solutions to Common Failures

| Problem | Possible Solution |
|---|---|
| Poor Data Quality | Validate measurements, correct units, and handle missing values appropriately. |
| Insufficient Data | Collect more representative examples where possible. |
| Class Imbalance | Use appropriate metrics and consider class weighting or resampling methods. |
| Overfitting | Apply regularisation, simplify the model, or use appropriate cross-validation. |
| Underfitting | Improve features, choose a more suitable model, or adjust training. |
| Data Leakage | Remove unavailable or target-derived information and rebuild the evaluation process. |
| Distribution Shift | Monitor changes in incoming data and evaluate the model on newer, representative samples. |
| Incorrect Evaluation | Select metrics that reflect the actual costs and requirements of the application. |

Solutions should be chosen based on evidence. For example, oversampling is not automatically the best solution to class imbalance, and outliers should not be removed without investigating whether they represent genuine defects.

## 6. Why Failure Analysis Matters in Semiconductor Engineering

Semiconductor systems require reliable testing and quality control. A model that misses defective chips may create risks, while a model that generates too many false alarms may increase inspection effort and testing costs.

Failure analysis helps engineers understand model limitations before relying on its predictions. It also supports ongoing monitoring when manufacturing conditions, equipment, or data collection methods change.

Machine Learning predictions should be validated against appropriate engineering tests and quality requirements. They should not replace mandatory testing merely because a model has a high reported accuracy.

## 7. Conclusion

Machine Learning models can fail because of poor data quality, insufficient examples, class imbalance, overfitting, underfitting, data leakage, distribution shift, or inappropriate evaluation.

A systematic investigation of data, metrics, predictions, and real-world conditions helps identify the cause and guide corrective action. In semiconductor engineering, this is especially important because missed failures and unnecessary false alarms can both have significant consequences.

## References

1. Google Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course
2. Scikit-learn Model Evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
3. IBM Machine Learning: https://www.ibm.com/think/topics/machine-learning
