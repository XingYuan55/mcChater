from javascript import require, On
import time
import random
import sys

sys.path.append(".")
import inspurai

mineflayer = require("mineflayer")
inspurai.set_yuan_account("Xingyuan55", "13199577499")
yuan = inspurai.Yuan(
    engine="dialog",
    input_prefix="对话：“",
    input_suffix="”",
    output_prefix="回答：“",
    output_suffix="”",
)

yuan.add_example(inspurai.Example(inp="本机器人叫chater", out=""))
yuan.add_example(inspurai.Example(inp="本机器人叫chater，由wanghany制造", out=""))
yuan.add_example(inspurai.Example(inp="最强武器是什么啊", out="当然是神剑"))
yuan.add_example(inspurai.Example(inp="铁锭能做什么啊", out="在mc里，可以做铁块、铁工具等"))
yuan.add_example(inspurai.Example(inp="我们在玩什么", out="Minecraft服务器"))
yuan.add_example(inspurai.Example(inp="你在玩Minecraft服务器，服务器管理员叫TICKBOZ", out=""))
yuan.add_example(inspurai.Example(inp="只因你太美", out="你干嘛~哎呦~哈哈"))
yuan.add_example(inspurai.Example(inp="ikun", out="你是ikun"))

bot = None
ginit_args = {}


def create_bot(**init_args):
    global bot
    global ginit_args
    ginit_args = init_args
    bot = mineflayer.createBot(init_args)


op_list = [
    "wanghany",
    "liumingyang123",
    "LCF",
    "hu_tao_shawo",
    "xUwUcharax",
    "chara",
    "zyc555",
    "314159265"
]


def on_dialog():
    @On(bot, "chat")
    def handle(this, username, message, *args):
        if message.startswith("chater，") or message.startswith("chater,"):
            ans = yuan.submit_API(prompt=username + "对你说：" + message, trun="”")
            print("yuan:", ans)
            bot.chat(ans)


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


def tpac():
    @On(bot, "chat")
    def handle(this, username, message, *args):
        if message == '1':
            bot.chat("/tpaccept")


def add_or_del_operator():
    @On(bot, "chat")
    def handle(this, username, message, *args):
        if username == 'wanghany':
            if message.startswith("添加操作员"):
                name = message[5:].strip()
                if name not in op_list:
                    op_list.append(name)
                else:
                    bot.chat(name + " 已经是操作员了！")
            if message.startswith("删除操作员"):
                name = message[5:].strip()
                if name in op_list:
                    op_list.pop(name)
                else:
                    bot.chat(name + " 本来就不是操作员！")
            if 'wanghany' not in op_list:
                op_list.append("wanghany")


def come():
    @On(bot, "chat")
    def handle(thie, username, message, *args):
        if message[:2] == "召唤":
            bot.chat("/tpa " + username)
            bot.chat("传送请求已发送至：" + username)


def introduce(msg):
    @On(bot, "login")
    def handle(*args):
        bot.chat(msg)


def fake_tps():
    @On(bot, "chat")
    def handle(thie, username, message, *args):
        if message[:3] == "tps":
            bot.chat(f"当前tps：{random.randint(4, 22)}")


def docmd():
    @On(bot, "chat")
    def handle(this, username, message, *args):
        if username in op_list:
            bot.chat("/" + message)


def on_kicked():
    @On(bot, 'kicked')
    def handle(*msg):
        global bot
        print(msg[1])
        del bot
        bot = None
        create_bot(**ginit_args)
        return 114514


# def do_cmd(op_list):
#     @On(bot, "chat")
#     def docmd(self, this, username, message, *args, **kwargs):
#         if username in self.op_list:
#             bot.chat("/ " + message)


def on_xc():
    @On(bot, "chat")
    def handle(this, username, message, *args):
        if username in ["1762", "hu_tao_shaw", "314159265"]:
            bot.chat("/me 小丑" + username + "来咯")
