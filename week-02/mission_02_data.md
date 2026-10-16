# Mission 2: Understanding Data in Machine Learning

## 1. Introduction

Data is the foundation of Machine Learning (ML). Machine Learning algorithms use data to identify patterns, learn relationships, and make predictions. The quality and quantity of data can directly affect the performance of an ML model.

In semiconductor engineering, data can come from wafer testing, manufacturing processes, circuit simulations, and chip validation.

## 2. Important Data Terminology

| Term | Meaning | Example |
|---|---|---|
| Dataset | A collection of data used for analysis or model development. | Semiconductor chip test records. |
| Feature | An input variable used by a model to make a prediction. | Operating temperature or leakage current. |
| Label | The target value that the model learns to predict in supervised learning. | Pass or Fail. |
| Sample | One individual record in a dataset. | Test results for one chip. |
| Training Data | Data used to train the model. | Historical chip test records used for learning. |
| Testing Data | Separate data used to evaluate the trained model. | Unseen chip test records used to measure performance. |

## 3. Example Dataset

The following is an illustrative semiconductor testing dataset. It is created for learning purposes and does not represent real factory data.

| Chip ID | Voltage (V) | Temperature (°C) | Leakage Current (mA) | Test Result |
|---|---:|---:|---:|---|
| C001 | 1.0 | 40 | 2.1 | Pass |
| C002 | 1.0 | 45 | 2.5 | Pass |
| C003 | 0.9 | 70 | 8.2 | Fail |
| C004 | 1.1 | 50 | 3.0 | Pass |
| C005 | 0.9 | 75 | 9.1 | Fail |
| C006 | 1.0 | 65 | 6.8 | Fail |
| C007 | 1.1 | 42 | 2.3 | Pass |
| C008 | 0.9 | 68 | 7.5 | Fail |

In this dataset, voltage, temperature, and leakage current are features. The test result is the label. Chip ID identifies each sample and would generally not be used as a predictive feature because it does not represent a meaningful electrical characteristic.

A supervised learning model could learn relationships between the electrical measurements and the test result. However, this small illustrative dataset is not sufficient to build a reliable real-world production model.

## 4. Data Quality Issues

Data quality is important because incomplete or incorrect data can lead to unreliable predictions.

| Data Quality Issue | Meaning | Semiconductor Example |
|---|---|---|
| Missing Values | Some values are unavailable. | Temperature is not recorded for a chip. |
| Duplicate Records | The same record appears more than once. | A chip test result is stored twice. |
| Incorrect Values | Values are recorded incorrectly. | Leakage current is entered with the wrong unit. |
| Inconsistent Units | Measurements use different units. | Some current values are recorded in µA and others in mA. |
| Class Imbalance | One label occurs much more frequently than another. | Most chips pass, while very few fail. |
| Outliers | Values differ significantly from typical observations. | An unusually high leakage current measurement. |

## 5. Why Data Quality Matters

Poor-quality data can cause an ML model to learn incorrect patterns. Missing values, measurement errors, duplicate records, and unrepresentative samples can reduce prediction accuracy.

For example, if a semiconductor dataset contains incorrect leakage current measurements, a model may learn the wrong relationship between leakage current and chip failure.

Before training a model, the data should be inspected, cleaned, validated, and checked for missing values, duplicates, incorrect units, and unusual observations.

Data cleaning must be performed carefully. Outliers should not automatically be removed because they may represent genuine manufacturing defects or important failure conditions.

## 6. Training Data and Testing Data

A dataset is commonly divided into training and testing portions.

- Training data is used by the learning algorithm to identify patterns.
- Testing data is used to evaluate the model on records that were not used during training.

For example, historical semiconductor test records can be divided into training and testing sets. The model learns from the training records, and its predictions are compared with the actual labels in the test set.

Data leakage must be avoided. Information from the test set should not influence model training or preprocessing decisions. Otherwise, the evaluation may give an overly optimistic estimate of model performance.

## 7. Conclusion

Data is a fundamental component of Machine Learning. Understanding datasets, features, labels, samples, and data quality helps engineers prepare reliable data for model development.

In semiconductor engineering, good-quality data from manufacturing, testing, and validation can support defect detection, failure prediction, and process monitoring. However, the usefulness of an ML model depends on the quality, relevance, and representativeness of the data.

## References

1. Google Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course
2. IBM Machine Learning: https://www.ibm.com/think/topics/machine-learning
3. Kaggle Learn: https://www.kaggle.com/learn
