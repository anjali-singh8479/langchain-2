import os
from langchain_community.embeddings import HuggingFaceEmbeddings,OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
load_dotenv()
cur_dir=os.path.dirname(os.path.abspath(__file__))
# print(cur_dir)
extracted_cards_path= os.path.join(cur_dir,'bot_data', 'extracted_cards.txt')
cards_path= os.path.join(cur_dir,'bot_data', 'cards.txt')
links_path=os.path.join(cur_dir,'bot_data', 'links_in_bot.txt')
persistent_path=os.path.join(cur_dir,'vectors', 'chroma_db')
#loading the data for chunks
loader= TextLoader(extracted_cards_path,encoding="utf-8")
documents=loader.load()
# RecursiveCharacterTextSplitter
splitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
splitter.split_documents(documents)

# embedding_model=HuggingFaceEmbeddings(
embedding_model=HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)  
vector_store=FAISS.from_documents(documents,embedding_model)
# vector_store.save_local(db_dir)

query="qsg for bike cam"

app = FastAPI()
class Question(BaseModel):
    question: str
@app.post("/query")
def query_bot(data: Question):
    query=data.question
    # return {"message": data}
    similar_chunks=vector_store.similarity_search(query,k=1)

    # for i, doc in enumerate(similar_chunks):
    #     pa
    #     print(f"document {i}\n {doc.page_content}\n{doc.metadata}\n")

    input=(
        "Here are some of the documents that can help you to answer the question- "+
        query
        +"relevant documents are\n"
        +"\n\n".join([doc.page_content for doc in similar_chunks])
        +"please provide answer based on the document provided only"
        )
    model=OpenAI(model="gpt-4o-mini")
    message=[SystemMessage(content="You are a qubo assistant and are here to resolve issues related to qubo devices"),
            HumanMessage(content=input)]
    response=model.invoke(message)
    response=AIMessage(content=response)
    print("response:", response)
    return response

