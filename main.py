import bot


class McChater:
    def __init__(self):
        self.log = "23.5.2②更新：更新了YUAN配置的ikun。"
        bot.create_bot(**{
            "host": "mc.icraft.cc",
            "username": 'Ciupui',
            "port": 49282,
            "version": "1.16.5",
        })

        self.op_list = ["wanghany"]
        bot.listen_msg()
        # kick = bot.on_kicked() 
        bot.chat("/l wurst7")
        bot.chat("/res tp DI_XIA_CHENG")
        bot.chat("INV，我是wanghany。我有点事qwq给我留点你的好东西啊 ")

        # bot.do_cmd(self.op_list)


chater = McChater()
bot.tpac()

bot.docmd()
bot.come()
bot.add_or_del_operator()
bot.fake_tps()
bot.on_dialog()


@bot.On(bot.bot, 'kicked')
def handle(*msg):
    print(msg[1])
