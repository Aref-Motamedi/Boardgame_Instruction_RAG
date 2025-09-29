import torch
from langchain_huggingface import HuggingFacePipeline, HuggingFaceEmbeddings
from transformers import pipeline
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

if torch.backends.mps.is_available():
    device = 'mps'
    use_pipeline_device = 0
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
    batch_size = 1,
)

llm = HuggingFacePipeline(pipeline=pipe)

# print(llm("Explain step by step, how old is the US president."))

loader = DirectoryLoader("./documents", glob='*.txt', loader_cls = TextLoader)
documents = loader.load()

textSplitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
texts = textSplitter.split_documents(documents)

print(f'Split text into {len(texts)} chunks')


embeddings = HuggingFaceEmbeddings(
    model_name = 'sentence-transformers/all-MiniLM-L6-v2',
    model_kwargs = {'device':'cpu'},
)

vectorstore = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    persist_directory="./chroma_db",
)

retriever = vectorstore.as_retriever(search_kwargs={'k':3})

prompt_template = """Use the following context to answer the question. 
If you don't know, say so. Keep your answer concise.

Context: {context}

Question: {question}

Answer:"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=['context','question']
)

qa_chain = RetrievalQA.from_chain_type(
    llm = llm,
    chain_type = 'stuff',
    retriever= retriever,
    return_source_documents=True,
    chain_type_kwargs={'prompt':PROMPT}
)

print('\n\n','='*30,'\n')

flag=True

while flag:
    user_input = input('Ask a question (EXIT for exit): ')
    if user_input == 'EXIT':
        flag=False
    else:
        result = qa_chain({'query': user_input})
        print(result['result'])
        print('-'*30,'\n')