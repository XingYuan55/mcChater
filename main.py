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
        bot.chat('嗨嗨嗨，我又来了噢！额可以说‘召唤机器人’来召唤我，输入1我就能接受传送请求啦！ 推荐一个pvp好地方：res tp pvp')
        
        # bot.do_cmd(self.op_list)
    





chater = McChater()
bot.tpac()
bot.docmd()
bot.come()
@bot.On(bot.bot, 'kicked')
def handle(*msg):
    # global chater 
    print(msg[1])
    # del chater
    # chater = None
    # chater = McChater()

