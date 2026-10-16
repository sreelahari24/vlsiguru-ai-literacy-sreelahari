# Week 02 — Final Reflection

## 1. Which concept became clearest to me, and how did I learn it?

The clearest concept for me was the difference between supervised, unsupervised, and reinforcement learning. I understood that supervised learning uses labelled data to predict outcomes, unsupervised learning identifies patterns in unlabelled data, and reinforcement learning learns through actions and rewards. Comparing these approaches and connecting them to semiconductor engineering examples helped me understand when each approach may be useful.

## 2. Which two concepts were confusing, and how did I distinguish them?

The first confusing concept was the difference between a Machine Learning algorithm and a model. I learned that an algorithm is the method used to learn from data, while a model is the learned system that makes predictions after training.

The second confusing concept was the difference between accuracy and recall. Accuracy measures the proportion of all predictions that are correct, while recall measures the proportion of actual positive cases that the model correctly identifies. The semiconductor failure detection example helped me understand why a model can have high accuracy but still miss important failures.

## 3. Which claim did I check against a reliable source, and what did I learn?

I checked the concept that a model should be evaluated on data that was not used during training. Educational material from Google's Machine Learning Crash Course helped me understand the importance of evaluating models on separate data and checking whether they generalise to unseen examples. This showed me that good training performance alone does not prove that a model will perform reliably in real-world situations.

Reference: https://developers.google.com/machine-learning/crash-course

## 4. Which stage of the Machine Learning lifecycle is easiest to underestimate, and why?

I think data preparation is one of the easiest stages to underestimate. A model depends on the quality of the data used to train it. Missing values, incorrect measurements, duplicate records, inconsistent units, and class imbalance can affect its predictions. In semiconductor engineering, incorrect electrical measurements could lead to unreliable failure predictions. Therefore, data validation and preparation are essential before model training.

## 5. What question do I still have before learning more deeply?

My main question is: How can Machine Learning be integrated into VLSI Physical Design and DFT workflows to improve timing prediction, test prioritisation, or failure analysis without replacing established engineering verification and sign-off methods?

I would like to explore practical examples where Machine Learning models are evaluated using real engineering data and compared with conventional methods.

## Conclusion

This week's assignment helped me understand the fundamentals of Machine Learning, including data, learning approaches, model anatomy, evaluation, generalisation, and common failure modes. I also learned that Machine Learning is not always the best solution and that rule-based methods may be more suitable for clearly defined problems.

As a VLSI DFT learner, I see potential for Machine Learning in semiconductor testing and failure analysis. However, I understand that reliable data, careful evaluation, engineering judgement, and proper validation are necessary before using ML predictions in practical applications.
