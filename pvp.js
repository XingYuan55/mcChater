const mineflayer = require('mineflayer')
const { pathfinder, Movements, goals } = require('mineflayer-pathfinder')
const pvp = require('mineflayer-pvp').plugin

const bot = mineflayer.createBot({
    host: "mc.icraft.cc",
    username: "_chater",
    port: 49282, 
    version: "1.16.5",
})

bot.loadPlugin(pathfinder)
bot.loadPlugin(pvp)

bot.on('chat', (username, message) => {
  if (message === 'fight me') {
    const player = bot.players[username]

    if (!player) {
      bot.chat("I can't see you.")
      return
    }

    bot.pvp.attack(player.entity)
  }

  if (message === 'stop') {
    bot.pvp.stop()
  }
})
function chat_to_game(msg)
{
    bot.once('spawn', () => { chater.chat(msg) })
}

bot.on('message', (message) => {
    console.log(message.toAnsi())
})

bot.on("login", (login) =>{
    chat_to_game("/l tt5566tt")
})