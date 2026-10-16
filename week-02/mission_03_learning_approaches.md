# Mission 3: Understanding Machine Learning Approaches

## 1. Introduction

Machine Learning (ML) approaches describe how a model learns from data or interacts with its environment. The three major approaches are supervised learning, unsupervised learning, and reinforcement learning.

Each approach is suitable for different types of problems depending on the availability of labelled data and the objective of the task.

## 2. Supervised Learning

Supervised learning is a Machine Learning approach in which a model learns from labelled data. Each training sample contains input features and a known target or label. The model learns the relationship between the inputs and the target so that it can make predictions on new data.

Examples include classification and regression.

### Example

In semiconductor testing, a dataset may contain voltage, temperature, and leakage current measurements along with a Pass or Fail label. A supervised learning model can learn from these historical records to predict whether a new chip is likely to pass or fail.

### Applications

- Email spam detection
- House price prediction
- Medical image classification
- Semiconductor chip failure prediction

## 3. Unsupervised Learning

Unsupervised learning is a Machine Learning approach in which a model works with data that does not have predefined target labels. It identifies patterns, similarities, groups, or unusual observations in the data.

Clustering and dimensionality reduction are common unsupervised learning tasks.

### Example

In semiconductor manufacturing, unsupervised learning can group wafers with similar measurement patterns. Engineers can investigate these groups to identify possible process variations or recurring defect patterns.

### Applications

- Customer segmentation
- Grouping similar manufacturing records
- Detecting unusual wafer measurement patterns
- Exploring patterns in large datasets

## 4. Reinforcement Learning

Reinforcement learning is a Machine Learning approach in which an agent learns by interacting with an environment. The agent takes actions and receives rewards or penalties based on the outcomes. Over time, it learns a policy that aims to maximise cumulative reward.

The main elements are the agent, environment, action, state, and reward.

### Example

A reinforcement learning system could explore different settings in a simulated semiconductor manufacturing process. It receives rewards for meeting quality and efficiency objectives and penalties for undesirable outcomes. The system can learn a strategy through repeated interactions with the simulation.

Real manufacturing use would require careful validation and safety constraints before applying any learned strategy to production equipment.

### Applications

- Robotics
- Game-playing systems
- Resource allocation
- Process optimisation in simulated environments

## 5. Comparison of the Three Approaches

| Characteristic | Supervised Learning | Unsupervised Learning | Reinforcement Learning |
|---|---|---|---|
| Learning Data | Labelled data | Unlabelled data | Experience from interaction |
| Main Goal | Predict a target | Discover patterns or structure | Learn actions that maximise reward |
| Feedback | Known target labels | No predefined target labels | Rewards or penalties |
| Common Tasks | Classification and regression | Clustering and dimensionality reduction | Sequential decision-making |
| Example | Predicting chip Pass or Fail | Grouping similar wafer measurements | Optimising a simulated manufacturing process |
| Main Challenge | Obtaining reliable labelled data | Interpreting discovered patterns | Designing useful rewards and safe exploration |

## 6. How to Choose the Right Approach

The choice of Machine Learning approach depends on the problem and the available data.

- Use supervised learning when labelled examples are available and the goal is to predict a known outcome.
- Use unsupervised learning when labels are unavailable and the goal is to discover hidden patterns or groups.
- Use reinforcement learning when an agent must learn a sequence of actions through interaction and feedback from an environment.

For example, predicting chip failures from historical Pass or Fail records is a supervised learning problem. Grouping wafers by similarities in their measurements is an unsupervised learning problem. Learning a strategy to optimise a simulated process through rewards is a reinforcement learning problem.

## 7. Conclusion

Supervised, unsupervised, and reinforcement learning are three important Machine Learning approaches. Supervised learning uses labelled data to predict outcomes, unsupervised learning discovers patterns in unlabelled data, and reinforcement learning learns strategies through interaction and rewards.

Understanding these approaches helps engineers select an appropriate method for a particular problem. In semiconductor engineering, they can support failure prediction, pattern discovery, and process optimisation, provided the data and system are suitable for the chosen approach.

## References

1. Google Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course
2. IBM Machine Learning: https://www.ibm.com/think/topics/machine-learning
3. IBM Reinforcement Learning: https://www.ibm.com/think/topics/reinforcement-learning
