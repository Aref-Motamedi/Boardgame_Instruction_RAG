import torch
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

if torch.backends.mps.is_available():
    device = 'mps'
    use_pipeline_device = None
else:
    device = 'cpu'
    use_pipeline_device = -1

print(device)

MODEL_NAME = "meta-llama/Llama-3.2-3B-Instruct" 

pipe = pipeline(
    "text-generation",
    model = MODEL_NAME,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device = use_pipeline_device,
    max_length =256,
)

llm = HuggingFacePipeline(pipeline=pipe)

print(llm("Explain step by step, how old is the US president."))