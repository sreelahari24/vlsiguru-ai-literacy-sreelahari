# Mission 1 - AI and ML Landscape

## 1. Introduction

Artificial Intelligence (AI), Machine Learning (ML), Deep Learning (DL), and Generative AI are related concepts used to build intelligent systems. Understanding their differences helps us identify which technology is suitable for a particular problem.

## 2. Definitions

### Artificial Intelligence (AI)

Artificial Intelligence is a broad field of computer science that focuses on creating systems capable of performing tasks that normally require human intelligence, such as reasoning, problem-solving, planning, and understanding language.

Example: A rule-based system that checks whether a temperature exceeds a predefined limit and raises an alarm.

### Machine Learning (ML)

Machine Learning is a subset of AI that enables computers to learn patterns from data and make predictions or decisions without explicitly programming every rule.

Example: A model trained on historical semiconductor test data to predict whether a chip is likely to pass or fail.

### Deep Learning (DL)

Deep Learning is a subset of Machine Learning that uses artificial neural networks with multiple layers to learn complex patterns from large amounts of data.

Example: A deep learning model that analyses images to identify defects in semiconductor wafers.

### Generative AI

Generative AI refers to AI systems that generate new content, such as text, images, audio, video, or computer code. Many modern generative AI systems use deep learning models.

Example: An AI assistant that generates Verilog code from a written description of a digital circuit.

## 3. Relationship Between AI, ML, DL, and Generative AI

AI is the broadest field. Machine Learning is one approach within AI, and Deep Learning is one approach within Machine Learning. Generative AI describes systems that create new content and often uses deep learning.

The relationship can be represented as follows:

AI
- Rule-based systems
- Machine Learning
  - Supervised Learning
  - Unsupervised Learning
  - Reinforcement Learning
  - Deep Learning
    - Neural networks used in many generative AI systems

Generative AI and Deep Learning are related, but they are not identical. Not every AI system uses Machine Learning, and not every Machine Learning model is a deep learning model.

## 4. Examples and Classification

### Example 1: Rule-Based Temperature Alarm

A system raises an alarm whenever the temperature exceeds a predefined threshold.

Classification: Rule-based automation or AI.

Reason: The system follows an explicitly programmed rule rather than learning the threshold or behaviour from training examples.

### Example 2: Semiconductor Pass/Fail Prediction

A model learns from historical semiconductor test measurements and their verified pass/fail labels to predict the outcome for a new test record.

Classification: Machine Learning, specifically supervised classification.

Reason: The model learns a relationship between input measurements and known output labels.

### Example 3: Defect Detection Using Neural Networks

A neural network is trained on labelled wafer images to identify possible manufacturing defects.

Classification: Deep Learning.

Reason: Deep learning uses multi-layer neural networks to learn complex patterns from data.

### Example 4: Generating Verilog Code

An AI system generates a Verilog module based on a written description of a digital circuit.

Classification: Generative AI.

Reason: The system generates new content in the form of computer code. The generated code must still be reviewed and verified.

## 5. Comparison Table

| Concept | Meaning | Example |
|---|---|---|
| Artificial Intelligence (AI) | The broader field of making machines perform tasks that require intelligence. | A rule-based system that raises an alarm when temperature exceeds a limit. |
| Machine Learning (ML) | A subset of AI in which systems learn patterns from data. | Predicting semiconductor test failures using historical test data. |
| Deep Learning (DL) | A subset of ML that uses neural networks with multiple layers. | Detecting wafer defects from images. |
| Generative AI | AI that generates new content based on learned patterns. | Generating Verilog code suggestions from a prompt. |

## 6. Importance in Semiconductor Engineering

AI and Machine Learning can support semiconductor engineering by analysing test data, identifying unusual patterns, predicting possible failures, and helping engineers prioritise investigations.

For example, a supervised ML model could learn from historical test measurements and verified outcomes to identify records that may need further inspection. However, its predictions must be evaluated using representative data and appropriate metrics. It should not replace mandatory test limits or engineering verification without proper validation and approval.

## 7. Limitations and Risks

- Machine Learning depends on the quality and representativeness of the training data.
- Incorrect labels can cause a model to learn incorrect relationships.
- Deep Learning models may require substantial computing resources and can be difficult to interpret.
- Generative AI can produce incorrect information or code that does not work as intended.
- Model performance can decrease when real-world data differ from training data.
- Predictions should be verified before being used in important engineering decisions.

## 8. Conclusion

AI is the broad field of creating intelligent systems. Machine Learning enables systems to learn patterns from data, while Deep Learning uses multi-layer neural networks to learn complex representations. Generative AI creates new content such as text, images, and code.

Understanding these concepts helps engineers select appropriate tools for different problems. In semiconductor engineering, ML can assist with analysing data and identifying patterns, but reliable data, careful evaluation, and human verification remain essential.

## 9. References

1. Google Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course
2. IBM - What Is Machine Learning?: https://www.ibm.com/think/topics/machine-learning
3. Kaggle Learn: https://www.kaggle.com/learn

These references provide introductory learning material about Machine Learning and related concepts. Consult the relevant sections when verifying the definitions and examples used in this mission.
