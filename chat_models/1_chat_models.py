from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI(model="gpt-4o", temperature=0.7)
prompt="how are you?"
response=llm.invoke(prompt)
print(response.content)
