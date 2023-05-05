import bot, time


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
        bot.introduce('/me 嗨嗨嗨，我又来了噢！我是wangh***的jqr可以说‘召唤机器人’来召唤我，输入1我就能接受传送请求啦！ 某些人输入不包括/的命令我就能执行了（如输入suicide）（说完没反应就是你没有权限）！以“chater，”开头的消息我就能回复了！（该功能正在开发中，不稳定） log:' + self.log)
        
        # bot.do_cmd(self.op_list)
    





chater = McChater()
bot.tpac()

bot.docmd()
bot.come()
bot.add_or_del_operator()
bot.fake_tps()
bot.on_dialog()
# bot.on_xc()
@bot.On(bot.bot, 'kicked')
def handle(*msg):
    # global chater 
    print(msg[1])
    # del chater
    # chater = None
    # chater = McChater()

