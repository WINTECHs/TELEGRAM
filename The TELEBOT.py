import  requests

import pandas as pd

src_url = "https://raw.githubusercontent.com/WINTECHs/TELEGRAM/root-WINTECH/ChatSource.tsv"

data_frames = pd.read_csv(src_url, sep="\t")

base_url = "https://api.telegram.org/bot6713809050:AAE3PZE64N6Yv9CmrVHYV95u-RabGIwlilA/"


#Read Message

def read_msg(offset):
    #print(offset)

    parameters = {
        "offset" : offset
        
        }

    resp=requests.get(base_url+"getupdates", data = parameters)
    data=resp.json()
    print(data)
    
    for result in data["result"]:
        #if "hi" in result["message"]["text"]:
        send_msg(result["message"]["text"],result["message"]["chat"]["id"])

        if data["result"]:
            return data["result"][-1]["update_id"]+1

#Preparing Answer

def auto_ans(msg):
    
    ans = data_frames.loc[data_frames['Question'].str.lower() == msg.lower()]
    
    if not ans.empty:
        ans = ans.iloc[0]['Answer']
        return ans
    else:
        return "Sorry, I could not understand you !!! I am still learning and try to get better in answering."
    

#Send Message

def send_msg(msg,chat_id):
    
    ans = auto_ans(msg)
    print(chat_id)
    parameters = {
        "chat_id" : chat_id,
        "text" : ans
        }

    resp=requests.get(base_url+"sendMessage", data = parameters)
    print(resp.text)


#Inialization
    
offset = 0
while True:
    offset=read_msg(offset)
