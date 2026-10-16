# Week 01 Questions

## Q1. AI → ML → Deep Learning → Generative AI → Agents

### A. Artificial Intelligence (AI)

Artificial Intelligence (AI) is the broader concept of making computers or machines perform tasks that normally need some form of human intelligence. These tasks can include understanding information, recognising things, solving problems, making decisions, and responding to people.

**Example:** Voice assistants such as Siri or Google Assistant can understand a user's request and provide a response.

### B. Machine Learning (ML)

Machine Learning (ML) is a part of AI where a computer learns patterns from data instead of depending only on rules written manually by a programmer. After learning from existing data, the system can use those patterns to make predictions or decisions on new data.

**Example:** An email spam filter can learn from previous spam and non-spam emails and use those patterns to identify new spam messages.

### C. Deep Learning (DL)

Deep Learning is a type of machine learning that uses neural networks with multiple layers to learn more complex patterns from data. It is commonly used for tasks such as image recognition, speech recognition, and language-related applications.

**Example:** Face recognition on a smartphone can use deep learning to recognise a person from an image.

### D. Generative AI

Generative AI refers to AI systems that can create new content based on an input or prompt. The content can be text, images, audio, video, or code. Many modern generative AI systems are built using deep-learning models.

**Example:** An AI tool can generate an email or image when a user gives it a short instruction about what the content should contain.

### E. AI Agent

An AI agent is a system that can work toward a particular goal by deciding what steps are needed and using available tools or information. An agent is therefore more than just generating an answer to a prompt.

**Example:** A travel-planning agent could take a user's travel requirements, search available options using connected tools, compare them, and help complete the required travel-related tasks.

### Concept Map

```text
Artificial Intelligence (AI)
          |
          v
Machine Learning (ML)
          |
          v
Deep Learning (DL)
          |
          v
Many modern Generative AI systems

AI Agent
   |
   v
Goal + Model + Tools
   |
   v
Planning and Actions
   |
   v
Task Completion
```

### E — Evidence

I cross-checked the definitions with IBM's published information and found that the explanations conveyed the same main ideas.

**Source:** [IBM — What Is Artificial Intelligence?](https://www.ibm.com/think/topics/artificial-intelligence)

### V — Verification

I compared the definitions from the sources instead of relying only on one explanation. The relationship between AI, machine learning, and deep learning was consistent across the sources: AI is the broader field, machine learning is a subset of AI, and deep learning is a type of machine learning.

I also checked the difference between generative AI and AI agents. Generative AI mainly focuses on creating content from an input or prompt, while an AI agent can use an AI model as part of a larger workflow involving a goal, tools, decision-making, and actions.

### R — Reflection

Before looking into the topic, I thought AI, machine learning, and generative AI were almost the same thing. After checking the sources, I understood that they describe different but related ideas. Machine learning and deep learning are approaches used to build AI systems, while generative AI describes systems that can create new content.

I also learned that an AI agent is different from simply generating a response because it can use tools and take steps toward completing a goal.

---

## Q2. Is Everything That Looks Intelligent Actually AI?

### Classification Table

| Example | Classification | Reason |
|---|---|---|
| A. Calculator produces `25 × 16 = 400` | Traditional software | It follows fixed mathematical instructions and does not learn from data. |
| B. Program displays `WARNING` if temperature is above 80°C | Traditional software | It follows an explicitly written rule: if the temperature is above 80°C, show the warning. |
| C. Email system identifies spam using learned patterns | Machine-learning-based AI | It learns patterns from previous email data and uses them to identify new spam messages. |
| D. AI assistant writes a document summary | Generative AI | It generates new text based on the information provided in the document. |
| E. Navigation application predicts ETA using traffic and historical data | Machine-learning-based AI | It uses data and learned patterns to predict future travel time. |

A program that follows fixed instructions will produce an output based on rules that were explicitly programmed. A machine-learning system can learn patterns from data and use them when dealing with new inputs. Generative AI goes further by producing new content such as text.

### E — Evidence

I checked the machine-learning examples using Google's published explanations of machine learning.

- [Google — How Machine Learning in G Suite Makes People More Productive](https://blog.google/products-and-platforms/products/workspace/how-machine-learning-g-suite-makes-people-more-productive/)
- [Google — How AI Helps Predict Traffic and Determine Routes](https://blog.google/products-and-platforms/products/maps/google-maps-101-how-ai-helps-predict-traffic-and-determine-routes/)

The first source describes machine learning being used for spam detection, and the second explains that Google Maps uses machine learning with live and historical traffic data to predict traffic and ETAs.

### V — Verification

I checked whether each example depends on fixed instructions, learned patterns, or content generation. The calculator and temperature warning use explicitly defined rules, while spam detection and ETA prediction use learned patterns from data. The document summary is different because the system generates new text.

### R — Reflection

This question helped me understand that something can look intelligent without actually being AI. A fixed rule can produce a useful automatic result without learning anything. Machine learning is different because it can learn patterns from data and use them on new inputs. Generative AI is mainly focused on creating new content.

---

## Q3. What Happens When You Ask an LLM a Question?

When I send a prompt to a Large Language Model (LLM), the text is first broken into smaller units called tokens. The model uses the tokens in the prompt and the available context to understand what has been provided. It then calculates probabilities for possible next tokens and selects one. This process continues one token at a time until the response is generated.

### Important Terms

| Term | Meaning |
|---|---|
| Prompt | The input or instruction given to the model. |
| Token | A small unit of text that the model processes. |
| Context | The information available to the model while generating the response. |
| Probability | A value representing how likely a possible next token is. |
| Next-token prediction | Choosing the next token based on the previous tokens and context. |
| Generated response | The final sequence of tokens produced by the model. |

Training is the stage where the model learns patterns from large amounts of data. Inference is when the trained model is used to generate an answer for a new prompt.

### Flow Diagram

```text
Prompt
  |
  v
Tokens
  |
  v
Model Processing + Context
  |
  v
Probability Distribution
  |
  v
Next-Token Selection
  |
  v
More Tokens Predicted
  |
  v
Generated Response
```

An LLM can produce fluent language because it has learned many patterns from its training data. However, fluency does not guarantee that every statement is true. The model generates likely text, so it can sometimes produce information that is incorrect, incomplete, or unsupported.

### E — Evidence

**Source:** [IBM — What Is a Large Language Model?](https://www.ibm.com/think/topics/large-language-models)

### V — Verification

I checked the explanation against the IBM source, especially the ideas of tokens, training, inference, and next-token prediction. I also made sure that probability and next-token prediction were explained at an intuitive level rather than using unnecessary mathematical details.

### R — Reflection

I learned that an LLM does not simply search a database and copy an answer. It processes the input as tokens and generates a response step by step by predicting likely next tokens. I also understood why a response can sound convincing while still containing incorrect information, so the output should be verified when accuracy is important.

---

## Q4. Hallucination Experiment: Can AI Sound Confident and Still Be Wrong?

I tested the same factual question with two different AI assistants.

**Question asked to both tools:** What is the difference between RAM and ROM?

### ChatGPT Response

| RAM | ROM |
|---|---|
| Random Access Memory | Read-Only Memory |
| Temporary memory | Non-volatile memory |
| Data is lost when power is turned off | Data is retained when power is turned off |
| Used while the computer is running | Used to store firmware and startup instructions |
| Can be read and written frequently | Traditionally mainly read; modern ROM types can be rewritten in certain ways |
| Example: Programs currently running | Example: Firmware used during device startup |

**Summary:**

- RAM = Working memory that stores data temporarily.
- ROM = Stored instructions that remain available after the power is turned off.

### Gemini Response

Gemini explained that RAM and ROM serve different roles in a computer or microcontroller system.

**RAM (Random Access Memory):**

RAM acts as the system's temporary workspace. It is volatile memory, meaning all data stored in RAM disappears when power is disconnected. Applications, running software, and live sensor data can be stored in RAM because the processor frequently reads from and writes to it.

**ROM (Read-Only Memory):**

ROM is non-volatile memory designed to retain its contents even when the device is powered off. It stores important system instructions, such as firmware or bootloader code, that help initialise the hardware and start the system.

### E — Evidence

I checked the important claims from both answers against a reliable technical source.

**Verification source:** [IBM — What Is Primary Storage?](https://www.ibm.com/think/topics/primary-storage)

**Verified claim:** The claim that RAM is temporary memory while ROM retains its data when the power is turned off was supported by the IBM reference.

### V — Verification

I compared the answers from both AI assistants with the reference source instead of assuming that a confident-sounding answer was automatically correct. The main points about RAM and ROM were correct based on the reference.

### R — Reflection

This experiment showed me that two AI assistants can give similar answers, but that does not automatically make the information correct. Checking important claims against a reliable source gives more confidence in the result. It also showed me why AI output should be treated as information to verify rather than final proof.

---

## Q5. AI Assistant vs Search vs Authoritative Reference

For this comparison, I used the same technical question with three different methods.

**Question:** What is a multiplexer (MUX)?

- AI assistant: ChatGPT
- Web search engine: Google Search
- Authoritative reference: NPTEL (National Programme on Technology Enhanced Learning), IIT Kharagpur

### AI Assistant: ChatGPT

I first asked ChatGPT, "What is a multiplexer (MUX)?" ChatGPT explained that a multiplexer is a digital circuit that selects one input from several inputs and sends the selected input to a single output. It also explained that select lines are used to decide which input is selected.

### Web Search Engine: Google Search

I then searched the same question using Google Search. The search results provided explanations from different websites. The explanations were useful, but I had to check which sources were reliable before using the information.

### Authoritative Reference: NPTEL

Finally, I checked the answer using an NPTEL Digital Systems reference. The NPTEL material explains that a multiplexer is a combinational circuit that selects one of several inputs and connects the selected input to a single output. The selection is controlled by select inputs.

### Comparison Table

| Comparison Point | ChatGPT | Google Search | NPTEL Reference |
|---|---|---|---|
| Main purpose | Provides a direct explanation | Finds information from different websites | Provides technical educational material |
| Explanation style | Simple and easy to understand | Depends on the selected source | More formal and detailed |
| Reliability | Needs verification against a reliable source | Depends on the source selected | An identifiable educational reference can be checked |
| Verification | Check the claims and supporting sources | Open and evaluate the search results | Compare the explanation with the reference material |
| Best use | Quick explanations and examples | Finding different explanations and resources | Verifying important technical concepts |

### When I Would Use Each

I would use ChatGPT when I want a quick explanation, examples, or help understanding a technical concept.

I would use Google Search when I want to find different explanations, tutorials, or sources about a topic.

I would use an authoritative reference such as NPTEL when I need to verify an important technical fact or use reliable information in my work.

For important technical decisions or claims, I would not rely only on an AI-generated answer. I would check the information against a reliable technical or primary source.

### E — Evidence

I checked the definition of a multiplexer using an NPTEL Digital Systems reference.

**Authoritative reference:** [NPTEL — Digital Systems: Multiplexers](https://archive.nptel.ac.in/content/storage2/courses/106108099/Digital%20Systems.pdf)

The NPTEL reference explains that a multiplexer is a combinational circuit that selects one of several inputs and connects the selected input to a single output. It also explains that select inputs control which data input is selected.

### V — Verification

I compared the explanation from ChatGPT and the information found through Google Search with the NPTEL reference. The main definition was consistent: a multiplexer selects one input from multiple inputs based on the select inputs and sends the selected input to the output.

I used the NPTEL reference as the authoritative source because it provides technical educational material that can be directly checked.

### R — Reflection

This comparison showed me that AI is useful for getting a quick and simple explanation, while Google Search helps me find different sources. However, I should not assume that the first AI answer or search result is automatically correct. An authoritative reference is useful for verifying important technical information.

I learned that AI can help me understand a topic, but reliable sources are important when I need to confirm that the information is correct.

---

## Q6. What Is an AI Agent?

### Important Concepts

**LLM:** A Large Language Model is an AI model that works with language and can generate text based on the input and context it receives.

**LLM application:** An application that uses an LLM as one part of a larger software system to provide a specific function.

**RAG system:** Retrieval-Augmented Generation is a system where relevant information is retrieved from a source and provided to the model so that the response can use that information.

**Tool-using assistant:** An AI assistant that can use external tools, such as a calculator, search system, or software API, instead of only generating text.

**AI agent:** An AI system that works toward a goal by deciding steps, using models and tools, and carrying out actions as part of a workflow.

### Architecture Diagram

```text
User Request
     |
     v
AI Model / LLM
     |
     v
Decide Whether a Tool Is Needed
     |
     v
Tool Call
     |
     v
Tool Result
     |
     v
Model Processes the Result
     |
     v
Decision / Final Response
```

### Example

A travel-planning agent could receive a trip requirement, search available flights and hotels, compare the results, and prepare the next action.

### E — Evidence

**Source:** [IBM — What Are AI Agents?](https://www.ibm.com/think/topics/ai-agents)

### V — Verification

I checked the difference between an AI model and an AI agent using the IBM explanation. The main point I verified is that an agent is a larger system that can use an AI model together with tools and workflows to perform tasks.

### R — Reflection

I learned that an LLM and an AI agent are not the same thing. An LLM mainly provides the intelligence for understanding and generating language, while an agent can use a model as part of a larger process involving tools, decisions, and actions.

---

## Q7. Where Should Humans Still Make the Decision?

Even when an AI assistant can read documents, answer questions, summarise information, generate text, or suggest actions, I would still require human inspection or approval for important decisions.

### Human Verification and Approval Table

| Situation | Possible Failure | Required Verification | Who or What Approves? |
|---|---|---|---|
| Medical information or advice | The AI may give incorrect, incomplete, or unsuitable information. | Check the information with a qualified medical professional and reliable medical sources. | Doctor or qualified medical professional |
| Financial decision | The AI may miss important financial details or make an incorrect calculation. | Check the calculations, terms, risks, and relevant financial information. | Person making the decision or a qualified financial professional |
| Legal information | The AI may misunderstand a law or apply it incorrectly to a specific situation. | Check the relevant law and, when necessary, obtain professional legal advice. | Qualified legal professional |
| Engineering calculation or design | An incorrect calculation, assumption, or technical detail could lead to a wrong result. | Recalculate the result and compare it with trusted technical references or tools. | Engineer or technical reviewer |
| Important email or document | The AI may include incorrect facts, names, numbers, or unintended wording. | Check the facts, names, numbers, and intended meaning before sending or using it. | Human author or responsible person |

### E — Evidence

The Week 1 assessment emphasises that AI-assisted engineering should not mean handing responsibility over to an AI system. Important AI outputs should be inspected and verified before acting on them.

The assessment also requires identifying what evidence is needed and who or what should approve the result.

### V — Verification

For each situation, I considered what could go wrong if the AI output were accepted without checking it. I then identified a suitable verification method, such as checking a reliable source, recalculating the result, or getting approval from a qualified person.

### R — Reflection

I learned that AI can help with information and suggestions, but human responsibility is still important for decisions that can have significant consequences. The more important the decision, the more carefully the AI output should be checked before it is accepted or acted on.

**My simple rule:** AI can assist with a decision, but a human should inspect, verify, and approve important results before acting on them.

---

## Q8. Find AI Around You

I identified five systems or features that I encounter in everyday life and checked public information to see whether AI or machine learning is involved.

### 1. Google Maps

**AI/ML involved:** Yes. Google Maps uses AI and machine learning for traffic prediction and route selection.

**Main task:** Prediction and recommendation.

**Evidence:** [Google — How AI Helps Predict Traffic and Determine Routes](https://blog.google/products-and-platforms/products/maps/google-maps-101-how-ai-helps-predict-traffic-and-determine-routes/)

**Conclusion:** AI and machine learning are involved in predicting traffic and helping select routes.

### 2. Gmail Spam Detection

**AI/ML involved:** Yes. Gmail uses machine learning to identify patterns in emails and detect spam.

**Main task:** Classification.

**Evidence:** [Google — How Machine Learning in G Suite Makes People More Productive](https://blog.google/products-and-platforms/products/workspace/how-machine-learning-g-suite-makes-people-more-productive/)

**Conclusion:** Machine learning is used to classify emails and identify messages that are likely to be spam.

### 3. YouTube Recommendations

**AI/ML involved:** Yes. YouTube uses AI to help recommend and organise content for users.

**Main task:** Recommendation.

**Evidence:** [Google — How YouTube Is Using AI](https://blog.google/intl/en-in/products/platforms/how-youtube-is-using-ai-to-bring-you-more-of-what-you-love/)

**Conclusion:** AI is used to help recommend content based on user activity and other information.

### 4. Google Photos

**AI/ML involved:** Yes. Google Photos uses machine learning to identify people, pets, objects, and text in photos and videos.

**Main task:** Recognition and classification.

**Evidence:** [Google — Google Photos and AI](https://blog.google/products-and-platforms/products/photos/30-years-family-videos-ai-archive/)

**Conclusion:** Machine learning is used for recognising and organising information in photos and videos.

### 5. ChatGPT

**AI/ML involved:** Yes. ChatGPT uses AI models to understand instructions and generate responses.

**Main task:** Generation.

**Evidence:** [OpenAI — How ChatGPT and Our Foundation Models Are Developed](https://openai.com/policies/how-chatgpt-and-our-foundation-models-are-developed/)

**Conclusion:** Generative AI is used to create responses and other content from user instructions.

### E — Evidence

I used public information from Google and OpenAI rather than assuming that a feature was AI just because it appeared intelligent. The sources above describe the use of AI or machine learning in the selected systems.

### V — Verification

I checked each system against public information from the company responsible for the product. I looked for explicit statements about AI or machine learning rather than relying only on how the feature behaves. The evidence supports AI/ML involvement in all five examples listed above.

### R — Reflection

This question helped me realise that AI and machine learning are already used in many systems I interact with every day. I also learned that a system should not be called AI just because it appears intelligent. Public evidence is important for confirming how a system actually works.

A simpler rule-based system can sometimes produce similar behaviour, but machine learning can handle patterns and situations that are harder to describe with fixed rules.

---

## Q9. Prediction, Classification, and Generation

### Classification Table

| Example | Classification | Reason |
|---|---|---|
| A. Predicting house prices | Prediction | The system estimates a numerical value, such as the expected price of a house. |
| B. Detecting whether an image contains a cat | Classification | The system decides whether the image belongs to a particular category, such as "cat" or "not cat". |
| C. Writing an email from a short instruction | Generation | The system creates new text based on the instruction given by the user. |
| D. Predicting whether a customer will cancel a subscription | Prediction | The system estimates the likelihood of a future event, such as whether the customer will cancel. |
| E. Summarising a research paper | Generation | The system generates new text that presents the important information from the research paper in a shorter form. |
| F. Identifying whether a transaction is fraudulent | Classification | The system assigns the transaction to a category such as "fraudulent" or "not fraudulent". |
| G. Generating an image from a text description | Generation | The system creates a new image based on the text description provided by the user. |
| H. Predicting the next word or token in a sentence | Prediction | The system predicts which token is likely to come next based on the previous tokens and context. |

### Why Is Next-Token Prediction Fundamental to Modern Language Models?

Next-token prediction is fundamental because a language model generates text one token at a time. The model looks at the previous tokens and context, predicts possible next tokens, and selects a next token. This process is repeated to produce a complete response.

Because of this process, the same basic mechanism can be used in applications that look different on the surface, such as writing emails, summarising documents, answering questions, and generating code.

Some real AI systems can perform more than one type of task, but in this question I classified each example according to its primary behaviour.

### E — Evidence

I used the Week 1 concepts about prediction, classification, generation, and next-token prediction. I also checked the explanation of language-model generation from Q3.

**Source:** [IBM — What Is a Large Language Model?](https://www.ibm.com/think/topics/large-language-models)

### V — Verification

I checked each example based on what the system is mainly trying to produce. Numerical or future-value estimation was classified as prediction, assigning an input to a category was classified as classification, and creating new content was classified as generation.

I also verified that next-token prediction is the basic process used to generate language-model responses one token at a time.

### R — Reflection

I learned that prediction, classification, and generation describe different types of AI tasks. I also understood that next-token prediction can be used to generate many different types of language outputs, even when the final application looks like writing, summarisation, coding, or question answering.

---

## Q10. Design Your Personal AI Verification Protocol

I would follow these seven steps before accepting an AI-generated result.

### Step 1: Define the Problem

I first clearly identify what I am trying to solve and what result I need.

**Why:** This prevents me from solving the wrong problem.

### Step 2: Check the Input and Assumptions

I check the information given to the AI and identify any missing or incorrect assumptions.

**Why:** Incorrect or incomplete input can lead to an incorrect result.

### Step 3: Inspect the AI Response

I read the complete AI response carefully and look for unclear statements, missing information, or unusual results.

**Why:** This can help identify obvious mistakes before accepting the answer.

### Step 4: Check the Evidence and Source

I check important facts and claims against reliable sources or references.

**Why:** This helps identify unsupported or false information.

### Step 5: Test the Result

I recalculate, reproduce, compare, or otherwise test the result when possible.

**Why:** Testing can reveal errors that may not be obvious from the explanation.

### Step 6: Compare with Another Reliable Method or Source

I compare the AI result with another calculation, method, tool, or reliable reference.

**Why:** An independent check reduces the chance of accepting one incorrect answer.

### Step 7: Accept, Reject, or Revise

After checking everything, I decide whether to accept the result, reject it, or revise it before using it.

**Why:** This prevents me from automatically trusting the AI output.

### Worked Example

Suppose I ask an AI to calculate the total cost of buying several items.

1. **Define the problem:** I list the items and their prices.
2. **Check the input:** I check that the prices and quantities entered into the AI are correct.
3. **Inspect the response:** I inspect the AI's calculation and explanation.
4. **Check the evidence:** I check the prices against the actual bill or product information.
5. **Test the result:** I calculate the total myself using a calculator.
6. **Compare the results:** I compare my calculation with the AI's answer.
7. **Make a decision:** If both results agree, I can accept the result. If they differ, I investigate the calculation before using it.

### E — Evidence

The seven-step process is based on the Week 1 assessment workflow of defining, investigating, inspecting, verifying, concluding, documenting, and reflecting. The assessment also requires checking assumptions, evidence or sources, testing the result, and deciding whether to accept, reject, or revise the AI output.

### V — Verification

I checked that my seven steps include the required parts of the assessment: defining the problem, inspecting assumptions, checking evidence or sources, testing the result, and making an accept, reject, or revise decision.

### R — Reflection

I learned that getting an answer from AI is only the first step. I should inspect and verify the result before using it, especially when the result is important.

My main rule is to use AI as an assistant, but make the final decision only after checking the result.
