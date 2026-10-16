# Mission 6: Model Evaluation and Generalisation

## 1. Introduction

Model evaluation is the process of measuring how well a Machine Learning model performs on a particular task. It helps determine whether the model makes reliable predictions and whether it can perform well on data it has not seen during training.

Generalisation is the ability of a trained model to make useful predictions on new, unseen data. A model that performs well only on its training data may not generalise effectively.

## 2. Training, Validation, and Testing Data

A dataset can be divided into separate subsets for different purposes.

| Dataset | Purpose | Example |
|---|---|---|
| Training Data | Used to train the model and learn its parameters. | Historical chip test records used for learning. |
| Validation Data | Used to compare models and tune settings during development. | A separate set of chip records used to select a model. |
| Testing Data | Used for final evaluation on data not used for model selection. | Unseen chip records used to measure final performance. |

The test set should remain separate from model training and model selection. Using test results repeatedly to tune a model can lead to an overly optimistic evaluation.

## 3. Classification Evaluation Metrics

Classification models predict categories, such as Pass or Fail. Several metrics can be used to evaluate their performance.

| Metric | Meaning |
|---|---|
| Accuracy | The proportion of all predictions that are correct. |
| Precision | The proportion of predicted positive cases that are actually positive. |
| Recall | The proportion of actual positive cases that the model correctly identifies. |
| F1-Score | The harmonic mean of precision and recall. |

Accuracy is useful when the classes are reasonably balanced and the costs of different errors are similar. When one class is rare, accuracy alone can be misleading.

For example, if only a small percentage of chips fail, a model that predicts Pass for every chip could achieve high accuracy while failing to identify defective chips.

## 4. Worked Example: Semiconductor Failure Detection

Consider an illustrative test set containing 100 semiconductor chips. In this example, a Fail result is treated as the positive class.

| Actual Result | Predicted Fail | Predicted Pass |
|---|---:|---:|
| Actual Fail | 15 (True Positive) | 5 (False Negative) |
| Actual Pass | 10 (False Positive) | 70 (True Negative) |

From this table:

- True Positives (TP) = 15
- False Positives (FP) = 10
- False Negatives (FN) = 5
- True Negatives (TN) = 70

### Accuracy Calculation

Accuracy is the number of correct predictions divided by the total number of predictions.

Accuracy = (TP + TN) / (TP + TN + FP + FN)

Accuracy = (15 + 70) / 100 = 85%

### Precision Calculation

Precision measures how many chips predicted as Fail actually failed.

Precision = TP / (TP + FP)

Precision = 15 / (15 + 10) = 60%

### Recall Calculation

Recall measures how many of the actual failing chips were correctly identified.

Recall = TP / (TP + FN)

Recall = 15 / (15 + 5) = 75%

### F1-Score Calculation

F1-Score = 2 × (Precision × Recall) / (Precision + Recall)

F1-Score = 2 × (0.60 × 0.75) / (0.60 + 0.75)

F1-Score ≈ 66.67%

### Results Summary

| Metric | Result |
|---|---:|
| Accuracy | 85% |
| Precision | 60% |
| Recall | 75% |
| F1-Score | 66.67% |

These values are calculated from the illustrative confusion matrix above. They are not results from an actual trained model.

## 5. Why Generalisation Matters

A model should perform well on new data, not only on the examples used during training.

For example, a semiconductor failure prediction model may learn patterns from one manufacturing batch but perform poorly on another batch because of differences in equipment, operating conditions, or measurement procedures.

To evaluate generalisation, engineers should test the model on representative data that was not used for training. Where data has a time or manufacturing-batch structure, the evaluation split should reflect how the model will be used in practice.

## 6. Overfitting and Underfitting

| Concept | Meaning | Example |
|---|---|---|
| Overfitting | The model learns the training data too closely, including noise or accidental patterns. | A model performs very well on training records but poorly on new chip records. |
| Underfitting | The model is too simple or has not learned enough from the data. | A model fails to capture important relationships between temperature, leakage current, and chip failures. |
| Good Generalisation | The model learns useful patterns that also work on unseen data. | A model performs consistently on separate, representative test records. |

Overfitting can sometimes be reduced through regularisation, simpler models, more representative training data, or appropriate cross-validation. Underfitting may require better features, a more suitable model, or improved training.

## 7. Choosing the Right Evaluation Metric

The evaluation metric should match the purpose of the model and the consequences of its errors.

In semiconductor failure detection, missing a genuinely defective chip may be costly. Recall can therefore be important because it measures how many actual failures are detected.

However, false alarms also matter because they can cause unnecessary inspections and additional testing. Precision helps measure how reliable the model's Fail predictions are.

Engineers should consider multiple metrics and the costs of different errors rather than relying on accuracy alone.

## 8. Conclusion

Model evaluation helps measure the quality and reliability of Machine Learning predictions. Training, validation, and testing datasets have different purposes, while metrics such as accuracy, precision, recall, and F1-score provide different views of classification performance.

Generalisation is essential because a model must work on unseen data to be useful in practice. In semiconductor engineering, careful evaluation can help determine whether a model is suitable for failure detection and other testing applications.

## References

1. Google Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course
2. Scikit-learn Model Evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
3. IBM Machine Learning: https://www.ibm.com/think/topics/machine-learning
