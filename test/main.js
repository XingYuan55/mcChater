const mineflayer = require("mineflayer")  // 导入mineflayer
const { pathfinder, Movements, goals } = require('mineflayer-pathfinder')
const pvp = require('mineflayer-pvp').plugin



const chater = mineflayer.createBot(
    {
        host: "mc.icraft.cc",
        username: "_chater",
        port: 49282, 
        version: "1.16.5",
    }
)

chater.loadPlugin(pathfinder)
chater.loadPlugin(pvp)
chater.on('chat', (username, message) => {
    if (message === 'dw') {
      chat_to_game("/tpa " + username)

      const player = chater.players[username]
  
      if (!player) {
        chater.chat("I can't see you.")
        return
      }
  
      chater.pvp.attack(player.entity)
    }
    if (message === 'dk') {
      chat_to_game("/tpa " + 'Karma_Poggi')

      const player = chater.players['Karma_Poggi']
  
      if (!player) {
        chater.chat("I can't see you.")
        return
      }
  
      chater.pvp.attack(player.entity)
    }
  
    if (message === 'stop') {
        chater.pvp.stop()
    }
  })
function chat_to_game(msg)
{
    chater.once('spawn', () => { chater.chat(msg) })
}


chater.on('chat', (username, message) => {
    if(username == chater.username) return;
    if(message == '1')  chater.chat("/tpaccept")
})
chater.on('chat', (username, message) => {
  if(username != 'wanghany') return;
  chater.chat("/" + message)
})
chater.on('message', (message) => {
    console.log(message.toAnsi())
})

// chater.on("login", (login) =>
//     chat_to_game("/l tt5566tt")
// })

chat_to_game("/l 登录！")
chat_to_game("有人吗？wanghany马上来")
chat_to_game("/tpa wanghany")
chat_to_game("/tpa wanghany")


