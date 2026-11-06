# Mission 2 – What Makes Deep Learning Different?

## 1. Introduction

Artificial Intelligence (AI), Machine Learning (ML) and Deep Learning (DL) are closely related concepts, but they have different meanings and applications.

Artificial Intelligence is the broader field of developing machines that can perform tasks that normally require human intelligence.

Machine Learning is a subset of Artificial Intelligence in which machines learn patterns from data and use those patterns to make predictions or decisions without being explicitly programmed for every situation.

Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers to learn complex patterns from large amounts of data.

Neural networks are computational models made up of interconnected processing units called neurons. Deep learning uses these networks with multiple layers to process information and learn complex relationships.

The relationship can be represented as:

**Artificial Intelligence → Machine Learning → Deep Learning**

Neural networks are the main computational models used in deep learning.

## 2. Difference Between Rule-Based Systems, Traditional Machine Learning and Deep Learning

### A. Rule-Based System

A rule-based system follows predefined instructions written by humans. It makes decisions using conditions such as IF and ELSE.

For example, in semiconductor inspection, an engineer can define a rule that flags an image if a measured defect size exceeds a specified threshold.

The system follows these predefined rules but does not independently learn new patterns from data.

### B. Traditional Machine Learning

Traditional machine learning algorithms learn patterns from data using selected features.

For example, engineers may extract features such as defect size, shape, brightness and texture from semiconductor inspection images. A machine learning algorithm can use these features to classify images as defective or non-defective.

The quality of feature extraction can strongly influence the model's performance.

### C. Deep Learning

Deep learning uses neural networks with multiple layers to learn useful features and complex patterns directly from data.

For semiconductor inspection, a deep learning model can process image pixels and learn visual patterns associated with defects.

Unlike traditional machine learning, it can automatically learn many relevant features without requiring engineers to manually define every feature.

However, deep learning generally requires sufficient training data and computational resources.

## 3. Comparison Between Different Approaches

| Approach | How It Works | Type of Problem | Example | Limitation |
|---|---|---|---|---|
| Rule-Based System | Uses predefined rules and conditions written by humans. | Problems with clearly defined conditions. | Identifying a semiconductor defect when its measured size exceeds a fixed threshold. | Cannot easily adapt to new or complex patterns. |
| Traditional Machine Learning | Learns patterns from data using selected or manually extracted features. | Classification and prediction using structured data or extracted features. | Classifying semiconductor defects using defect size, shape and texture. | Depends on feature selection and extraction. |
| Deep Learning | Uses multi-layer neural networks to automatically learn complex patterns from data. | Complex problems involving images, audio and text. | Identifying semiconductor defects directly from inspection images. | Often requires large datasets, more computing power and careful evaluation. |

## 4. What Is a Neural Network and Why Is It Made Up of Interconnected Units?

A neural network is a computational model inspired by the interconnected structure of biological neurons.

It consists of small processing units called neurons or nodes, which are organised into different layers.

Each neuron receives numerical inputs, processes them using weights and biases, applies an activation function and passes the result to the next layer.

Neurons are interconnected because information needs to move from one processing unit to another during computation.

These connections allow the network to identify relationships and learn patterns from training data.

During training, the network adjusts its weights and biases to improve its predictions.

For example, in semiconductor defect detection, different neurons and layers can learn visual features such as edges, shapes and textures that help identify possible defects.

## 5. What Does It Mean for a Model to Learn Useful Patterns from Data?

Learning useful patterns means identifying relationships and characteristics in training data that can help a model make predictions on new examples.

A model receives input data and produces predictions. During training, these predictions are compared with the actual answers, and the resulting errors are used to update the model's parameters.

As training continues, the model gradually improves its ability to recognise relevant patterns.

For example, a deep learning model trained on semiconductor inspection images may learn visual patterns associated with scratches, cracks and other manufacturing defects.

After training, it can use the learned patterns to predict whether a new inspection image contains a defect.

## 6. Why Is Deep Learning Useful for Complex Inputs Such as Images, Audio and Language?

Deep learning is useful for complex inputs because it can automatically learn different levels of features from large amounts of data.

For example, in image processing:

- Early layers may learn simple patterns such as edges and lines.
- Intermediate layers may learn shapes and textures.
- Deeper layers may learn more complex visual structures associated with objects or defects.

In audio processing, deep learning models can learn patterns in sound signals to recognise spoken words.

In natural language processing, they can learn relationships between words and sentences to perform tasks such as translation and text generation.

This ability to learn complex features makes deep learning useful in applications where manually identifying every important feature would be difficult.

## 7. Does Adding More Layers Automatically Make a Model More Accurate or Useful?

No. Adding more layers does not automatically make a neural network more accurate or useful.

A deeper network may learn more complex patterns, but increasing network complexity can also introduce several challenges.

Some of these challenges include:

- **More training data:** Complex networks may require larger datasets to learn effectively.
- **Higher computational requirements:** More layers and neurons can increase memory and processing requirements.
- **Longer training time:** Training a complex network may take more time.
- **Overfitting:** A model may memorise training examples instead of learning patterns that generalise to new data.
- **Poor generalisation:** A complex model may perform well on training data but poorly on unseen examples.

Therefore, network complexity should be selected based on the problem, available data and evaluation results rather than simply increasing the number of layers.

## 8. When Might a Simple Rule or Traditional ML Model Be Better Than Deep Learning?

Deep learning is not always the best solution for every problem.

A simple rule-based system may be suitable when the problem has clearly defined conditions and fixed decision rules.

For example, if a semiconductor inspection system needs to flag a defect whenever its measured size exceeds a specified threshold, a rule-based approach may be sufficient.

Traditional machine learning may be more suitable when the dataset is relatively small, the important features are already known and the problem can be solved using simpler algorithms.

For example, an ML algorithm can classify semiconductor defects using manually extracted features such as size, shape and brightness.

Deep learning may be a better option when the problem involves complex visual patterns that are difficult to identify manually.

The choice of approach should depend on the problem requirements, available data, computational resources and expected performance.

## 9. Example Outside the Semiconductor Industry

One example of deep learning outside semiconductor manufacturing is speech recognition.

Speech recognition systems convert spoken language into written text.

A deep learning model processes audio signals and learns patterns associated with different sounds, words and language structures.

It can use these learned patterns to recognise spoken words and generate corresponding text.

Examples of applications include:

- Voice assistants.
- Speech-to-text applications.
- Automated transcription systems.
- Voice-controlled devices.

This demonstrates how deep learning can be applied to complex data beyond semiconductor inspection images.

## 10. Conclusion

Traditional machine learning and deep learning are both approaches used to learn patterns from data, but they differ in how they process information.

Traditional machine learning generally depends on manually selected or extracted features, whereas deep learning uses multi-layer neural networks to automatically learn complex features.

Deep learning is particularly useful for complex data such as images, audio and text. However, it often requires more training data, computational resources and careful evaluation.

A simple rule-based system or traditional machine learning model may sometimes be more practical than a complex deep learning model.

Therefore, the most suitable approach depends on the nature of the problem, available data, complexity and performance requirements.

Through this mission, I understood that deep learning is not always the best solution. Choosing the right approach for a particular engineering problem is more important than simply selecting the most complex model.
