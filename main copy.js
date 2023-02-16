const mineflayer = require("mineflayer")  // 导入mineflayer
const { pathfinder, Movements, goals } = require('mineflayer-pathfinder')
const pvp = require('mineflayer-pvp').plugin



const chater = mineflayer.createBot(
    {
        host: "mc.icraft.cc",
        username: "chater",
        port: 49282, 
        version: "1.16.5",
    }
)

chater.loadPlugin(pathfinder)
chater.loadPlugin(pvp)
chater.on('chat', (username, message) => {
    if (message === 'dr') {
      chat_to_game("/tpa Regedit")

      const player = chater.players['Regedit']
  
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

chater.on('message', (message) => {
    console.log(message.toAnsi())
})

// chater.on("login", (login) =>
//     chat_to_game("/l tt5566tt")
// })
chat_to_game("/l tt5566tt")
chat_to_game("/tpa Regedit")


