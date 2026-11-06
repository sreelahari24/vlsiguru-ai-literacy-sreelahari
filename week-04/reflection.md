# Week 04 – Final Reflection

## 1. What is the most important difference between traditional machine learning and deep learning?

Traditional machine learning generally depends on manually selected or extracted features to identify patterns in data, whereas deep learning uses multi-layer neural networks to automatically learn complex features.

Deep learning is particularly useful for complex data such as images, audio and text.

I understood that deep learning is not always better than traditional machine learning. The most suitable approach depends on the problem, available data and computational resources.

## 2. How does data preparation affect what a neural network can learn?

Data preparation directly affects the quality of learning.

If a dataset contains incorrect labels, duplicate images, noisy inputs or class imbalance, the neural network may learn incorrect or misleading patterns.

Cleaning, labelling, normalisation and proper dataset splitting help improve the reliability of training and evaluation.

I learned that even a well-designed neural network may produce poor predictions if the training data is not properly prepared.

## 3. What happens inside a neural network when it learns from examples?

A neural network receives numerical input data and processes it through interconnected layers.

During a forward pass, the network uses weights, biases and activation functions to produce a prediction.

A loss function measures the difference between the predicted output and the actual target.

Backpropagation calculates gradients, and an optimisation algorithm uses these gradients to update the network's weights and biases.

This process repeats over multiple training iterations so that the network can gradually improve its predictions.

## 4. What did your TensorFlow Playground experiment reveal about model complexity?

I compared two neural network configurations using the Circle classification dataset.

Experiment A contained two hidden layers with 4 and 2 neurons, while Experiment B contained three hidden layers with 4, 2 and 2 neurons.

The baseline network was trained for 1,517 epochs, and the modified network was trained for 1,513 epochs.

Both experiments displayed training and test loss values of 0.000, rounded to three decimal places.

Both networks successfully separated the central blue points from the surrounding orange points.

This experiment helped me understand that adding more hidden layers does not automatically improve a model's performance. A simpler network may already be sufficient for a particular classification problem.

## 5. What is one technical claim you verified using a reliable source?

I investigated the claim that Convolutional Neural Networks can be used for semiconductor wafer defect classification.

A research paper published in Applied Sciences in 2020, titled "Inspection and Classification of Semiconductor Wafer Surface Defects Using CNN Deep Learning Networks," demonstrated the use of CNNs to classify different wafer defect patterns.

The study investigated four defect categories: center, local, random and scrape.

This provided research evidence that CNN-based methods can be useful for semiconductor wafer defect classification.

Reference:
https://www.mdpi.com/2076-3417/10/15/5340

## 6. What remains unclear about neural networks, their training or the data they use?

I would like to understand more about how weights and biases are updated mathematically during backpropagation.

I am also interested in understanding how activation functions, learning rates and optimisation algorithms influence training performance.

Another area I would like to explore is how neural networks can be implemented efficiently on hardware while maintaining accuracy and reducing computational requirements.

## 7. What question would you like answered during the Saturday masterclass?

How can a neural network trained using software frameworks be implemented efficiently on FPGA hardware, and what challenges arise when converting trained models into hardware implementations using fixed-point arithmetic and limited memory resources?

## 8. Overall Learning

During Week 04, I learned about data preparation, traditional machine learning, deep learning, neural network architecture and the training process.

I understood the roles of input layers, hidden layers, output layers, neurons, weights, biases and activation functions.

Through TensorFlow Playground, I observed how neural network configurations affect learning behaviour and classification results.

The engineering case study helped me connect deep learning concepts to semiconductor wafer defect detection.

Overall, this week helped me understand that developing a reliable deep learning system requires not only a suitable neural network architecture but also good-quality data, proper training, careful evaluation and engineering judgement.
