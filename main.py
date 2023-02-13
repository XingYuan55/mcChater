from javascript import require, On, Once 
from yuan import inspurai
import yuan
import time
mineflayer = require("mineflayer")


chater = mineflayer.createBot(
    {
        "host": "mc.icraft.cc",
       "username": "_chater",
        "port": 49282, 
    "version": "1.16.5",
    }
)
yuan.set_yuan_account("yuan账号", "手机") 
yuan = inspurai.Yuan(engine='dialog',
            input_prefix="问：“",
            input_suffix="”",
            output_prefix="答：“",
            output_suffix="”",
            append_output_prefix_to_query=True,
            topK=5,
            temperature=1,
            topP=0.8,
            frequencyPenalty=1.2)


def strstartwith(str, e):
    if str[1] == e[0]: return True
    else: return False 


@On(chater, "login")
def login(this):
    chater.chat("/l tt5566tt")
    chater.chat("嗨嗨嗨，chater来咯 ")


def chat_to_game(msg):
    @Once(chater, "spawn")
    def say(args):
        chater.chat(msg)

@On(chater, "message")
def listen_msg(this, message, *args):
    print(message.toAnsi())
    
@On(chater, "chat")
def handle(this, username, message, *args):
    msg = username+": "+message
    response = str(yuan.submit_API(prompt=msg, trun="”").strip())
    print("##YUAN", response)
    if(len(message) >= 5 and len(message) <= 15):
        chater.chat(response)
    else:
        chater.chat(f"/w {username} {response}")

