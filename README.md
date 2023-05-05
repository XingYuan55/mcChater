# mcChater

## 1、介绍

chater 是 Xingyuan55 编写的、适用于《Minecraft: Java Edition》的多人服务器的聊天机器人。
它使用[Yuan-1.0 超大规模预训练中文模型](https://air.inspur.com/)进行支持聊天功能。
此外，它还有接受传送、登录自我介绍、执行指令、自助挂机等功能，是您游玩服务器的小助手。

## 2、bot 库使用方法

**以下无参数函数均为功能开关**

### **·** 1 bot.on_dialog()

开启 yuan 对话。以 chater 打头的游戏内消息就会回复。

### **·** 2 bot.listen_msg()

持续将游戏内消息以全彩色输出到控制台。

### **·** 3 bot.chat(msg)

对原 mineflayer.bot.chat 的封装。可以在别处直接引用。以机器人的身份在游戏里发送`msg`参数的信息。

### **·** 4 bot.introduce(msg)

令机器人在登陆时发送`msg`参数的信息

### **·** 5 bot.tpac()

开启接受传送请求(`/tpaccept`)功能。游戏内发送 1 以令机器人接受请求。

### **·** 6 bot.come()

令机器人向 发送以召唤打头的人 发送传送请求。
