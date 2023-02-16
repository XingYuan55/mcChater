BOTNAME = "chater"


from javascript import require, On, Once 
from yuan import inspurai
import yuan
import threading
import asyncio
import time
mineflayer = require("mineflayer")
pathfinder, Movements, goals = require('mineflayer-pathfinder')
pvp = require('mineflayer-pvp').plugin

op_list = [
    "wanghany",
    "TLttz",
    "C418____11",
    "chara",
]

chater = mineflayer.createBot(
    {
        "host": "mc.icraft.cc",
       "username": BOTNAME,
        "port": 49282, 
    "version": "1.16.5",
    }
)
<<<<<<< HEAD
=======
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
>>>>>>> FETCH_HEAD

# chater.loadPlugin(pathfinder)
# chater.loadPlugin(pvp)

yuan.set_yuan_account("Xingyuan55", "13199577499") 
yuan = inspurai.Yuan(engine='translate',
            input_prefix="将下列中文翻译成英文。中文：",
            input_suffix="",
            output_prefix="英文：",
            output_suffix="",
            append_output_prefix_to_query=True,
            # topK=6,
            # temperature=0.6,
            # max_tokens=100,
            # topP=0.75,
            # frequencyPenalty=1.2
            )
# yuan.add_example(inspurai.Example(inp='该聊天机器人名叫chater，女，16岁，居住地黑龙江。', out='该聊天机器人名叫chater，女，16岁，居住地黑龙江。'))

def strstartwith(str, e):
    if str[1] == e[0]: return True
    else: return False 

# @On(chater, "chat")
# def pvper(this, username, message, *args):
#     if(message == 'dw'):
#         player = chater.players[username]
#         if not player:
#             chater.chat("你搁哪呢")
#             return None
#         chater.pvp.attack(player.entity)
#     if message == 'stop':
#         chater.pvp.stop()

@On(chater, "login")
def login(this):
    chater.chat("/l tt5566tt")


def chat_to_game(msg):
    @Once(chater, "spawn")
    def say(args):
        chater.chat(msg)

@On(chater, "message")
def listen_msg(this, message, *args):
    print(message.toAnsi())

@On(chater, "chat")
def tpac(this, username, message, *args):
    if message == '1':
        chater.chat("/tpaccept")

@On(chater, "chat")
def docmd(this, username, message, *args):
    if username in op_list:
        chater.chat("/" + message)


@On(chater, "chat")
def handle(this, username, message, *args):
    if len(message) > 2:
        if message[:2] == "翻译" and username != BOTNAME:
            
            # msg = username+": "+message
            response = str(yuan.submit_API(prompt=message[2:], trun="").strip())
            # print("##YUAN", response)
            chater.chat("/w" + " " + username + " " + response)
# print(dir(chater))
