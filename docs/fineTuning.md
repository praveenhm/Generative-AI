#### Fine tuning

```zsh
Fine-Tuning Process

Rule of thumb RAG vs FINE TUNE(quite basic):
  - if you want to infuse knowledge into your LLM replies, use RAG
  - if you want your LLM to reply in a certain style, like JSON, use fine-tuning
  Do not try to fine-tune your model, expecting it to learn the data of your company. It's just going to make the waters murky, and you will spend a lot of time and resources waiting for it to train.

Why search is better than fine-tuning
  GPT can learn knowledge in two ways:

  -Via model weights (i.e., fine-tune the model on a training set)
  -Via model inputs (i.e., insert the knowledge into an input message)

  Although fine-tuning can feel like the more natural option—training on data is how GPT learned all of its other knowledge, after all—we generally do not recommend it as a way to teach the model knowledge. Fine-tuning is better suited to teaching specialized tasks or styles, and is less reliable for factual recall.

  As an analogy, model weights are like long-term memory. When you fine-tune a model, it's like studying for an exam a week away. When the exam arrives, the model may forget details, or misremember facts it never read.

  In contrast, message inputs are like short-term memory. When you insert knowledge into a message, it's like taking an exam with open notes. With notes in hand, the model is more likely to arrive at correct answers.

=========================================

- Actual fine-tuning is easy part 
  - Many tools available - FastChat, Axolot, Deepspeed, Transformers, LoRA, qLoRA
  - Just grab example from repositories and tweak for your model and data
- Real challenge is preparing and formatting the data

Data Preparation

- Massive wiki, PDFs, forums - useless if data not in right format
- Enriching data improves results e.g. Dolly, Orca
- Multi-step Q&A also works well e.g. Vicuna
- Many dataset formats depending on expected usage
- Most projects use #instruction, #input, #output format
  - Flexible format for most fine-tuning tasks
- Shaping data into correct format is most difficult and time consuming step

Data Cleaning

- Can use GPT-4 to assist with data preparation
  - Avoid if highly sensitive data
  - Any public data should not contain sensitive info  
- Automated tools have limits, manual work is indispensable
- Those who understand product/process should validate data
- Even with GPT-4, can still fail due to:
  - Outdated information
  - Contradictory responses
- Involve large internal team to review and correct data
- Simple internal tool to edit rows or flag invalid ones

Model Training

- With large dataset (>10k examples), fine-tune full model
  - Follow initial training process from model repositories 
- With smaller dataset, use LoRA or qLoRA fine-tuning
  - Start with examples from LoRA/qLoRA repositories
  - Experiment with different settings
  - qLoRA training is trial-and-error process

Deployment

- Don't directly expose fine-tuned model to clients
- Run client queries through model internally first 
- Manually correct model responses before public use
- May need further fine-tuning or redo with corrected data


Conclusion

- Data quality is absolute most important factor
- Properly formatting data for model is very challenging
- Manual validation by domain experts is indispensable
- Continued monitoring and improvement critical after deployment

Let me know if you would like me to expand or add any clarification to this very detailed outline.
