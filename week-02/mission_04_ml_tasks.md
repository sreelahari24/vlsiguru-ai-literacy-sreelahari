# Mission 4: Understanding Machine Learning Task Types

## 1. Introduction

Machine Learning tasks describe the type of problem a model is designed to solve. Different tasks are selected depending on the expected output and the problem requirements.

The major Machine Learning task types include classification, regression, clustering, anomaly detection, dimensionality reduction, and recommendation or ranking.

Understanding these tasks helps engineers choose an appropriate approach for a particular application.

## 2. Classification

Classification is a supervised Machine Learning task in which a model predicts a category or class label.

The output is a discrete category rather than a continuous numerical value.

Example: A semiconductor testing model predicts whether a chip will Pass or Fail based on its voltage, temperature, and leakage current measurements.

Applications:
- Email spam detection
- Image recognition
- Disease classification
- Semiconductor defect classification

## 3. Regression

Regression is a supervised Machine Learning task in which a model predicts a continuous numerical value.

Example: A model predicts the expected power consumption of a chip using operating voltage, clock frequency, and temperature.

Applications:
- House price prediction
- Temperature forecasting
- Power consumption estimation
- Manufacturing yield estimation

## 4. Clustering

Clustering is an unsupervised Machine Learning task that groups data points based on similarities. It does not require predefined class labels.

Example: A model groups semiconductor wafers with similar electrical measurement patterns so that engineers can investigate possible manufacturing variations.

Applications:
- Customer segmentation
- Grouping similar manufacturing records
- Organising unlabeled images
- Discovering patterns in sensor data

## 5. Anomaly Detection

Anomaly detection identifies observations that differ significantly from normal or expected patterns. Depending on the method, it can use labelled or unlabelled data.

Example: A model flags a chip with unusually high leakage current compared with typical measurements for similar chips.

Applications:
- Detecting unusual sensor readings
- Identifying suspicious transactions
- Finding manufacturing defects
- Monitoring equipment behaviour

## 6. Dimensionality Reduction

Dimensionality reduction reduces the number of variables or features in a dataset while attempting to preserve important information.

It can make high-dimensional data easier to visualise, analyse, and process. Principal Component Analysis (PCA) is a commonly used technique.

Example: A semiconductor dataset may contain hundreds of electrical measurements. Dimensionality reduction can represent the data using fewer combined variables to help engineers explore patterns.

Applications:
- Data visualisation
- Simplifying complex datasets
- Feature extraction
- Reducing computational requirements

## 7. Recommendation and Ranking

Recommendation systems suggest relevant items to users or systems. Ranking systems order items according to their relevance, predicted value, or priority.

These tasks can use different Machine Learning techniques, including supervised learning and collaborative filtering.

Example: A manufacturing analysis system ranks semiconductor test cases according to their predicted likelihood of detecting important failures, helping engineers prioritise testing.

Applications:
- Product recommendations
- Search result ranking
- Content recommendations
- Prioritising semiconductor test cases

## 8. Comparison of Machine Learning Task Types

| Task Type | Main Purpose | Typical Output | Example |
|---|---|---|---|
| Classification | Predict a category | Discrete class label | Chip Pass or Fail |
| Regression | Predict a numerical value | Continuous number | Predicted chip power consumption |
| Clustering | Group similar observations | Groups or clusters | Grouping wafers by measurement patterns |
| Anomaly Detection | Identify unusual observations | Anomaly score or flag | Detecting unusually high leakage current |
| Dimensionality Reduction | Reduce the number of features | Smaller feature representation | Simplifying hundreds of wafer measurements |
| Recommendation and Ranking | Suggest or order relevant items | Recommendations or ordered list | Ranking semiconductor test cases |

## 9. Choosing the Appropriate Task

The task type depends on the desired output.

- If the output is a category, classification may be appropriate.
- If the output is a continuous numerical value, regression may be appropriate.
- If the goal is to discover groups in unlabelled data, clustering may be appropriate.
- If the goal is to identify unusual observations, anomaly detection may be appropriate.
- If the dataset contains many features and needs a simpler representation, dimensionality reduction may be appropriate.
- If the goal is to suggest items or prioritise them, recommendation or ranking may be appropriate.

Some problems can use more than one task. For example, semiconductor failure analysis may use anomaly detection to flag unusual measurements and classification to predict a specific defect category.

## 10. Conclusion

Machine Learning includes several task types, each designed to address a different problem. Classification predicts categories, regression predicts numerical values, clustering discovers groups, anomaly detection identifies unusual observations, dimensionality reduction simplifies feature representations, and recommendation or ranking helps identify relevant items or priorities.

In semiconductor engineering, these tasks can support chip testing, failure analysis, power estimation, manufacturing monitoring, and test prioritisation. Selecting the correct task is an important step in designing a useful Machine Learning solution.

## References

1. Google Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course
2. IBM Machine Learning: https://www.ibm.com/think/topics/machine-learning
3. Scikit-learn User Guide: https://scikit-learn.org/stable/user_guide.html
