BOTNAME = "Ciupui"

from javascript import require, On, Once
from yuan import inspurai
import yuan
import threading
import asyncio
import time

mineflayer = require("mineflayer")
# pathfinder, Movements, goals = require('mineflayer-pathfinder')
# pvp = requ ire('mineflayer-pvp').plugin


chater = mineflayer.createBot(
    {
        "host": "mc.icraft.cc",
        "username": BOTNAME,
        "port": 49282,
        "version": "1.16.5",
    }
)

@On(chater, "message")
def listen_msg(this, message, *args):
    print(message.toAnsi())

def chat_to_game(msg):
    @Once(chater, "spawn")
    def say(*args):
        chater.chat(msg)
        
chat_to_game("/l wurst7")
while True:
    chat_to_game("/w 123456bb 傻逼123456逼逼，乱逼逼，大挂逼，还挺有理，死鸭子嘴硬")
    time.sleep(1.5)