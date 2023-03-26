import bot, time


class McChater:
    def __init__(self):
        bot.create_bot(**{
                "host": "mc.icraft.cc",
                "username": 'chater',
                "port": 49282,
                "version": "1.16.5",
            })

        self.op_list = ["wanghany"]
        bot.listen_msg()
        # kick = bot.on_kicked()
        bot.login("tt5566tt")
        bot.do_cmd(self.op_list)
    





chater = McChater()
@bot.On(bot.bot, 'kicked')
def handle(*msg):
    # global chater 
    print(msg[1])
    # del chater
    # chater = None
    # chater = McChater()
    
@bot.On(bot.bot, 'chat')
def handlemr(this, username, message , *args):
    if(username == '123456bb'):
            bot.chat("/w 123456bb 傻逼123456逼逼，乱逼逼，大挂逼，还挺有理，死鸭子嘴硬，没下辈子的人，还乱跟你妈狗叫说：“我的火葬场粘锅了”")
            bot.chat("/w 123456bb 傻逼123456逼逼，乱逼逼，大挂逼，还挺有理，死鸭子嘴硬，没下辈子的人，还乱跟你妈狗叫说：“我的火葬场粘锅了”")
            bot.chat("/w 123456bb 傻逼123456逼逼，乱逼逼，大挂逼，还挺有理，死鸭子嘴硬，没下辈子的人，还乱跟你妈狗叫说：“我的火葬场粘锅了”")
            bot.chat("/w 123456bb 傻逼123456逼逼，乱逼逼，大挂逼，还挺有理，死鸭子嘴硬，没下辈子的人，还乱跟你妈狗叫说：“我的火葬场粘锅了”")
            bot.chat("/w 123456bb 傻逼123456逼逼，乱逼逼，大挂逼，还挺有理，死鸭子嘴硬，没下辈子的人，还乱跟你妈狗叫说：“我的火葬场粘锅了”")

    

