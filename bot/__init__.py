from javascript import require, On, Once
import time

mineflayer = require("mineflayer")

bot = None
ginit_args = {}
def create_bot(**init_args):
    global bot
    global ginit_args
    ginit_args = init_args
    bot = mineflayer.createBot(init_args)


def listen_msg():
    @On(bot, "message")
    def handle(this, message, *args):
        print(message.toAnsi())


def chat(msg):
    @On(bot, "spawn")
    def say(*args):
        bot.chat(msg)

def register(password):
    chat("/register " + password + " " + password)

def login(password):
    @On(bot, "spawn")
    def handle(*args):
        bot.chat("/l " + password)

def on_kicked():
    @On(bot, 'kicked')
    def handle(*msg):
        global bot
        print(msg[1])
        del bot
        bot = None
        create_bot(**ginit_args)
        return 114514
    
def do_cmd(op_list):
    @On(bot, "chat")
    def docmd(self, this, username, message, *args, **kwargs):
        if username in self.op_list:
            bot.chat("/ " + message)
    

