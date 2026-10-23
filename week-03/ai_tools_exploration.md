# AI Tools Exploration

## 1. Objective

The objective of this activity is to explore AI tools for engineering learning, improve prompts, compare AI-generated explanations, and verify technical claims using reliable sources.

## 2. AI Tools Explored

### ChatGPT

ChatGPT was used to explain the VLSI Physical Design flow, organise technical concepts, and support prompt improvement.

### Google Gemini

Gemini was used to explain the same Physical Design topic. Its response included explanations of the five main stages and practical analogies.

### Claude

Claude is an AI assistant that can support technical explanations, document analysis, writing, and coding.

### NotebookLM

NotebookLM helps users study provided sources, summarise documents, and ask questions grounded in reference material.

### Perplexity

Perplexity supports web research and helps users discover sources that can be checked against original documentation.

The descriptions of Claude, NotebookLM, and Perplexity are introductory observations; I have not claimed to have tested every feature of these tools.

## 3. Prompt Engineering Experiment

### Basic Prompt

Explain Physical Design in VLSI.

### Improved Prompt

I am a BTech ECE student specialising in VLSI Physical Design. Explain the Physical Design flow in beginner-friendly language. Cover floorplanning, placement, clock tree synthesis (CTS), routing, and timing analysis. Explain the purpose of each stage and give one simple example. Use clear headings and keep the explanation concise.

### Observation

The improved prompt specifies the audience, topic, concepts to cover, examples required, and preferred format. This gives the AI a clearer direction and produces a more structured explanation.

## 4. Comparison of ChatGPT and Google Gemini

### Task

Both tools were used to explain the VLSI Physical Design flow using the same improved prompt.

### Comparison

| Criterion | ChatGPT | Google Gemini |
|---|---|---|
| Main concepts | Explained the main Physical Design stages | Explained all five stages |
| Technical detail | Provided a beginner-friendly overview | Included terms such as GDSII, clock skew, DRC, setup, and hold |
| Examples | Used a general explanatory approach | Provided a separate analogy for each stage |
| Structure | Organised the explanation by stage | Used headings, purposes, and examples |
| Follow-up learning | Can explain concepts in further detail | Suggested exploring setup and hold optimisation |

### Comparison Findings

Both tools explained floorplanning, placement, clock tree synthesis, routing, and timing analysis. Gemini's response included more detailed technical terminology and a separate analogy for each stage. These features made its answer useful for visualising the concepts.

The comparison is based on the responses observed in this experiment. Technical accuracy still needs to be checked against reliable references.

## 5. Verification of an AI-Generated Claim

### Claim

Clock tree synthesis creates a clock distribution network to deliver the clock signal to sequential elements while controlling clock skew and latency.

### Verification Source

OpenROAD documentation:

https://openroad.readthedocs.io/

### Verification Method

1. Consult the official documentation for clock tree synthesis.
2. Check the documented purpose of clock distribution and the relevant configuration or reporting options.
3. Compare the documented behaviour with the AI-generated claim.
4. Record the result and any limitations after checking the source.

### Verification Result

To be completed after checking the relevant official documentation. The claim should not be marked as verified until the source has been inspected.

## 6. Responsible AI Usage

- Check technical claims using official documentation or other reliable references.
- Do not assume that a confident or detailed answer is automatically correct.
- Avoid uploading confidential design information to public AI tools.
- Review and understand AI-generated code before using it.

## 7. Conclusion

This activity demonstrated how prompt improvement can guide AI responses and how two tools can explain the same engineering topic differently. Comparing responses helps identify differences in structure, terminology, and examples. Independent verification remains necessary before accepting technical claims.
