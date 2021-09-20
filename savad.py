import json
import requests
import time
import urllib
import sqlite3
from sqlite3 import Error



TOKEN = '1391583443:1NDTayVHoX3s64dSauMsrbsJvoVoueNpiYOtuM5D'
URL = "https://tapi.bale.ai/{}/".format(TOKEN)

print(URL);


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    print(js);
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    for update in updates["result"]:
        print(update)
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]

    
    if (text ==" تعريف سواد رسانه اي"):
        try:

         conn = sqlite3.connect('c:/azmayeshi/az3.db')
         
         send_message ('تعاريف سواد رسانه اي', chat_id=138511752)
         
         cursor = conn.execute("SELECT tarif,edalat,janbeha,maharat from SAVAD")
         
         for row in cursor:
           
           send_message (" "+str(row[0]), chat_id=138511752)
        except Exception as e: 
         print(e)
        finally:
            conn.close()          

           
     




    elif (text =="عدالت در سواد رسانه ای"):  
           try:

            conn = sqlite3.connect('c:/azmayeshi/az3.db')
         
            send_message ('عدالت در سواد رسانه اي', chat_id=138511752)
         
            cursor = conn.execute("SELECT tarif,edalat,janbeha,maharat from SAVAD")
         
            for row in cursor:
           
              send_message (" "+str(row[1]), chat_id=138511752)

           except Exception as e: 
             print(e)
           finally:
                conn.close()              

              
     



        

    elif (text =="جنبه های سواد رسانه ای"):  
           try:

            conn = sqlite3.connect('c:/azmayeshi/az3.db')
         
            send_message ('جنبه های سواد رسانه ای', chat_id=138511752)
         
            cursor = conn.execute("SELECT id,tarif,edalat,janbeha,maharat from SAVAD")
         
            for row in cursor:
           
              send_message (" "+str(row[2]), chat_id=138511752)
           except Exception as e: 
             print(e)
           finally:
                conn.close()              

              
     





    elif (text =="مهارتهای سواد رسانه ای"):  
           try:

            conn = sqlite3.connect('c:/azmayeshi/az3.db')
         
            send_message ('مهارتهاي سواد رسانه اي', chat_id=138511752)
         
            cursor = conn.execute("SELECT tarif,edalat,janbeha,maharat from SAVAD")
         
            for row in cursor:
           
              send_message (" "+str(row[3]), chat_id=138511752)
           except Exception as e: 
             print(e)
           finally:
                conn.close()              

              
    else:
        send_message ('پيغام شما نامعتبر است', chat_id=138511752) 









import telegram

from telegram import ReplyKeyboardMarkup

bot = telegram.Bot('1391583443:kqJ2iD38WLSNQckKhC76iKRfL6E4DyyCZvQrsJu5')

menu_keyboard = [[' تعريف سواد رسانه اي'], ['عدالت در سواد رسانه ای'], ['جنبه های سواد رسانه ای'], ['مهارتهای سواد رسانه ای']]

menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)

bot.send_message(chat_id=138511752, text='به ربات سواد رسانه اي خوش آمديد.لطفا يکي از گزينه هاي زير راانتخاب کنيد', reply_markup=menu_markup) 

            
 



def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
