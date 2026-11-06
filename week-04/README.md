# Week 04 – Data & Deep Learning Foundations

## Overview

Week 04 focuses on understanding how data is prepared for deep learning, how neural networks are structured, how they learn from examples and how deep learning can be applied to real-world engineering problems.

This week explores the journey from raw data to trained neural networks and their predictions.

The main focus is on understanding neural network components, training processes, model complexity, data quality and practical applications in semiconductor manufacturing.

## Learning Objectives

Through this assignment, I explored:

- How raw data is converted into numerical inputs for neural networks.
- The importance of data preparation, labelling and normalisation.
- Differences between rule-based systems, traditional machine learning and deep learning.
- The structure and components of neural networks.
- How neural networks learn through forward propagation, loss calculation and backpropagation.
- The relationship between model complexity and classification performance.
- Applications of deep learning in semiconductor manufacturing.

## Missions Completed

### Mission 1 – Data Behind Deep Learning

Studied how raw images are converted into numerical inputs and why data preparation is important before training a neural network.

Topics covered:
- Pixels and numerical image representation.
- Data cleaning, resizing and normalisation.
- Labels and labelled datasets.
- Data quality and class imbalance.
- Training, validation and test datasets.

**Deliverable:** Data preparation workflow and explanations.

[View Mission 1 – Data Behind Deep Learning](data_behind_deep_learning.md)

### Mission 2 – What Makes Deep Learning Different?

Explored the differences between rule-based systems, traditional machine learning and deep learning.

Topics covered:
- Relationship between AI, ML and DL.
- Neural networks and interconnected neurons.
- Learning patterns from data.
- Applications of deep learning.
- Model complexity and limitations.

**Deliverable:** Comparison table and explanations with engineering examples.

[View Mission 2 – ML vs Deep Learning](ml_vs_deep_learning.md)

### Mission 3 – Open the Neural Network

Explored the internal structure of a neural network and how information moves through its layers.

Topics covered:
- Input layer.
- Hidden layers.
- Output layer.
- Neurons and nodes.
- Weights and biases.
- Activation functions.

**Deliverable:** Labelled neural network diagram for semiconductor defect detection.

[View Neural Network Diagram](neural_network_diagram.png)

### Mission 4 – How Does a Neural Network Learn?

Studied how a neural network improves its predictions through repeated training.

Topics covered:
- Forward pass.
- Loss function.
- Optimisation.
- Backpropagation.
- Epochs.
- Training versus inference.
- Generalisation and overfitting.

**Deliverable:** Neural network learning flowchart and explanation of the training process.

[View Mission 4 – How Neural Networks Learn](how_neural_networks_learn.md)

### Mission 5 – Experiment and Observe

Performed an interactive experiment using TensorFlow Neural Network Playground to investigate the relationship between network complexity and classification performance.

Two configurations were compared using the Circle dataset.

**Experiment A:**
- Two hidden layers.
- Four and two neurons.
- Training loss: 0.000.
- Test loss: 0.000.
- Epoch: 1,517.

**Experiment B:**
- Three hidden layers.
- Four, two and two neurons.
- Training loss: 0.000.
- Test loss: 0.000.
- Epoch: 1,513.

Both networks successfully learned the Circle classification pattern.

**Observation:** Increasing the number of hidden layers did not produce a visible improvement in the displayed loss values in this experiment.

**Deliverables:** Experiment comparison, observations and screenshots.

[View Mission 5 – Playground Experiment](playground_experiment.md)

[Baseline Experiment Screenshot](playground_baseline.png)

[Modified Experiment Screenshot](playground_three_hidden_layers.png)

## Final Challenge – Engineering Case Study

### Deep Learning-Based Semiconductor Wafer Defect Detection

Investigated how deep learning can be applied to identify defects in semiconductor wafer inspection images.

The case study covered:
- Semiconductor manufacturing defects.
- Input image data and preparation.
- CNN-based defect classification.
- Comparison with traditional machine learning and rule-based approaches.
- Model evaluation metrics.
- False positives and false negatives.
- Human review and engineering judgement.
- Published research on semiconductor wafer defect classification.

**Deliverable:** Engineering case study supported by two research papers.

[View Engineering Case Study](engineering_case_study.md)

## Sources and References

Consulted Google Machine Learning Crash Course, TensorFlow Neural Network Playground and published research papers on semiconductor wafer defect classification.

[View Sources and References](sources.md)

## Final Reflection

This assignment helped me understand how neural networks process data, learn patterns and generate predictions.

The interactive experiment helped me investigate how network complexity affects classification performance.

The semiconductor case study helped me connect deep learning concepts with practical engineering applications.

I also developed a better understanding of the importance of data quality, model evaluation and generalisation.

[View Final Reflection](reflection.md)

## Key Takeaways

1. Data quality and preparation directly influence what a neural network can learn.
2. Deep learning uses multi-layer neural networks to identify complex patterns.
3. Weights, biases and activation functions play important roles in neural network computation.
4. Backpropagation and optimisation help neural networks improve their predictions.
5. Increasing network complexity does not automatically guarantee better performance.
6. Testing on unseen data is essential for evaluating generalisation.
7. Deep learning can support semiconductor defect detection, but engineering verification remains important.

## Conclusion

Week 04 provided an understanding of data preparation, neural network architecture, deep learning and model training.

Through research, interactive experimentation and an engineering case study, I explored how neural networks learn patterns from data and how they can be applied to semiconductor manufacturing problems.

This week helped strengthen my understanding of deep learning fundamentals and their relevance to engineering applications.
