# 💬 LangChain Chatbot – OpenAI Integration Project

This project demonstrates how to build a basic chatbot refernce used- https://www.youtube.com/watch?v=yF9kGESAi3M&ab_channel=aiwithbrandon

# 1. Setting the virtual environment for python
python -m venv .venv

# 2. Creating a basic chatbot model for open api
Install langchain_openai, dotenv

# 3. Passing chathistory as a prompt.

# 4. Storing chathistory on cloud(using firebase)
login to your firebase account
create a new project by going to firebase console
Generate new private key by going Project Settings > Service Accounts 
intall firebase-admin sdk file, then store it in your project folder
install 

# 5. Install firebase package
1. 
pip install firebase-admin , langchain_google_firestore, google-cloud-firestore
from firebase-admin import firebase
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory

# 2.
setup variable for project id, session id, collection and store values(prject id one you created)
setup client by using- client=firestore.Client(project=project id)
setup the collection- db=client.collection(your collection name)
now finally you can created document in this collection like- db.add({your json here}) OR db.document(document name).set({your json here})




