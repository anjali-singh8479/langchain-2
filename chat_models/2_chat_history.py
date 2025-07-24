from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage,   SystemMessage
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-4o", temperature=1)
chathistory=[]
system_message=SystemMessage(
    content="You are a qubo agent and your task is to assist users in solving issues related to qubo devices and queries."
)
chathistory.append(system_message)
# chathistory=[
#     {"role": "system", "content": "You are a qubo agent and your task is to assist users in solving issues related to qubo devices and queries."},]
while True:
    user_query=input("Enter your query: ")
    if(user_query.lower() == "exit"):
        print("Exiting the chat. Goodbye!")
        break
    chathistory.append(HumanMessage(content=user_query))
    # chathistory.append({"role": "user", "content": user_query})
    response=llm.invoke(chathistory)
    chathistory.append(AIMessage(content=response.content))
    # chathistory.append({"role": "assistant", "content": response.content})
    print(response.content)
# print("Chat history:")
# print(chathistory)