# Mission 5: Understanding Model Anatomy

## 1. Introduction

A Machine Learning model is a system that learns patterns from data and uses those patterns to make predictions or decisions. Understanding how a model is built helps engineers understand how it learns, how it produces outputs, and how its performance can be evaluated.

The main components of a Machine Learning workflow include input features, model parameters, a learning algorithm, predictions, and an evaluation process.

## 2. Input Features

Input features are the variables provided to a model to help it make a prediction. The selection and quality of these features influence how effectively the model can learn useful patterns.

Example: In semiconductor testing, voltage, temperature, and leakage current can be used as input features to predict whether a chip will pass or fail a test.

Other examples include:
- Age and income for a financial prediction.
- Pixel values for image classification.
- Clock frequency and voltage for power consumption estimation.

## 3. Model Parameters

Model parameters are values learned by a Machine Learning model during training. They determine how the model uses input features to produce predictions.

For example, in a linear regression model, the coefficients and intercept are learned parameters. In a neural network, weights and biases are learned parameters.

The training process adjusts these parameters to reduce prediction errors according to a chosen objective.

## 4. Learning Algorithm

A learning algorithm is the method used to learn model parameters from training data.

For example, gradient descent updates model parameters in a direction intended to reduce the loss function. Decision tree algorithms learn rules that divide data into groups based on feature values.

Different learning algorithms are suitable for different types of problems and datasets.

## 5. Loss Function

A loss function measures how different a model's prediction is from the correct target for a training example. During training, the learning process attempts to minimise the loss.

Examples include:
- Mean Squared Error (MSE), commonly used for regression.
- Cross-Entropy Loss, commonly used for classification.

A low training loss does not automatically mean that a model will perform well on new data. Its performance must also be evaluated on data that was not used for training.

## 6. Predictions and Outputs

The output of a model depends on the task it is designed to solve.

| Model Task | Input Example | Output Example |
|---|---|---|
| Classification | Voltage, temperature, leakage current | Pass or Fail |
| Regression | Voltage, clock frequency, temperature | Predicted power consumption |
| Clustering | Multiple wafer measurements | A cluster assignment |
| Anomaly Detection | Electrical test measurements | An anomaly score or flag |

The output should be interpreted according to the model's design and the requirements of the application.

## 7. Training and Inference

Training and inference are two different stages of using a Machine Learning model.

| Stage | Meaning | Example |
|---|---|---|
| Training | The model learns patterns and adjusts its parameters using training data. | Learning from historical chip test records. |
| Inference | The trained model processes new inputs to produce predictions. | Predicting the test result for a newly measured chip. |

Training may require substantial computation depending on the model and dataset. Inference uses the trained model to produce outputs and may need to meet latency or resource constraints.

## 8. Example: Semiconductor Pass/Fail Prediction

Consider a model trained to predict whether a semiconductor chip will pass or fail.

The input features are voltage, temperature, and leakage current. The target label is the actual test result, either Pass or Fail.

During training, the model learns relationships between the input measurements and the known results. The learning algorithm adjusts the model parameters to reduce the loss.

During inference, the trained model receives measurements from a new chip and produces a prediction. Engineers can compare the prediction with the actual test result to evaluate performance.

This prediction can assist engineering analysis, but it should not replace required production testing or safety and quality controls without appropriate validation.

## 9. Important Considerations

A Machine Learning model is only one part of a complete solution. Its usefulness also depends on data quality, appropriate feature selection, suitable training methods, and evaluation on representative data.

A model may perform well on its training data but poorly on unseen data. This can happen when the model overfits the training examples or when the training data does not represent real operating conditions.

Engineers should therefore examine both the model's internal learning process and its behaviour on new data.

## 10. Conclusion

Model anatomy explains the main components that allow a Machine Learning system to learn and make predictions. Input features provide information, learning algorithms adjust parameters, loss functions measure prediction errors, and trained models generate outputs during inference.

Understanding these components helps engineers interpret model behaviour and evaluate whether a model is appropriate for a particular application. In semiconductor engineering, this knowledge supports the responsible use of Machine Learning for test-result prediction, power estimation, and defect analysis.

## References

1. Google Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course
2. Scikit-learn User Guide: https://scikit-learn.org/stable/user_guide.html
3. IBM Machine Learning: https://www.ibm.com/think/topics/machine-learning
