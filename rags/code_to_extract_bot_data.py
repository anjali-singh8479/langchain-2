import os
import json
from langchain.docstore.document import Document
# import file_system as fs
cur_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(cur_dir, 'bot_data', 'Bot all data.txt')
cards_path= os.path.join(cur_dir,'bot_data', 'cards.txt')
extracted_cards_path= os.path.join(cur_dir,'bot_data', 'extracted_cards.txt')
# #this gets all card data from the file
# with open(file_path, "r", encoding="utf-8") as f:
#     print("Reading bot data from file...")
#     bot_data = json.load(f)
# cards_data = bot_data.get("action_data", {})
# if cards_data:
#     print("Cards data loaded successfully.")
#     with open(cards_path, "w") as file:
#         file.write(json.dumps(cards_data, indent=4))
# # getting all cards data from the file code ende here

# # gets the extracted cards data from the cards file

# docs = []
# # print(cards_data)
# with open(cards_path, "r", encoding="utf-8") as f:
#     cards = json.load(f) 
#     cards_data = cards.get("en", {})      
# for card_id, card in cards_data.items():
#     card_name = card.get("name", "Unnamed Card")
#     rendering = card.get("rendering_config", {})
#     action= rendering.get("action", "No Action")
#     replies= rendering.get("replies", [])
#     for reply in replies:
#         message = reply.get("text")
#         links=reply.get("links")
#         if links:
#             link=links[0].get("url")
#             text= links[0].get("text", "No Text")
#             data={
#             "message":card_name,
#               "link":link
#             }
#         else:
#             data = {"message": card_name}
#     suggestions = rendering.get("suggestions", [])
#     options=[]
#     for suggestion in suggestions:
#         options.append(suggestion.get("text"))
#     data["options"] = options
#     behavior = rendering.get("behavior", "No Behavior")
#     if(behavior== "wait_for_user_input"):
#         card_type="Button Card"
#     else:
#         card_type="Message Card" 
#     doc=Document(page_content=str(data), metadata={"card_type": card_type, "card_name": card_name})
#     docs.append(doc)
# with open(extracted_cards_path, 'w',encoding="utf-8") as file:
#     for item in docs:
#         file.write(str(item) + "\n")
# # Save the extracted cards data to a file and code for same ends here

# getting all links
links_docs=[]
with open(cards_path,"r",encoding="utf-8") as file:
    cards_data=json.load(file)
    cards_data = cards_data.get("en", {})  
    for card_id, card in cards_data.items():
        card_name = card.get("name", "Unnamed Card")
        rendering = card.get("rendering_config", {})
        replies=rendering.get("replies",[])
        for reply in replies:
            links=reply.get("links")
            if(links):
                links_docs.append({card_name:links[0].get("url")})
with open(os.path.join(cur_dir,"bot_data","links_in_bot.txt"),"w", encoding="utf-8")as file:
    for link in links_docs:
        file.write(str(link)+"\n")





